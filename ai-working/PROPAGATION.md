# QIF Truth Propagation Protocol

> **One rule:** Truth flows downward. Never upward. Never sideways.
>
> ```
> QIF-TRUTH.md  -->  oni/ repo docs  -->  qinnovates.github.io/blogs/
>   (canonical)       (implementation)       (public-facing)
> ```

---

## A. Propagation Map

Use this table to look up which files need updating when a QIF-TRUTH.md section changes.

| QIF-TRUTH Section | Repo Files (oni/) | Blog Files (qinnovates.github.io/blogs/) |
|---|---|---|
| **S1: Framework Identity** | `neurosecurity/qif/README.md`, `README.md`, `brand.json` | OSI of Mind |
| **S2: Layer Architecture** | `ONI_LAYERS.md`, all TechDocs with layer tables, `layers.py` | All 7 QIF blogs |
| **S3.1: Coherence Metric** | `TechDoc-Coherence_Metric.md`, `coherence.py`, whitepaper | Spam Filter (Coherence) |
| **S3.2: Scale-Frequency** | `TechDoc-Scale_Frequency.md`, whitepaper | Hidden Equation (f x S) |
| **S3.3: Established Physics** | Whitepaper equation chain table | (none directly) |
| **S3.4: Quantum Equations** | `TechDoc-Quantum_Encryption.md`, whitepaper | Quantum Hackers, Nobel Prize, Liminal Phase |
| **S4: Candidate QI Equations** | Whitepaper (when published) | (none yet) |
| **S5: Validated External Claims** | All TechDocs referencing these numbers | Heart Attack, Quantum Hackers |
| **S6: Sync Dashboard** | (self-tracking) | (self-tracking) |

### Key Repo File Locations

| File | Path |
|------|------|
| brand.json | `neurosecurity/legacy-core/resources/brand/brand.json` |
| ONI_LAYERS.md | `neurosecurity/legacy-core/oni-framework/ONI_LAYERS.md` |
| layers.py | `neurosecurity/legacy-core/oni-framework/oni/layers.py` |
| coherence.py | `neurosecurity/legacy-core/oni-framework/oni/coherence.py` |
| TechDocs | `neurosecurity/legacy-core/publications/[topic]/TechDoc-*.md` |
| Whitepaper | `docs/whitepaper/` |
| QIF README | `neurosecurity/qif/README.md` |

---

## B. Change Protocol

**When you change QIF-TRUTH.md, follow these 10 steps in order:**

- [ ] 1. Make the change in **QIF-TRUTH.md**
- [ ] 2. Update the **"Last validated"** date in QIF-TRUTH.md header
- [ ] 3. Look up affected **repo files** in the Propagation Map (Section A)
- [ ] 4. Update each affected repo file
- [ ] 5. Run **Editor Agent** to catch cascades within the repo
- [ ] 6. Look up affected **blog files** in the Propagation Map
- [ ] 7. Update each affected blog file
- [ ] 8. Update **Section 6 Sync Dashboard** in QIF-TRUTH.md
- [ ] 9. Commit **oni/** repo changes
- [ ] 10. Commit **qinnovates.github.io** changes

**Do not skip steps. Do not reorder.**

---

## C. Backwards Flow Prevention

```
IF you find an error in a blog or repo doc:

  1. Check QIF-TRUTH.md — is the truth doc also wrong?

     YES → Fix QIF-TRUTH.md FIRST, then propagate down (Section B)
     NO  → The blog/repo diverged. Update it to match QIF-TRUTH.md.

  2. NEVER update QIF-TRUTH.md based on a blog post.

  QIF-TRUTH.md is updated based on:
  - Primary sources (peer-reviewed papers, textbooks)
  - Physics / mathematics / neuroscience evidence
  - Strategic decisions by Kevin Qi
  - Novel QIF contributions (labeled as hypothesis)
```

---

## D. Weekly Audit (Every Sunday, 15 min max)

- [ ] 1. Open QIF-TRUTH.md — check **"Next audit due"** date
- [ ] 2. Scan **Section 6 Sync Dashboard** — any `REVIEW` or `NEEDS_SYNC`?
- [ ] 3. Has any repo TechDoc been edited since last audit? If yes → verify it matches truth
- [ ] 4. Has any blog been edited since last audit? If yes → verify it matches truth
- [ ] 5. Update **"Last audit"** date in QIF-TRUTH.md
- [ ] 6. Set **"Next audit due"** to next Sunday
- [ ] 7. If clean, confirm all Section 6 entries with today's date

**If discrepancies found:** Follow Section B (Change Protocol) to fix them. Truth wins.

---

*Created: 2026-02-02*
*Lives next to: QIF-TRUTH.md*
*Maintainer: Quantum Intelligence (Kevin Qi + Claude)*
