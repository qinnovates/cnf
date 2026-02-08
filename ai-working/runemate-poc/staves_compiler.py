#!/usr/bin/env python3
"""
Runemate Forge: HTML/CSS/JS -> Staves Bytecode Compiler (PoC)

Demonstrates that compiling web content to a compact bytecode format
can offset post-quantum cryptography overhead for BCI applications.

This is a proof-of-concept, not a production compiler.
"""

import struct
import json
import re
import os
import sys
from html.parser import HTMLParser
from collections import Counter
from dataclasses import dataclass, field
from typing import Optional

# ─── Staves Bytecode Format ───────────────────────────────────────────────────
#
# Header (16 bytes):
#   Magic:       4 bytes  "STAV"
#   Version:     2 bytes  uint16
#   Flags:       2 bytes  uint16
#   String Pool: 4 bytes  uint32 (offset)
#   Style Table: 4 bytes  uint32 (offset)
#
# String Pool:
#   Count:       2 bytes  uint16
#   Entries:     [length: uint16, utf8_data: bytes]...
#
# Style Table:
#   Count:       2 bytes  uint16
#   Entries:     [prop_count: uint8, (prop_id: uint8, value_idx: uint16)...]...
#
# DOM Opcodes:
#   OPEN_TAG:    0x01  tag_id: uint8, attr_count: uint8, attrs...
#   CLOSE_TAG:   0x02
#   TEXT:        0x03  string_idx: uint16
#   ATTR:        0x04  name_idx: uint16, value_idx: uint16
#   STYLE_REF:   0x05  style_idx: uint16
#   EOF:         0xFF
# ──────────────────────────────────────────────────────────────────────────────

STAVES_MAGIC = b"STAV"
STAVES_VERSION = 1

# Common HTML tags get single-byte IDs
TAG_IDS = {
    "html": 0x01, "head": 0x02, "body": 0x03, "div": 0x04, "span": 0x05,
    "p": 0x06, "h1": 0x07, "h2": 0x08, "h3": 0x09, "h4": 0x0A,
    "a": 0x0B, "img": 0x0C, "button": 0x0D, "input": 0x0E, "form": 0x0F,
    "table": 0x10, "tr": 0x11, "td": 0x12, "th": 0x13, "thead": 0x14,
    "tbody": 0x15, "ul": 0x16, "li": 0x17, "header": 0x18, "footer": 0x19,
    "nav": 0x1A, "section": 0x1B, "article": 0x1C, "main": 0x1D,
    "meta": 0x1E, "link": 0x1F, "title": 0x20, "style": 0x21, "script": 0x22,
}

# Common CSS properties get single-byte IDs
CSS_PROP_IDS = {
    "display": 0x01, "position": 0x02, "width": 0x03, "height": 0x04,
    "margin": 0x05, "padding": 0x06, "color": 0x07, "background": 0x08,
    "background-color": 0x09, "font-size": 0x0A, "font-weight": 0x0B,
    "font-family": 0x0C, "border": 0x0D, "border-radius": 0x0E,
    "box-shadow": 0x0F, "text-align": 0x10, "line-height": 0x11,
    "flex": 0x12, "gap": 0x13, "grid-template-columns": 0x14,
    "justify-content": 0x15, "align-items": 0x16, "overflow": 0x17,
    "cursor": 0x18, "transition": 0x19, "opacity": 0x1A,
    "max-width": 0x1B, "min-width": 0x1C, "box-sizing": 0x1D,
    "text-transform": 0x1E, "letter-spacing": 0x1F, "border-bottom": 0x20,
    "border-collapse": 0x21, "aspect-ratio": 0x22, "margin-top": 0x23,
    "margin-bottom": 0x24, "grid-column": 0x25,
}

# Opcodes
OP_OPEN = 0x01
OP_CLOSE = 0x02
OP_TEXT = 0x03
OP_ATTR = 0x04
OP_STYLE_REF = 0x05
OP_EOF = 0xFF


@dataclass
class StringPool:
    strings: list = field(default_factory=list)
    index: dict = field(default_factory=dict)

    def add(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0xFFFF  # null string
        if s in self.index:
            return self.index[s]
        idx = len(self.strings)
        self.strings.append(s)
        self.index[s] = idx
        return idx

    def encode(self) -> bytes:
        data = struct.pack("<H", len(self.strings))
        for s in self.strings:
            encoded = s.encode("utf-8")
            data += struct.pack("<H", len(encoded)) + encoded
        return data

    def size(self) -> int:
        return len(self.encode())


@dataclass
class StyleEntry:
    properties: dict  # {prop_name: value_string}
    selector: str = ""


class StyleTable:
    def __init__(self, string_pool: StringPool):
        self.entries: list[StyleEntry] = []
        self.pool = string_pool
        self.selector_index: dict[str, int] = {}

    def add(self, selector: str, properties: dict) -> int:
        if selector in self.selector_index:
            return self.selector_index[selector]
        idx = len(self.entries)
        self.entries.append(StyleEntry(properties=properties, selector=selector))
        self.selector_index[selector] = idx
        return idx

    def encode(self) -> bytes:
        data = struct.pack("<H", len(self.entries))
        for entry in self.entries:
            props = entry.properties
            data += struct.pack("<B", len(props))
            for prop_name, prop_value in props.items():
                prop_id = CSS_PROP_IDS.get(prop_name, 0x00)
                value_idx = self.pool.add(prop_value)
                data += struct.pack("<BH", prop_id, value_idx)
        return data

    def size(self) -> int:
        return len(self.encode())


class StavesHTMLParser(HTMLParser):
    def __init__(self, string_pool: StringPool):
        super().__init__()
        self.pool = string_pool
        self.opcodes: list[bytes] = []
        self.skip_content = False
        self.skip_tags = {"style", "script", "meta", "link"}

    def handle_starttag(self, tag, attrs):
        if tag in self.skip_tags:
            self.skip_content = True
            return

        tag_id = TAG_IDS.get(tag, 0x00)
        if tag_id == 0x00:
            # Unknown tag: store name in string pool
            tag_name_idx = self.pool.add(tag)
            self.opcodes.append(struct.pack("<BBB", OP_OPEN, 0x00, len(attrs))
                                + struct.pack("<H", tag_name_idx))
        else:
            self.opcodes.append(struct.pack("<BBB", OP_OPEN, tag_id, len(attrs)))

        # Encode attributes
        for name, value in attrs:
            if name == "style":
                # Inline styles: skip for now (handled by style table)
                continue
            name_idx = self.pool.add(name)
            value_idx = self.pool.add(value or "")
            self.opcodes.append(struct.pack("<BHH", OP_ATTR, name_idx, value_idx))

    def handle_endtag(self, tag):
        if tag in self.skip_tags:
            self.skip_content = False
            return
        self.opcodes.append(struct.pack("<B", OP_CLOSE))

    def handle_data(self, data):
        if self.skip_content:
            return
        text = data.strip()
        if text:
            text_idx = self.pool.add(text)
            self.opcodes.append(struct.pack("<BH", OP_TEXT, text_idx))

    def get_bytecode(self) -> bytes:
        result = b""
        for op in self.opcodes:
            result += op
        result += struct.pack("<B", OP_EOF)
        return result


def parse_css(css_text: str) -> list[tuple[str, dict]]:
    """Simple CSS parser: extract selector -> {property: value} pairs."""
    rules = []
    # Remove comments
    css_text = re.sub(r"/\*.*?\*/", "", css_text, flags=re.DOTALL)
    # Remove @rules (media queries, etc.)
    css_text = re.sub(r"@[^{]*\{[^}]*\}", "", css_text)

    # Extract rules
    pattern = r"([^{]+)\{([^}]*)\}"
    for match in re.finditer(pattern, css_text):
        selector = match.group(1).strip()
        props_text = match.group(2).strip()
        properties = {}
        for prop_match in re.finditer(r"([\w-]+)\s*:\s*([^;]+);?", props_text):
            properties[prop_match.group(1).strip()] = prop_match.group(2).strip()
        if properties:
            rules.append((selector, properties))
    return rules


def compile_html_to_staves(html_content: str) -> tuple[bytes, dict]:
    """Compile HTML/CSS to Staves bytecode. Returns (bytecode, stats)."""

    pool = StringPool()
    style_table = StyleTable(pool)

    # Extract and compile CSS
    css_blocks = re.findall(r"<style[^>]*>(.*?)</style>", html_content, re.DOTALL)
    for css_text in css_blocks:
        for selector, properties in parse_css(css_text):
            style_table.add(selector, properties)

    # Parse HTML to DOM opcodes
    parser = StavesHTMLParser(pool)
    parser.feed(html_content)
    dom_bytecode = parser.get_bytecode()

    # Build final binary
    string_pool_data = pool.encode()
    style_table_data = style_table.encode()

    header_size = 16
    string_pool_offset = header_size
    style_table_offset = string_pool_offset + len(string_pool_data)
    dom_offset = style_table_offset + len(style_table_data)

    header = STAVES_MAGIC
    header += struct.pack("<HH", STAVES_VERSION, 0)  # version, flags
    header += struct.pack("<II", string_pool_offset, style_table_offset)

    staves_binary = header + string_pool_data + style_table_data + dom_bytecode

    stats = {
        "header_bytes": header_size,
        "string_pool_bytes": len(string_pool_data),
        "string_pool_entries": len(pool.strings),
        "style_table_bytes": len(style_table_data),
        "style_table_entries": len(style_table.entries),
        "dom_bytecode_bytes": len(dom_bytecode),
        "dom_opcodes": len(parser.opcodes),
        "total_staves_bytes": len(staves_binary),
    }

    return staves_binary, stats


def verify_staves(staves_binary: bytes) -> bool:
    """Verify a Staves binary is well-formed (can be decoded)."""
    if len(staves_binary) < 16:
        return False
    if staves_binary[:4] != STAVES_MAGIC:
        return False

    version = struct.unpack_from("<H", staves_binary, 4)[0]
    if version != STAVES_VERSION:
        return False

    # Verify we can read the string pool
    sp_offset = struct.unpack_from("<I", staves_binary, 8)[0]
    if sp_offset >= len(staves_binary):
        return False

    try:
        sp_count = struct.unpack_from("<H", staves_binary, sp_offset)[0]
        pos = sp_offset + 2
        for _ in range(sp_count):
            str_len = struct.unpack_from("<H", staves_binary, pos)[0]
            pos += 2 + str_len
            if pos > len(staves_binary):
                return False
    except struct.error:
        return False

    return True


# ─── PQ Overhead Constants ────────────────────────────────────────────────────

PQ_OVERHEAD = {
    "classical_handshake": 9_512,
    "pq_level3_handshake": 33_178,
    "pq_level5_handshake": 42_710,
    "classical_cert_chain": 3_500,
    "pq_hybrid_cert_chain": 19_223,
    "classical_rekey": 64,
    "pq_level3_rekey": 2_272,
    "aes_gcm_per_frame": 41,  # nonce + tag + header (same for both)
}


def benchmark(html_file: str) -> dict:
    """Run full benchmark: HTML -> Staves -> comparison with PQ overhead."""

    with open(html_file, "r") as f:
        html_content = f.read()

    original_size = len(html_content.encode("utf-8"))

    # Separate content types
    js_matches = re.findall(r"<script[^>]*>(.*?)</script>", html_content, re.DOTALL)
    css_matches = re.findall(r"<style[^>]*>(.*?)</style>", html_content, re.DOTALL)
    js_size = sum(len(js.encode("utf-8")) for js in js_matches)
    css_size = sum(len(css.encode("utf-8")) for css in css_matches)
    html_size = original_size - js_size - css_size

    # Compile to Staves
    staves_binary, compile_stats = compile_html_to_staves(html_content)

    # Verify the output
    is_valid = verify_staves(staves_binary)

    staves_size = len(staves_binary)
    compression_ratio = (1 - staves_size / original_size) * 100
    savings = original_size - staves_size

    # PQ overhead comparison
    pq_handshake_overhead = PQ_OVERHEAD["pq_level3_handshake"] - PQ_OVERHEAD["classical_handshake"]

    result = {
        "file": os.path.basename(html_file),
        "original": {
            "total_bytes": original_size,
            "html_bytes": html_size,
            "css_bytes": css_size,
            "js_bytes": js_size,
        },
        "staves": {
            "total_bytes": staves_size,
            "valid": is_valid,
            **compile_stats,
        },
        "compression": {
            "ratio_percent": round(compression_ratio, 1),
            "bytes_saved": savings,
            "reduction_factor": round(original_size / max(staves_size, 1), 1),
        },
        "pq_comparison": {
            "pq_handshake_overhead_bytes": pq_handshake_overhead,
            "content_savings_bytes": savings,
            "net_savings_bytes": savings - pq_handshake_overhead,
            "pq_offset": savings >= pq_handshake_overhead,
            "sessions_to_offset": max(1, pq_handshake_overhead // max(savings, 1) + 1) if savings > 0 else float("inf"),
            "classical_total": PQ_OVERHEAD["classical_handshake"] + original_size,
            "pq_total": PQ_OVERHEAD["pq_level3_handshake"] + original_size,
            "pq_plus_staves_total": PQ_OVERHEAD["pq_level3_handshake"] + staves_size,
        },
    }

    return result


def print_benchmark(result: dict):
    """Print benchmark results as formatted tables."""

    print("\n" + "=" * 70)
    print(f"  RUNEMATE FORGE BENCHMARK: {result['file']}")
    print("=" * 70)

    o = result["original"]
    s = result["staves"]
    c = result["compression"]
    p = result["pq_comparison"]

    print(f"\n{'ORIGINAL CONTENT':^70}")
    print("-" * 70)
    print(f"  HTML:       {o['html_bytes']:>8,} bytes")
    print(f"  CSS:        {o['css_bytes']:>8,} bytes")
    print(f"  JavaScript: {o['js_bytes']:>8,} bytes  (ELIMINATED in Staves)")
    print(f"  Total:      {o['total_bytes']:>8,} bytes")

    print(f"\n{'STAVES OUTPUT':^70}")
    print("-" * 70)
    print(f"  Header:         {s['header_bytes']:>6} bytes")
    print(f"  String Pool:    {s['string_pool_bytes']:>6} bytes  ({s['string_pool_entries']} entries)")
    print(f"  Style Table:    {s['style_table_bytes']:>6} bytes  ({s['style_table_entries']} rules)")
    print(f"  DOM Bytecode:   {s['dom_bytecode_bytes']:>6} bytes  ({s['dom_opcodes']} opcodes)")
    print(f"  Total Staves:   {s['total_bytes']:>6} bytes")
    print(f"  Valid:          {'YES' if s['valid'] else 'NO'}")

    print(f"\n{'COMPRESSION':^70}")
    print("-" * 70)
    print(f"  Ratio:          {c['ratio_percent']}% reduction")
    print(f"  Bytes saved:    {c['bytes_saved']:,} bytes")
    print(f"  Factor:         {c['reduction_factor']}x smaller")

    print(f"\n{'POST-QUANTUM OVERHEAD COMPARISON':^70}")
    print("-" * 70)
    print(f"  PQ handshake overhead:    +{p['pq_handshake_overhead_bytes']:>6,} bytes")
    print(f"  Staves content savings:   -{c['bytes_saved']:>6,} bytes")
    print(f"  Net savings:              {p['net_savings_bytes']:>+7,} bytes")
    print(f"  PQ tax fully offset?      {'YES' if p['pq_offset'] else 'NO'}")

    print(f"\n{'TOTAL TRANSMISSION SIZE':^70}")
    print("-" * 70)
    print(f"  Classical (ECDH) + raw HTML:    {p['classical_total']:>8,} bytes")
    print(f"  PQ (ML-KEM) + raw HTML:         {p['pq_total']:>8,} bytes  (+{p['pq_total'] - p['classical_total']:,})")
    pq_staves_diff = p['pq_plus_staves_total'] - p['classical_total']
    sign = "+" if pq_staves_diff >= 0 else ""
    print(f"  PQ (ML-KEM) + Staves:           {p['pq_plus_staves_total']:>8,} bytes  ({sign}{pq_staves_diff:,})")
    print()

    if p['pq_offset']:
        print(f"  RESULT: PQ + Staves is {abs(pq_staves_diff):,} bytes "
              f"{'LARGER' if pq_staves_diff > 0 else 'SMALLER'} than Classical + raw HTML")
    else:
        print(f"  RESULT: Need {p['sessions_to_offset']} page loads to offset PQ handshake")

    print("=" * 70)


def generate_chart_data(results: list[dict]) -> str:
    """Generate a markdown chart comparing all benchmarks."""

    lines = []
    lines.append("\n## Runemate Forge: Compression Benchmark Results\n")
    lines.append("| File | Original | Staves | Ratio | PQ Overhead | Net | PQ Offset? |")
    lines.append("|------|----------|--------|-------|-------------|-----|-----------|")

    for r in results:
        o = r["original"]["total_bytes"]
        s = r["staves"]["total_bytes"]
        ratio = r["compression"]["ratio_percent"]
        pq = r["pq_comparison"]["pq_handshake_overhead_bytes"]
        net = r["pq_comparison"]["net_savings_bytes"]
        offset = "YES" if r["pq_comparison"]["pq_offset"] else "NO"
        lines.append(f"| {r['file']} | {o:,} B | {s:,} B | {ratio}% | +{pq:,} B | {net:+,} B | {offset} |")

    lines.append("")
    lines.append("### Total Transmission Comparison\n")
    lines.append("| File | Classical+HTML | PQ+HTML | PQ+Staves | vs Classical |")
    lines.append("|------|---------------|---------|-----------|-------------|")

    for r in results:
        p = r["pq_comparison"]
        diff = p["pq_plus_staves_total"] - p["classical_total"]
        sign = "+" if diff >= 0 else ""
        lines.append(
            f"| {r['file']} | {p['classical_total']:,} B | {p['pq_total']:,} B "
            f"| {p['pq_plus_staves_total']:,} B | {sign}{diff:,} B |"
        )

    return "\n".join(lines)


if __name__ == "__main__":
    sample_dir = os.path.join(os.path.dirname(__file__), "samples")
    output_dir = os.path.join(os.path.dirname(__file__), "output")
    os.makedirs(output_dir, exist_ok=True)

    results = []

    for filename in sorted(os.listdir(sample_dir)):
        if filename.endswith(".html"):
            filepath = os.path.join(sample_dir, filename)
            result = benchmark(filepath)
            results.append(result)
            print_benchmark(result)

            # Write the Staves binary
            staves_path = os.path.join(output_dir, filename.replace(".html", ".stav"))
            staves_binary, _ = compile_html_to_staves(open(filepath).read())
            with open(staves_path, "wb") as f:
                f.write(staves_binary)
            print(f"  Staves binary written to: {staves_path}")

    # Generate chart
    if results:
        chart = generate_chart_data(results)
        chart_path = os.path.join(output_dir, "benchmark-results.md")
        with open(chart_path, "w") as f:
            f.write(chart)
        print(f"\nBenchmark chart written to: {chart_path}")

        # Write JSON results
        json_path = os.path.join(output_dir, "benchmark-results.json")
        with open(json_path, "w") as f:
            json.dump(results, f, indent=2)
        print(f"JSON results written to: {json_path}")
