# Quantum Security — Index

> **Analysis of quantum computing threats to cryptography and security, including HNDL attacks, physical vulnerabilities, and post-quantum defenses.**

**Status:** Published
**Last Updated:** 2026-01-21
**ONI Layers:** L10-L14 (silicon/software layers), cross-domain implications

---

## Summary

Quantum Security examines the emerging threat landscape where quantum computers pose existential risks to classical cryptography while simultaneously introducing new attack surfaces against quantum systems themselves.

The analysis debunks science fiction scenarios (quantum entanglement enabling "anywhere in the universe" attacks) while highlighting real, mathematically-proven threats: Harvest Now, Decrypt Later (HNDL) attacks where nation-states collect encrypted data today for future decryption, Shor's algorithm breaking RSA/ECC encryption, and physical attacks exploiting quantum hardware fragility.

A key connection to the ONI Framework is the Scale-Frequency Invariant (f × S ≈ k) applied to quantum coherence—demonstrating how the "observer effect" functions as a denial-of-service attack vector against quantum computation, collapsing global quantum states into local noise.

The article proposes a three-category threat taxonomy: attacks BY quantum computers (on classical systems), attacks ON quantum computers (hardware/software vulnerabilities), and attacks on the classical-quantum INTERFACE.

---

## Dependencies

**This topic builds on:**

| Topic | Relationship |
|-------|--------------|
| [ONI Framework](../0-oni-framework/INDEX.md) | Layer model extends to quantum-classical interfaces |
| [Scale-Frequency](../scale-frequency/INDEX.md) | f × S ≈ k invariant applies to quantum coherence |
| [Coherence Metric](../coherence-metric/INDEX.md) | Coherence concepts parallel quantum decoherence |

**Topics that build on this:**

| Topic | Relationship |
|-------|--------------|
| (Future topics) | Post-quantum BCI security, quantum-enhanced neural attacks |

---

## Documents

| Type | Document | Description |
|------|----------|-------------|
| Blog | [Blog-Quantum_Security.md](Blog-Quantum_Security.md) | Accessible deep dive into quantum threats ([Original on Cybersecurity Writeups](https://cybersecuritywriteups.com/can-hackers-attack-quantum-computers-across-time-and-space-the-truth-is-far-more-terrifying-d74e41a2223a)) |

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| HNDL (Harvest Now, Decrypt Later) | Adversaries collecting encrypted data today for quantum decryption later |
| Shor's Algorithm | Quantum algorithm that factors large integers in polynomial time, breaking RSA/ECC |
| Grover's Algorithm | Quantum search providing quadratic speedup, weakening symmetric encryption |
| Coherence Breach | Collapse of quantum computational state through observer effect/probing |
| No-Communication Theorem | Mathematical proof that entanglement cannot transmit information FTL |
| No-Cloning Theorem | Quantum mechanics forbids copying arbitrary quantum states |
| Decoherence Attacks | Physical attacks inducing loss of quantum coherence |
| Multi-Tenant Vulnerabilities | Crosstalk risks on shared quantum cloud platforms |

---

## Threat Taxonomy

| Category | Description | Examples |
|----------|-------------|----------|
| Attacks BY Quantum | Quantum computers attacking classical systems | Shor's, Grover's, optimization attacks |
| Attacks ON Quantum | Targeting quantum hardware/software | Decoherence, side-channel, fault injection |
| Interface Attacks | Exploiting classical-quantum boundary | Control signal manipulation, QRNG attacks |

---

## Related Topics

| Topic | Connection |
|-------|------------|
| [Scale-Frequency](../scale-frequency/INDEX.md) | f × S ≈ k explains coherence collapse mechanics |
| [Coherence Metric](../coherence-metric/INDEX.md) | Signal coherence concepts apply to quantum states |
| [Neural Firewall](../neural-firewall/INDEX.md) | Defense architectures transferable to quantum systems |
| [Neural Ransomware](../neural-ransomware/INDEX.md) | Threat modeling approaches applicable to quantum |

---

## Keywords

**Primary:** quantum security, HNDL, harvest now decrypt later, post-quantum cryptography, quantum threats
**Technical:** Shor's algorithm, Grover's algorithm, quantum decoherence, qubit, RSA, ECC, CRYSTALS-Kyber
**Scientific:** no-communication theorem, no-cloning theorem, Bell inequality, quantum entanglement, superposition
**Security:** side-channel attacks, fault injection, multi-tenant vulnerabilities, cryptographic migration

---

## Future Work

- [ ] TechDoc with formal threat model and mathematical proofs
- [ ] Integration with ONI Framework L10-L14 layer security
- [ ] Quantum-BCI intersection analysis
- [ ] Post-quantum cryptography implementation guide
- [ ] Timeline projections for quantum threat maturity

---

← Back to [Index](../../INDEX.md)
