# Transparency Statement: Human-AI Collaboration in ONI Framework

> This document serves as an auditable record of how AI tools were integrated into the development of the ONI Framework, demonstrating principles of Responsible AI, cognitive boundary maintenance, and Human-in-the-Loop (HITL) methodology.

**Last Updated:** 2026-01-22
**Document Version:** 1.0

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

#### Example 4: Firewall Decision Matrix
- **AI Initial Output**: Suggested binary accept/reject based solely on coherence score
- **Human Enhancement**: Added authentication requirement and ACCEPT_FLAG intermediate state
- **Reasoning**: Zero-trust principles require identity verification independent of signal quality
- **Action Taken**: Implemented full decision matrix with alert levels

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
- Transport variance defaults required multiple iterations before I fully internalized *why* synaptic transmission reliability (0.85) dominates the coherence penalty
- Some nuances only became clear when I had to explain AI errors

**Mitigation Strategy:**
- Mandatory "explain it without AI" check for core concepts
- Periodic manual writing sessions to maintain voice and reasoning skills
- Deliberate engagement with primary sources, not just AI summaries

---

## Tool Disclosure

### AI Tools Used

| Tool | Version/Model | Use Case |
|------|---------------|----------|
| Claude (Anthropic) | Claude Opus 4.5 | Code assistance, documentation drafting, research synthesis |
| Claude Code | CLI | Repository management, file operations, git workflows |

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

This provides a machine-readable audit trail. Commits without this tag represent purely human work.

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
**Repository**: https://github.com/qikevinl/ONI

---

*This transparency statement itself was drafted with AI assistance for structure and formatting. The content, examples, and methodological decisions are human contributions.*
