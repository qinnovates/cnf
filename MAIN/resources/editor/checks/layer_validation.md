# Layer Validation Rules

> Sub-instruction file for Editor Agent — validates 14-layer model accuracy

---

## Authoritative Definition

**Source:** `MAIN/publications/0-oni-framework/TechDoc-ONI_Framework.md`

### The 14 ONI Layers (Canonical)

| Layer | Name | Domain | Description |
|:-----:|------|--------|-------------|
| L1 | Physical Carrier | Silicon | Conveys raw data through electromagnetic means |
| L2 | Link Framing | Silicon | Handles error detection and synchronization |
| L3 | Network Routing | Silicon | Manages addressing and packet pathfinding |
| L4 | Transport Flow | Silicon | Ensures dependable delivery with flow management |
| L5 | Session State | Silicon | Oversees connection lifecycle |
| L6 | Data Encoding | Silicon | Translates formats, encryption, compression |
| L7 | Application Interface | Silicon | Provides user-accessible services and APIs |
| L8 | Neural Gateway | Bridge | Physical boundary between digital and biological |
| L9 | Ion Channel Encoding | Biology | Spike generation and neurotransmitter activity |
| L10 | Oscillatory Synchronization | Biology | Temporal alignment via frequency rhythms |
| L11 | Cognitive Session | Biology | Working memory and attentional focus |
| L12 | Semantic Assembly | Biology | Meaning and concept formation |
| L13 | Intent & Agency | Biology | Goal formation and decision-making |
| L14 | Identity & Ethics | Biology | Self-concept and moral reasoning |

---

## Validation Checks

### Check 1: Layer Name Accuracy

**Detection:** Search for tables containing "Layer" and layer numbers (L1-L14)

**Patterns to find:**
```
grep -E "L[0-9]{1,2}.*\|"
grep -E "\| L[0-9]"
grep -E "Layer.*[0-9]"
```

**Validation:** Each layer number must have the correct name:
- L1 = "Physical Carrier" (NOT "Molecular")
- L2 = "Link Framing" (NOT "Cellular")
- L8 = "Neural Gateway" (always correct, bridge layer)
- L9 = "Ion Channel Encoding" (NOT "Signal Processing")
- etc.

### Check 2: Domain Accuracy

**Silicon Layers:** L1-L7
**Bridge Layer:** L8
**Biology Layers:** L9-L14

**Common Error:** Domains inverted (Biology for L1-L7, Silicon for L9-L14)

### Check 3: Layer Count

**Must always be exactly 14 layers**

If document mentions "7-layer" or "OSI extension" — verify it explains the full 14.

---

## Files to Validate

These files contain layer references:

| File | Contains | Priority |
|------|----------|----------|
| `publications/0-oni-framework/README.md` | Full 14-layer table | CRITICAL |
| `publications/0-oni-framework/Blog-ONI_Framework.md` | Layer descriptions | HIGH |
| `MAIN/INDEX.md` | Layer references | HIGH |
| `oni-framework/oni/layers.py` | Code implementation | CRITICAL |
| Root `README.md` | May contain summary | MEDIUM |

---

## Common Errors

### Error Type 1: Inverted Model
**Wrong:**
```
L1: Molecular (Biology)
L7: Behavioral (Biology)
L9: Signal Processing (Silicon)
L14: Application (Silicon)
```

**Correct:**
```
L1: Physical Carrier (Silicon)
L7: Application Interface (Silicon)
L9: Ion Channel Encoding (Biology)
L14: Identity & Ethics (Biology)
```

### Error Type 2: OSI Names Used
**Wrong:** Using pure OSI names for L1-L7
```
L1: Physical
L2: Data Link
L3: Network
```

**Correct:** Using ONI-specific names
```
L1: Physical Carrier
L2: Link Framing
L3: Network Routing
```

### Error Type 3: Missing Layers
**Wrong:** Only showing 7 layers or skipping L8

**Correct:** All 14 layers, L8 (Neural Gateway) explicitly shown as bridge

---

## Action Protocol

**If mismatch found:**

1. **STOP** — Do not auto-fix layer content
2. **REPORT** — Show exact mismatch with line numbers
3. **PROPOSE** — Show correct values from authoritative source
4. **WAIT** — Require explicit user approval
5. **FIX** — Apply correction only after approval
6. **VERIFY** — Re-check after fix applied

---

## Verification Command

After fixing, verify all layer tables match:

```bash
# Find all layer tables
grep -rn "14 Layers\|L1.*L14\|Layer.*Silicon\|Layer.*Biology" MAIN/

# Compare against authoritative source
diff <(grep "L[0-9]" TechDoc-ONI_Framework.md) <(grep "L[0-9]" README.md)
```

---

*Layer Validation v1.0*
