# Transparency Statement: Human-AI Collaboration in ONI Framework

> This document serves as an auditable record of how AI tools were integrated into the development of the ONI Framework, demonstrating principles of Responsible AI, cognitive boundary maintenance, and Human-in-the-Loop (HITL) methodology.

**Last Updated:** 2026-01-26
**Document Version:** 1.1

---

## Purpose

The ONI Framework addresses security for brain-computer interfaces—technology that will fundamentally alter the human-machine boundary. It is therefore essential that the *development process itself* models the transparency and cognitive autonomy principles the framework seeks to protect.

This document:
1. Defines the cognitive boundary between human and AI contributions
2. Documents the Human-in-the-Loop refinement process
3. Provides an auditable trail for academic and professional review
4. Serves as a case study in Responsible AI methodology

---

## Methodology: The Cognitive Division

### Core Principle

Every contribution is categorized by its cognitive origin. AI assistance is treated as a tool subject to human oversight, not a collaborator with independent judgment on ethical or novel technical matters.

### Contribution Matrix

| Domain | Human Contribution | AI Contribution | Boundary Notes |
|--------|-------------------|-----------------|----------------|
| **Conceptual Architecture** | Original 14-layer ONI model design, attack surface identification, layer-to-ethics mapping | None | Purely human ideation; AI was not consulted on framework structure |
| **Mathematical Formulas** | Cₛ coherence metric conception, variable selection (σ²φ, σ²τ, σ²γ), security interpretations | LaTeX formatting, notation consistency | Human selected which variances matter for security; AI formatted |
| **Security Decisions** | Zero-trust architecture choice, firewall placement at L8, rejection thresholds | None | All security-critical decisions made by human judgment |
| **Quantum Security Concepts** | TTT as security primitive, QPUF authentication proposal, liminal phase hypothesis | Literature organization | Novel security applications are human contributions |
| **Code Implementation** | Algorithm design, API decisions, security-critical logic | Syntax generation, boilerplate, docstrings | Human reviewed all generated code for security implications |
| **Research Synthesis** | Source selection, relevance judgment, argument construction, conclusions | Initial literature summaries | All AI summaries verified against primary sources |
| **Technical Writing** | All original analysis, ethical arguments, novel hypotheses | Structural suggestions, grammar, APA formatting | Human wrote arguments; AI assisted with presentation |
| **Blog Posts** | Core narratives, analogies, original insights | Draft structuring, SEO optimization | Human voice and perspective preserved throughout |

---

## The Refinement Loop: Human-in-the-Loop Evidence

### Documented Corrections

The following examples demonstrate active human oversight correcting AI output:

#### Example 1: Quantum Coherence Timescales
- **AI Initial Output**: Suggested biological quantum coherence persists for ~10 milliseconds
- **Human Correction**: Rejected; actual biological coherence timescales are ~100 femtoseconds (Engel et al., 2007)
- **Action Taken**: Corrected in TechDoc-Quantum_Encryption.md with proper citation
- **Lesson**: AI hallucinated a plausible-sounding but incorrect value by three orders of magnitude

#### Example 2: Encryption Architecture
- **AI Initial Output**: Suggested symmetric encryption for neural signal authentication
- **Human Override**: Rejected due to key distribution vulnerability in implanted devices
- **Action Taken**: Pivoted to QPUF-based authentication as documented in quantum-encryption publications
- **Ethical Reasoning**: Key distribution in BCIs creates attack surface for "harvest now, decrypt later" scenarios affecting long-term cognitive autonomy

#### Example 3: Transport Variance Defaults
- **AI Initial Output**: Suggested using uniform reliability factors (all 0.95)
- **Human Override**: Rejected; biological pathways have heterogeneous reliability
- **Action Taken**: Researched actual synaptic transmission reliability (~0.85), myelination effects, etc.
- **Lesson**: AI defaulted to simplified assumptions that would reduce biological validity

**Expanded Analysis — Why Synaptic Reliability Dominates:**

The Coherence Metric (Cₛ) combines three variance components: phase (σ²φ), transport (σ²τ), and gain (σ²γ). Understanding *why* transport variance dominates required multiple iterations:

1. **Biological Reality of Synaptic Transmission**: Synaptic vesicle release is inherently probabilistic — approximately 85% reliable per synapse (Branco & Bhalla, 2006; Del Castillo & Katz, 1954). This isn't a defect; it's a feature enabling neural plasticity and energy efficiency.

2. **Compounding Effect Across Pathways**: Neural signals traverse multi-synaptic pathways. For a 3-synapse pathway: 0.85³ ≈ 0.61 reliability. For 5 synapses: 0.85⁵ ≈ 0.44. This exponential degradation means transport variance accumulates faster than phase or gain variance.

3. **Why This Matters for Security**: An attacker cannot easily *improve* transport reliability — it's biologically constrained. However, they can *exploit* it by injecting signals that appear to have unnaturally high reliability (>0.95), which should trigger anomaly detection. Signals with *too perfect* transmission are as suspicious as degraded ones.

4. **The Learning Moment**: AI's suggestion of uniform 0.95 reliability would have:

   - **Overestimated baseline signal quality**: A 0.95 reliability assumption is 10 percentage points higher than biological reality (~0.85). This might seem like a small difference, but compounded across pathways it dramatically shifts expectations. At 0.95³ = 0.86 reliability for 3 synapses vs. 0.85³ = 0.61 — the AI's assumption would predict 40% higher pathway reliability than actually exists. Any coherence threshold calibrated on these inflated baselines would be fundamentally miscalibrated.

   - **Missed a key attack detection vector (supranormal reliability)**: "Supranormal" means *above the normal biological range*. If real synapses transmit at ~85% reliability, a signal showing 95%+ reliability is biologically implausible — it's *too clean*. This is a critical security insight: attackers injecting synthetic signals into a BCI cannot easily replicate the natural "messiness" of biological transmission. Their signals will be suspiciously reliable. By using 0.95 as our baseline, we would have normalized this attack signature, making it invisible to detection. The 0.95 threshold matters specifically because it sits at the boundary of biological plausibility — signals above this should trigger immediate scrutiny.

   - **Ignored decades of neuroscience research on synaptic stochasticity**: The probabilistic nature of synaptic transmission has been documented since Katz's Nobel Prize-winning work in the 1950s-70s (Del Castillo & Katz, 1954). This isn't obscure knowledge — it's foundational neuroscience. The AI's "clean" assumption of 0.95 revealed a pattern: AI systems optimize for mathematical elegance (uniform, high values) rather than biological fidelity (heterogeneous, lower values). This is precisely the kind of domain-specific knowledge that requires human oversight.

   **Why 0.95 Specifically?** The AI likely selected 0.95 because it's a common "high confidence" placeholder in engineering contexts (like 95% confidence intervals). But this reveals a category error: applying statistical conventions to biological systems. Real synapses don't care about human statistical preferences — they evolved under constraints of energy efficiency, plasticity, and noise tolerance that produce ~85% reliability as an *optimal* tradeoff, not a limitation.

This example illustrates why domain expertise cannot be fully offloaded to AI — the AI optimized for "clean" assumptions while biological systems operate on "messy" realities that carry security-relevant information. The mess *is* the signal.

#### Example 4: Firewall Decision Matrix
- **AI Initial Output**: Suggested binary accept/reject based solely on coherence score
- **Human Enhancement**: Added authentication requirement and ACCEPT_FLAG intermediate state
- **Reasoning**: Zero-trust principles require identity verification independent of signal quality
- **Action Taken**: Implemented full decision matrix with alert levels

#### Example 5: Coherence Formula Notation Correction (2026-01-26)
- **Legacy Notation**: `Cₛ = Σᵢ wᵢ × Φᵢ(Δtᵢ) × Θᵢ(fᵢ, Aᵢ)` (weighted sum representation)
- **Authoritative Formula**: `Cₛ = e^(−(σ²φ + σ²τ + σ²γ))` (exponential decay)
- **Discovery Process**: Systematic repository audit found 8 files containing the legacy notation that contradicted the authoritative TechDoc and code implementation
- **Mathematical Proof**:
  1. The exponential form models biological threshold behaviors (Markram et al., 1997 — STDP windows)
  2. Formula is derived from Shannon entropy: Cₛ = e^(−H_total) where H_total = total variance
  3. Produces bounded output [0, 1] with proper asymptotic behavior (Cₛ → 1 as variance → 0)
  4. All 14 unit tests in `test_coherence.py` explicitly verify e^−x behavior
  5. Both `oni-framework` and `tara_mvp` implementations use `math.exp(-total_variance)`
- **Files Corrected**: CLAUDE.md, AGENTS.md, TARA/API.md, TARA/CLAUDE.md, PERSONAS.md, app.py, CoherenceGauge.tsx, coherence.tsx
- **Lesson**: Legacy notation from early development propagated to auxiliary documentation without review against authoritative sources. This underscores the importance of establishing clear truth hierarchies (TechDoc > Implementation > Supporting docs).

### Correction Rate

Across the development of ONI Framework v0.1.0:
- **Total AI suggestions reviewed**: ~200+
- **Accepted without modification**: ~60%
- **Accepted with modification**: ~25%
- **Rejected entirely**: ~15%

The 40% modification/rejection rate demonstrates active critical engagement, not passive acceptance.

---

## Verification Protocol

### Scientific Claims
- All neuroscience claims verified against peer-reviewed sources
- Quantum physics claims cross-referenced with recent experimental literature
- Biological assumptions explicitly flagged for expert review (see ../CONTRIBUTING.md)

### Code Quality
- 77 unit tests covering all core modules
- No AI-generated tests accepted without manual review and modification
- Security-critical code paths manually audited

### Documentation
- All "facts" in technical documents traced to citations
- Speculative content clearly marked as hypotheses
- Research status disclaimer prominent in README and package documentation

---

## Cognitive Boundary Maintenance

### The Challenge

Using AI for efficiency creates a risk: cognitive offloading may trade deep understanding for breadth. This tension is directly relevant to neuroethics, where we ask similar questions about neural augmentation.

### Self-Assessment

**Where AI Helped Understanding:**
- Rapid literature survey revealed connections I might have missed
- Forcing clear documentation improved my own conceptual clarity
- Debugging conversations exposed gaps in my reasoning

**Where AI Hindered Understanding:**
- Initial over-reliance on AI-structured outlines delayed developing my own organizational logic
- Transport variance defaults required multiple iterations before I fully internalized *why* synaptic transmission reliability (0.85) dominates the coherence penalty (see Example 3 in Refinement Loop for detailed analysis). The AI's "clean" assumptions obscured the biological insight that stochastic synaptic release is both a constraint *and* a security feature — understanding this required returning to primary neuroscience literature and reasoning through the exponential compounding effect myself.
- Some nuances only became clear when I had to explain AI errors

**Mitigation Strategy:**
- Mandatory "explain it without AI" check for core concepts
- Periodic manual writing sessions to maintain voice and reasoning skills
- Deliberate engagement with primary sources, not just AI summaries

---

## Tool Disclosure

### AI Tools Used

| Tool | Version/Model | Use Case | Contribution Level |
|------|---------------|----------|-------------------|
| Claude (Anthropic) | Claude Opus 4.5 | Code assistance, documentation drafting, research synthesis | Primary |
| Claude Code | CLI | Repository management, file operations, git workflows | Primary |
| Gemini (Google) | Gemini 1.5/2.0 | Research verification, cross-model validation, alternative perspectives | Secondary |
| ChatGPT (OpenAI) | GPT-4 | Research queries, concept exploration, literature discovery | Secondary |
| LMArena (LMSYS) | Blind comparison | Unbiased initial concept exploration, cross-model validation | Exploratory |

**Note on Multi-Model Approach**: Using multiple AI models serves as a form of epistemic hygiene — cross-referencing outputs between Claude, Gemini, ChatGPT, and blind comparisons via LMArena helps identify model-specific biases or hallucinations. When models disagree, human judgment adjudicates by consulting primary sources.

### Non-AI Tools
- Python 3.9+ for implementation
- pytest for testing
- GitHub Actions for CI/CD
- Standard scientific Python stack (no AI libraries in core package)

---

## Commit Convention

All commits involving AI assistance include:

```
Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
```

This provides a historical audit trail of all changes requested by the HITL (human-in-the-layer). Commits without this tag represent manual changes made within the Github UI.

### Enhanced Commit Format (Adopted January 2026)

For significant contributions, commits may include cognitive boundary metadata:

```
[Domain] Brief description

Original conception: Human/AI/Joint
Implementation: Human/AI-assisted
Verification: Human (method)

- Detailed changes
- Human decisions noted
- AI suggestions accepted/rejected noted

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
```

---

## Alignment with Responsible AI Principles

### Transparency
- This document exists
- AI contributions explicitly marked
- Refinement loop documented with specific examples

### Accountability
- Human author (Kevin L. Qi) takes full responsibility for all published content
- AI is a tool, not a co-author with independent standing
- Errors in final output are human responsibility regardless of origin

### Human Oversight
- All AI output subject to human review before publication
- Security-critical decisions made by human judgment
- Rejection/modification rate demonstrates active oversight

### Explainability
- The ONI Framework itself embodies XAI principles (every firewall decision has traceable reasoning)
- This document explains *how* AI was used, not just *that* it was used

---

## For Academic Review

This transparency statement is provided for:
- Graduate program admissions review
- Academic integrity assessment
- Responsible AI methodology evaluation

### Key Takeaways for Reviewers

1. **Cognitive Autonomy Maintained**: Original ideas, security architecture, and ethical reasoning are human contributions
2. **Critical Engagement Demonstrated**: 40% of AI suggestions modified or rejected
3. **Verification Performed**: All claims traced to sources; code tested
4. **Meta-Awareness Present**: The author analyzed their own human-AI cognitive boundary as a neuroethics exercise

---

## Website Security Controls (GitHub Pages)

> **Added:** 2026-01-26 | **Location:** `docs/index.html`

The ONI Framework website dynamically loads brand content (mission, slogan, vision, stats) from `brand.json` via GitHub's raw content API. This creates a potential attack vector if the repository is compromised. The following security controls mitigate these risks:

### Content Security Policy (CSP)

```html
<meta http-equiv="Content-Security-Policy" content="
  default-src 'self';
  script-src 'self' 'unsafe-inline' https://unpkg.com;
  style-src 'self' 'unsafe-inline' https://unpkg.com;
  img-src 'self' https: data:;
  connect-src 'self' https://raw.githubusercontent.com https://api.github.com;
  font-src 'self';
">
```

**Effect:** Restricts where scripts, styles, and data can be loaded from. Blocks execution of scripts from unauthorized sources.

### Subresource Integrity (SRI)

External dependencies (AOS animation library) include cryptographic hashes:

```html
<link href="https://unpkg.com/aos@2.3.4/dist/aos.css"
      integrity="sha384-/rJKQnzXffaXJfyu1v+..." crossorigin="anonymous">
<script src="https://unpkg.com/aos@2.3.4/dist/aos.js"
        integrity="sha384-oZixfuJpr9a/P06Xslt0X..." crossorigin="anonymous">
```

**Effect:** Browser refuses to load the resource if the hash doesn't match, preventing supply chain attacks via compromised CDN.

### Input Validation for brand.json

All values from `brand.json` pass through validation before DOM insertion:

| Function | Validation | Rejection Criteria |
|----------|------------|-------------------|
| `sanitizeText(input, maxLength)` | Type check, length limit, pattern check | Non-string, >maxLength chars, contains HTML tags, control characters |
| `sanitizeNumber(input, min, max)` | Type check, range validation | Non-number, outside min/max range |

**Implementation:**
```javascript
function sanitizeText(input, maxLength = 500) {
    if (typeof input !== 'string') return null;
    if (input.length > maxLength) return null;
    if (/<[^>]*>/.test(input)) return null;  // Reject HTML tags
    return input.replace(/[\x00-\x1F\x7F]/g, '');  // Strip control chars
}
```

### Safe DOM Assignment

All dynamic content uses `.textContent` (never `.innerHTML`):

```javascript
missionEl.textContent = safeMission;  // Safe - treats content as text
// NOT: missionEl.innerHTML = safeMission;  // Unsafe - would parse HTML
```

**Effect:** Even if malicious content bypasses validation, it renders as literal text, not executable code.

### Attack Vectors Mitigated

| Attack Vector | Mitigation | Status |
|---------------|------------|--------|
| XSS via brand.json | Input validation + textContent | ✅ Blocked |
| Supply chain (CDN compromise) | SRI hashes | ✅ Blocked |
| Script injection (external) | CSP whitelist | ✅ Blocked |
| DoS via oversized input | Max length validation | ✅ Blocked |
| Malformed JSON | Structure validation | ✅ Blocked |

### Remaining Considerations

1. **Repository compromise**: If an attacker gains write access to the repo, they could modify the JavaScript itself. Mitigation: Branch protection, required reviews, audit logging.
2. **GitHub raw content availability**: If GitHub is unavailable, fallback to hardcoded defaults preserves functionality.

---

## Document Maintenance

This document is updated whenever:
- New publications are added to the repository
- Significant AI-assisted development occurs
- Methodology changes

Update log maintained in git history.

---

## Contact

For questions about this transparency statement or the human-AI collaboration methodology:

**Author**: Kevin L. Qi
**Repository**: https://github.com/qinnovates/qinnovate

---

*This transparency statement itself was drafted with AI assistance for structure and formatting. The content, examples, and methodological decisions are human contributions.*

---

← Back to [INDEX.md](../INDEX.md) | [NEUROETHICS_ALIGNMENT.md](NEUROETHICS_ALIGNMENT.md) | [REGULATORY_COMPLIANCE.md](REGULATORY_COMPLIANCE.md)
