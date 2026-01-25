# Academic Research Landscape: BCI Security & Neuroethics

> A comprehensive mapping of foundational research, key institutions, and notable researchers whose work aligns with and informs the ONI Framework.

**Last Updated:** 2026-01-24
**Purpose:** Academic positioning, collaboration opportunities, graduate program alignment

---

## Table of Contents

- [Executive Summary](#executive-summary)
- [Tier 1: Core Foundational Research](#tier-1-core-foundational-research-directly-integrated)
- [Tier 2: Neuroethics & Policy Research](#tier-2-neuroethics--policy-research)
  - [University of Washington — Neuroethics Research Group](#university-of-washington--neuroethics-research-group)
  - [Harvard Medical School — Center for Bioethics](#harvard-medical-school--center-for-bioethics)
  - [Columbia University — NeuroRights Foundation](#columbia-university--neurorights-foundation)
  - [ETH Zurich / TU Munich — Neurorights Theory](#eth-zurich--tu-munich--neurorights-theory)
  - [Oxford University — Uehiro Centre](#oxford-university--uehiro-centre-for-practical-ethics)
  - [University of British Columbia — Neuroethics Canada](#university-of-british-columbia--neuroethics-canada)
  - [University of Pennsylvania — Center for Neuroscience & Society](#university-of-pennsylvania--center-for-neuroscience--society)
- [Tier 3: Neural Engineering & BCI Development](#tier-3-neural-engineering--bci-development)
  - [Stanford University — Neural Prosthetics Systems Lab](#stanford-university--neural-prosthetics-systems-lab)
  - [Brown University — BrainGate Consortium](#brown-university--braingate-consortium)
  - [Carnegie Mellon University — Biomedical Engineering](#carnegie-mellon-university--biomedical-engineering)
  - [Caltech — Andersen Lab / Chen BMI Center](#caltech--andersen-lab--chen-bmi-center)
  - [Johns Hopkins University](#johns-hopkins-university--apl--physical-medicine)
  - [Duke University — Nicolelis Lab](#duke-university--nicolelis-lab)
  - [Rice University — Neural Interface Lab](#rice-university--neural-interface-lab)
- [Research Gaps ONI Addresses](#research-gaps-oni-addresses)
- [Collaboration Opportunities](#collaboration-opportunities)
- [Citation Practices](#citation-practices)
- [Integrated Research Log](#integrated-research-log)
- [Quick Reference: Key Researchers by Domain](#quick-reference-key-researchers-by-domain)

---

## Executive Summary

The ONI Framework sits at the intersection of three academic domains:
1. **BCI Security** — Technical protection of neural device communications
2. **Neuroethics** — Philosophical and policy frameworks for neural technology
3. **Neural Engineering** — Development of brain-machine interfaces

This document maps the research landscape to:
- Acknowledge foundational work that ONI builds upon
- Identify synergies between ONI's contributions and ongoing research
- Position ONI for academic collaboration and graduate study opportunities

---

## Tier 1: Core Foundational Research (Directly Integrated)

These researchers' work is directly implemented in ONI's codebase.

### University of Washington — Security & Privacy Research Lab + BioRobotics Lab

**The birthplace of "neurosecurity" as a field.**

| Researcher | Role | Key Contributions | ONI Integration |
|------------|------|-------------------|-----------------|
| **[Tadayoshi Kohno](https://homes.cs.washington.edu/~yoshi/)** | Professor, Allen School | Coined "neurosecurity" (2009), IEEE Fellow for cybersecurity contributions | `NeurosecurityFirewall` — CIA threat model |
| **[Tamara Bonaci](https://www.researchgate.net/profile/Tamara-Bonaci)** | PhD, Security Researcher | BCI Anonymizer patent, "brain spyware" demonstration, neural PII classification | `BCIAnonymizer` — privacy-preserving filtering |
| **[Howard Chizeck](https://people.ece.uw.edu/chizeck/)** | Professor Emeritus, BioRobotics | Deep brain stimulator security, closed-loop neural device safety | Attack surface analysis, L8 firewall design |

**Key Publications:**
- Kohno, T., Denning, T., & Matsuoka, Y. (2009). [Neurosecurity: Security and privacy for neural devices](https://cyberlaw.stanford.edu/content/files/doi/pdf/10.3171/2009.4.pdf). *Journal of Neurosurgery: Focus*, 27(1), E7.
- Bonaci, T., Calo, R., & Chizeck, H. (2015). [App Stores for the Brain: Privacy & Security in Brain-Computer Interfaces](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2788104). *IEEE Technology & Society Magazine*, 34(2), 32-39.
- US Patent US20140228701A1 — [Brain-Computer Interface Anonymizer](https://patents.google.com/patent/US20140228701A1)

**How ONI Extends This Work:**
- Implements Kohno's CIA threat model as executable code (`NeurosecurityFirewall`)
- Operationalizes the BCI Anonymizer patent concepts (`BCIAnonymizer`)
- Extends security considerations to a full 14-layer model (beyond device-level to cognitive layers)

---

## Tier 2: Neuroethics & Policy Research

These researchers define the ethical and legal frameworks that ONI's technical implementations serve.

### University of Washington — Neuroethics Research Group

| Researcher | Role | Key Contributions | ONI Alignment |
|------------|------|-------------------|---------------|
| **[Sara Goering](https://phil.washington.edu/people/sara-goering)** | Professor & Chair, Philosophy | Agency in BCI users, disability theory integration, BRAIN Initiative ethics lead | Identity layer (L14) design principles |
| **[Eran Klein](https://phil.washington.edu/neuroethics-research-group)** | Neurologist & Affiliate Professor | Clinical neuroethics, user experience in neural devices | User consent models, cognitive autonomy |

**Key Research:**
- $1.6M NIH grant: "Human Agency and Brain Computer Interfaces" (2018-2022)
- $1.5M NIH R01: "Caring for BRAIN Pioneers" (2022-2026)
- Goering, Brown & Klein (2024). "Brain Pioneers and Moral Entanglement." *Hastings Center Report*.

**How ONI Aligns:**
- L14 (Identity & Ethics layer) directly addresses agency concerns raised by Goering/Klein
- Transparency documentation models HITL methodology they advocate
- User consent frameworks influenced by their "relational agency" concept

---

### Harvard Medical School — Center for Bioethics

| Researcher | Role | Key Contributions | ONI Alignment |
|------------|------|-------------------|---------------|
| **[Gabriel Lázaro-Muñoz](https://bioethics.hms.harvard.edu/faculty-staff/gabriel-lazaro-munoz)** | Assistant Professor | DBS ethics, pediatric neuroethics, International Brain Initiative ethics lead | Privacy layer design, post-trial device access |

**Key Research:**
- Ethical considerations for multimodal perception + neurotechnology integration (2024)
- Post-trial responsibilities for neural device participants
- Member, UNESCO neurotechnology ethics consultation (2024)

**How ONI Aligns:**
- Privacy scoring in `BCIAnonymizer` addresses his neural data concerns
- Framework supports continued access considerations he advocates
- Design accounts for vulnerable populations (pediatric, psychiatric)

---

### Columbia University — NeuroRights Foundation

| Researcher | Role | Key Contributions | ONI Alignment |
|------------|------|-------------------|---------------|
| **[Rafael Yuste](https://en.wikipedia.org/wiki/Rafael_Yuste)** | Professor, Biological Sciences | Co-initiator of BRAIN Initiative, NeuroRights Foundation co-founder, Kavli Institute co-director | Full framework alignment with 5 neurorights |

**The Five Neurorights (Yuste et al.):**
1. **Mental Privacy** — Brain data cannot be used without consent
2. **Personal Identity** — Technology cannot alter sense of self
3. **Free Will** — Decisions without neurotechnological manipulation
4. **Equal Access** — Fair access to cognitive enhancement
5. **Protection from Bias** — No discrimination based on brain data

**Legislative Impact:**
- Chile constitutional reform (2021) — First nation to protect "mental integrity"
- Colorado neurorights law (2024)
- California "Neurorights Bill" (2024) — Senate unanimous approval
- U.S. MIND Act (2025) — First federal neurotechnology governance bill

**How ONI Aligns:**
- L14 (Identity) protects personal identity
- `BCIAnonymizer` implements mental privacy at signal level
- Coherence metric detects manipulation attempts (free will protection)
- Open-source framework supports equal access principle

---

### ETH Zurich / TU Munich — Neurorights Theory

| Researcher | Role | Key Contributions | ONI Alignment |
|------------|------|-------------------|---------------|
| **[Marcello Ienca](https://www.professoren.tum.de/en/ienca-marcello)** | Professor, Ethics of AI & Neuroscience | Four original neurorights proposal (2017), UNESCO advisor, Council of Europe neural data guidelines | Theoretical foundation for privacy layers |

**The Four Neurorights (Ienca & Andorno, 2017):**
1. **Cognitive Liberty** — Right to mental self-determination
2. **Mental Privacy** — Protection against unauthorized brain data collection
3. **Mental Integrity** — Protection from harmful neural intrusions
4. **Psychological Continuity** — Protection of personal identity

**How ONI Aligns:**
- Framework operationalizes Ienca's theoretical neurorights as technical controls
- Coherence metric (Cₛ) provides mathematical basis for "integrity" verification
- L8 Neural Gateway implements "mental integrity" as firewall function

---

### Oxford University — Uehiro Centre for Practical Ethics

| Researcher | Role | Key Contributions | ONI Alignment |
|------------|------|-------------------|---------------|
| **[Hannah Maslen](https://www.practicalethics.ox.ac.uk/people/dr-hannah-maslen)** | Senior Research Fellow | BrainCom project ethics lead, EU BCI regulation advisor, autonomy in closed-loop systems | Adaptive system design, regulatory preparation |

**Key Insight:**
> "It raises questions about autonomy because it's directly modulating the brain... a person who uses a closed-loop system to manage a mood disorder could find themselves unable to have a negative emotional experience, even in a situation in which it would be considered normal."

**How ONI Aligns:**
- Framework accounts for closed-loop system risks in L13 (Semantic) layer
- User override capabilities preserved at every layer
- Regulatory-ready documentation structure

---

### University of British Columbia — Neuroethics Canada

| Researcher | Role | Key Contributions | ONI Alignment |
|------------|------|-------------------|---------------|
| **[Judy Illes](https://neuroethics.med.ubc.ca/)** | Professor, Neurology | WHO consultation on neurotechnologies (2024), UNESCO ethics of neurotechnology (2024), Hastings Center Fellow | International standards alignment |

**How ONI Aligns:**
- Framework designed for international regulatory compliance
- Documentation follows transparency principles she advocates

---

### University of Pennsylvania — Center for Neuroscience & Society

Multi-disciplinary center spanning Medicine, Law, Engineering, and Wharton.

**Research Areas:**
- Ethical, legal, and social implications of neuroscience
- Brain data governance frameworks
- Neurotechnology commercialization ethics

**How ONI Aligns:**
- Addresses legal implications through clear attribution
- Provides technical substrate for policy implementation

---

## Tier 3: Neural Engineering & BCI Development

These researchers advance the BCI technology that ONI aims to secure.

### Stanford University — Neural Prosthetics Systems Lab

| Researcher | Role | Key Contributions | ONI Alignment |
|------------|------|-------------------|---------------|
| **[Krishna Shenoy](https://en.wikipedia.org/wiki/Krishna_Shenoy)** (1968-2023) | Professor (deceased) | BrainGate co-founder, Neuralink co-founder, motor cortex decoding | Signal integrity requirements, L9-L10 design |
| **[Jaimie Henderson](https://nptl.stanford.edu/)** | NPTL Co-Director | Clinical BCI trials, paralysis restoration | Real-world deployment constraints |

**Key Achievements:**
- 90 characters/minute typing via neural signals
- 17+ years of safety data on intracortical BCIs
- Elected to National Academy of Medicine (2022)

**How ONI Can Contribute:**
- Security layer for BrainGate-class devices
- Framework for multi-site clinical trial security standardization

---

### Brown University — BrainGate Consortium

| Researcher | Role | Key Contributions | ONI Alignment |
|------------|------|-------------------|---------------|
| **[Leigh Hochberg](https://www.braingate.org/team/krishna-shenoy-ph-d/)** | Associate Professor | BrainGate clinical trial director, speech decoding (97% accuracy) | Clinical translation pathway |
| **[John Donoghue](https://www.brown.edu/news/2021-05-12/handwriting)** | Institute Director | BrainGate founder, Utah array pioneer | Historical context, foundational tech |

**Key Achievements:**
- First wireless high-bandwidth human BCI (2021)
- 97% accuracy speech decoding for ALS patients (2023)
- 17+ years adverse event monitoring data

**How ONI Can Contribute:**
- Wireless BCI security protocols
- Long-term implant integrity monitoring

---

### Carnegie Mellon University — Biomedical Engineering

| Researcher | Role | Key Contributions | ONI Alignment |
|------------|------|-------------------|---------------|
| **[Bin He](https://engineering.cmu.edu/directory/bios/he-bin.html)** | Trustee Professor | Bidirectional BCI with ultrasound neuromodulation, non-invasive BCI | Non-invasive security considerations |

**Key Achievement (2024):**
First bidirectional BCI integrating EEG decoding with focused ultrasound stimulation, demonstrating machine learning-enhanced BCI performance.

**How ONI Can Contribute:**
- Bidirectional communication security (both encoding and decoding)
- ML model integrity verification for BCI decoders

---

### Caltech — Andersen Lab / Chen BMI Center

| Researcher | Role | Key Contributions | ONI Alignment |
|------------|------|-------------------|---------------|
| **[Richard Andersen](https://www.vis.caltech.edu/)** | Professor | Posterior parietal cortex BCIs, internal speech decoding, sensory feedback | Intent decoding security |

**Key Research:**
- BMI devices that predict internal (unspoken) speech
- Bidirectional BMIs with sensory feedback via stimulation
- FDA-approved clinical studies on sensory restoration

**How ONI Can Contribute:**
- Intent privacy protection (L13 Semantic layer)
- Stimulation safety bounds (bidirectional security)

---

### Johns Hopkins University — APL + Physical Medicine

| Researcher | Role | Key Contributions | ONI Alignment |
|------------|------|-------------------|---------------|
| **[Pablo Celnik](https://celniklab.johnshopkins.edu/)** | Professor & Director | Bilateral BCI control, non-invasive brain stimulation, motor learning | Dual-hemisphere security |

**Key Achievements:**
- First bilateral MEA implantation (both brain hemispheres)
- Simultaneous control of two prosthetic arms
- Virtual object perception via BCI (mixed reality integration)

**How ONI Can Contribute:**
- Multi-array synchronization security
- Mixed reality BCI attack surface analysis

---

### Duke University — Nicolelis Lab

| Researcher | Role | Key Contributions | ONI Alignment |
|------------|------|-------------------|---------------|
| **[Miguel Nicolelis](https://en.wikipedia.org/wiki/Miguel_Nicolelis)** | Professor | Brain-to-brain interfaces, exoskeleton control (2014 World Cup), tactile feedback | Multi-subject security |
| **[Mikhail Lebedev](https://sites.google.com/site/lebedevneuro/)** | Senior Research Scientist | BMI signal processing, motor intent decoding | Signal processing security |

**Key Achievement:**
2014 World Cup opening kick by paraplegic patient using brain-controlled exoskeleton with tactile feedback.

**How ONI Can Contribute:**
- Brain-to-brain interface security (if BTBI becomes clinical)
- Exoskeleton command verification

---

### Rice University — Neural Interface Lab

**Opened January 2025** — Emerging research center with focus on novel neural interfaces.

**How ONI Can Contribute:**
- Early security-by-design integration opportunity
- Framework adoption during development phase

---

## Research Gaps ONI Addresses

| Gap in Current Research | ONI's Contribution |
|-------------------------|-------------------|
| No unified security model across BCI types | 14-layer model applicable to invasive, non-invasive, and hybrid BCIs |
| Privacy concepts remain theoretical | `BCIAnonymizer` provides executable implementation |
| No standard threat taxonomy | Kohno CIA model + attack pattern library in TARA |
| Layer-by-layer attack surface undefined | ONI explicitly maps attacks to layers L1-L14 |
| Coherence/integrity unmeasured | Cₛ metric provides quantifiable signal trust |
| Neurorights lack technical enforcement | Framework translates rights to technical controls |

---

## Collaboration Opportunities

### For Graduate Study Applications

| Institution | Program | Faculty Alignment | ONI Contribution |
|-------------|---------|-------------------|------------------|
| **University of Washington** | CSE (Security) | Kohno, Goering, Klein | Extend neurosecurity, neuroethics implementation |
| **Harvard** | Bioethics / HMS | Lázaro-Muñoz | Technical substrate for ethics research |
| **Columbia** | Neuroscience | Yuste | Neurorights enforcement mechanisms |
| **Stanford** | Bioengineering | Henderson (NPTL) | Clinical security protocols |
| **CMU** | Biomedical Engineering | He | Bidirectional BCI security |
| **Brown** | Neuroscience | Hochberg | BrainGate security layer |

### For Research Partnerships

- **Technical Integration:** ONI could serve as security middleware for BrainGate, NPTL, or Chen BMI Center trials
- **Policy Translation:** Framework provides technical reference for neurorights legislation
- **Standards Development:** Contribute to IEEE, ISO neural device security standards

---

## Citation Practices

When referencing foundational work in ONI publications:

### Required Citations (Direct Implementation)
```
Kohno, T., Denning, T., & Matsuoka, Y. (2009). Neurosecurity: Security and privacy
    for neural devices. Journal of Neurosurgery: Focus, 27(1), E7.

Bonaci, T., Calo, R., & Chizeck, H. (2015). App stores for the brain: Privacy &
    security in brain-computer interfaces. IEEE Technology & Society Magazine,
    34(2), 32-39.
```

### Recommended Citations (Theoretical Foundation)
```
Ienca, M., & Andorno, R. (2017). Towards new human rights in the age of
    neuroscience and neurotechnology. Life Sciences, Society and Policy, 13(1), 5.

Yuste, R., et al. (2017). Four ethical priorities for neurotechnologies and AI.
    Nature, 551(7679), 159-163.

Goering, S., & Klein, E. (2020). Neurotechnology and human agency.
    Philosophy & Technology, 33(3), 375-396.
```

---

## Integrated Research Log

> Tracking research successfully integrated into ONI. See [RESEARCH_INTEGRATION_WORKFLOW.md](resources/workflows/RESEARCH_INTEGRATION_WORKFLOW.md) for the full integration process.

| Date | Paper/Patent | Authors | Type | ONI Component | Status |
|------|--------------|---------|------|---------------|--------|
| 2026-01 | Neurosecurity (2009) | Kohno, Denning, Matsuoka | MODEL | `NeurosecurityFirewall` — CIA threat model | Complete |
| 2026-01 | BCI Anonymizer Patent | Bonaci, Calo, Chizeck | CODE | `BCIAnonymizer` — privacy filtering | Complete |
| 2026-01 | App Stores for Brain (2015) | Bonaci, Calo, Chizeck | MODEL | Neural PII classification | Complete |
| 2026-01 | Four Neurorights (2017) | Ienca, Andorno | ETHICS | L14 Identity layer principles | Complete |
| 2026-01 | Five Neurorights (2017) | Yuste et al. | ETHICS | Framework-wide alignment | Complete |

### Integration Queue

| Priority | Research Area | Researcher | Target | Type | Status |
|----------|---------------|------------|--------|------|--------|
| P1 | Bidirectional BCI security | He (CMU) | L8 firewall rules | CODE | Queued |
| P1 | Synaptic reliability data | Hochberg (Brown) | Coherence validation | VALIDATION | Queued |
| P2 | Intent decoding privacy | Andersen (Caltech) | L13 Semantic layer | MODEL | Planned |
| P2 | Closed-loop autonomy | Maslen (Oxford) | User override mechanisms | MODEL | Planned |
| P3 | DBS pediatric ethics | Lázaro-Muñoz (Harvard) | Vulnerable populations | ETHICS | Backlog |

---

## Document Maintenance

Update this document when:
- New significant BCI security/neuroethics publications emerge
- Researchers change institutions
- Legislative developments occur
- New collaboration opportunities identified
- Research integrations completed (update log above)

---

*This document was compiled with AI assistance for research synthesis. All academic claims verified against primary sources. Institution and researcher information current as of January 2026.*

---

## Quick Reference: Key Researchers by Domain

### BCI Security
- Tadayoshi Kohno (UW) — Foundational neurosecurity
- Tamara Bonaci (UW) — BCI privacy, anonymization
- Howard Chizeck (UW) — Device security, closed-loop systems

### Neuroethics
- Sara Goering (UW) — Agency, disability theory
- Eran Klein (UW) — Clinical neuroethics
- Gabriel Lázaro-Muñoz (Harvard) — DBS ethics, pediatric
- Rafael Yuste (Columbia) — Neurorights, BRAIN Initiative
- Marcello Ienca (TU Munich) — Neurorights theory
- Hannah Maslen (Oxford) — Autonomy, regulation
- Judy Illes (UBC) — International standards

### Neural Engineering
- Leigh Hochberg (Brown) — BrainGate, clinical trials
- Richard Andersen (Caltech) — Intent decoding
- Bin He (CMU) — Bidirectional BCI
- Pablo Celnik (Johns Hopkins) — Bilateral BCIs
- Miguel Nicolelis (Duke) — Exoskeletons, BTBI
