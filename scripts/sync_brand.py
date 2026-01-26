#!/usr/bin/env python3
"""
Sync brand.json values into README.md and other documentation.

Usage:
    python scripts/sync_brand.py

This script updates documentation files to match brand.json,
ensuring consistency across the repository.
"""

import json
import re
from pathlib import Path


def load_brand() -> dict:
    """Load brand.json from repo root."""
    brand_path = Path(__file__).parent.parent / "brand.json"
    with open(brand_path) as f:
        return json.load(f)


def update_readme(brand: dict) -> bool:
    """Update README.md with brand values."""
    readme_path = Path(__file__).parent.parent / "README.md"
    content = readme_path.read_text()
    original = content

    oni = brand["oni"]

    # Update ONI full name in parentheses
    # Pattern: **ONI** (Something) —
    content = re.sub(
        r'\*\*ONI\*\* \([^)]+\) —',
        f'**ONI** ({oni["full_name"]}) —',
        content
    )

    # Update tagline if present
    # Pattern: *The OSI of Mind* or similar italicized tagline
    if oni.get("tagline"):
        content = re.sub(
            r'^\*The [^*]+\*$',
            f'*{oni["tagline"]}*',
            content,
            flags=re.MULTILINE
        )

    if content != original:
        readme_path.write_text(content)
        return True
    return False


def update_github_pages(brand: dict) -> bool:
    """Update docs/index.html with brand values."""
    html_path = Path(__file__).parent.parent / "docs" / "index.html"
    if not html_path.exists():
        return False

    content = html_path.read_text()
    original = content

    oni = brand["oni"]

    # Update mission text in the fallback/default value
    # Pattern: <p id="mission-text" ...>old mission text</p>
    if oni.get("mission"):
        content = re.sub(
            r'(<p id="mission-text"[^>]*>)[^<]*(</p>)',
            rf'\1{oni["mission"]}\2',
            content
        )

    if content != original:
        html_path.write_text(content)
        return True
    return False


def main():
    print("Loading brand.json...")
    brand = load_brand()

    print(f"ONI: {brand['oni']['full_name']}")
    print(f"TARA: {brand['tara']['full_name']}")
    print(f"Mission: {brand['oni']['mission'][:50]}...")
    print()

    print("Updating README.md...")
    if update_readme(brand):
        print("  README.md updated")
    else:
        print("  README.md already in sync")

    print("Updating docs/index.html...")
    if update_github_pages(brand):
        print("  docs/index.html updated")
    else:
        print("  docs/index.html already in sync")

    print("\nDone!")


if __name__ == "__main__":
    main()
