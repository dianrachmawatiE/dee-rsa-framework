# DEE-RSA Cryptanalysis Evaluation Template

> Complete this template for each novel RSA variant, documenting resistance or susceptibility to each attack category in the DEE-RSA cryptanalysis checklist (8 items).

## Variant Information

| Field | Value |
|-------|-------|
| Variant Name | |
| Modulus Structure | |
| Key Relationship | |
| Minimum Key Size (bits) | |
| Public Exponent Value | |
| Deterministic / Probabilistic | |

---

## Attack 1: Wiener's Continued Fraction Attack

**Reference:** Wiener (1990); Verheul & van Tilborg (1997); de Weger (2002); Bunder & Tonien (2017); Nitaj et al. (2024)

**Condition for vulnerability:** Private exponent d < (1/3) N^(1/4)

**Variant assessment:**

| Aspect | Value |
|--------|-------|
| Minimum d for recommended key size | |
| Wiener bound threshold for same key size | |
| Is d sufficiently large? | Yes / No |
| Analysis methodology | |
| Verdict | Resistant / Vulnerable / Not Evaluated |

---

## Attack 2: Boneh-Durfee Lattice Attack

**Reference:** Boneh & Durfee (2000); Nitaj (2009); Blömer & May (2003)

**Condition for vulnerability:** Private exponent d < N^0.292

**Variant assessment:**

| Aspect | Value |
|--------|-------|
| Minimum d for recommended key size | |
| Boneh-Durfee bound threshold | |
| Is d sufficiently large? | Yes / No |
| F-constrained exponent analysis (Nitaj, 2009) | |
| Verdict | Resistant / Vulnerable / Not Evaluated |

---

## Attack 3: Factorization Attacks (NFS, ECM, Fermat, GCD)

**Reference:** Lenstra (1990); Boneh & Shacham (2002); Albrecht et al. (2018); Heninger et al. (2012)

**Assessment dimensions:**

| Attack Method | Relevant? | Assessment |
|---------------|-----------|------------|
| Number Field Sieve (NFS) | Yes / No | |
| Elliptic Curve Method (ECM) | Yes / No | |
| Fermat Factorization | Yes / No | |
| GCD Attack (shared primes) | Yes / No | |
| Prime size for ECM resistance | | |
| Fermat condition: |p-q| > 2N^(1/4) enforced? | Yes / No |
| Verdict | | Resistant / Vulnerable / Not Evaluated |

---

## Attack 4: Timing Attacks

**Reference:** Kocher (1996); Cáceres et al. (2022)

**Assessment dimensions:**

| Aspect | Value |
|--------|-------|
| Are constant-time operations used? | Yes / No |
| Is RSA blinding implemented? | Yes / No |
| Cache-timing assessment (decryption) | |
| Cache-timing assessment (key generation) | |
| Verdict | Resistant / Vulnerable / Not Evaluated |

---

## Attack 5: Chosen Ciphertext Attacks (Bleichenbacher, ROBOT)

**Reference:** Bleichenbacher (1998); Böck et al. (2018, ROBOT); Meyer et al. (2014)

**Assessment dimensions:**

| Aspect | Value |
|--------|-------|
| Is the variant deterministic? | Yes / No |
| If deterministic, is IND-CPA achievable? | Yes / No |
| Is PKCS#1 v1.5 padding used? | Yes / No |
| Is OAEP or RSA-KEM applied? | Yes / No |
| Bleichenbacher oracle assessment | |
| Verdict | Resistant / Vulnerable / Not Evaluated |

---

## Attack 6: Partial Key Exposure Attacks

**Reference:** Boneh, Durfee & Frankel (1998)

**Assessment dimensions:**

| Aspect | Value |
|--------|-------|
| Bits of d needed for recovery (theoretical) | |
| Bits of p or q needed for recovery | |
| Is the variant more or less resilient than standard RSA? | |
| Verdict | Resistant / Vulnerable / Not Evaluated |

---

## Attack 7: Fault Injection Attacks

**Reference:** Boneh, DeMillo & Lipton (1997); Chiu & Xiong (2023); Erata et al. (2024)

**Assessment dimensions:**

| Aspect | Value |
|--------|-------|
| Is CRT-based decryption used? | Yes / No |
| Number of CRT components (fault surface) | |
| Are fault countermeasures in place? | Yes / No |
| CRT output validation performed? | Yes / No |
| Random Self-Reducibility (RSR) applied? | Yes / No |
| Verdict | Resistant / Vulnerable / Not Evaluated |

---

## Attack 8: Side-Channel Attacks (Power, Thermal)

**Reference:** Aljuffri et al. (2021); Socha et al. (2022)

**Assessment dimensions:**

| Aspect | Value |
|--------|-------|
| Power analysis assessment | |
| Thermal side-channel assessment | |
| EM emanation assessment | |
| Countermeasures in place? | Yes / No |
| Verdict | Resistant / Vulnerable / Not Evaluated |

---

## Overall Assessment Summary

| Attack # | Attack Name | Verdict |
|----------|-------------|---------|
| 1 | Wiener's Continued Fraction | |
| 2 | Boneh-Durfee Lattice | |
| 3 | Factorization (NFS/ECM/Fermat/GCD) | |
| 4 | Timing Attacks | |
| 5 | Chosen Ciphertext Attacks | |
| 6 | Partial Key Exposure | |
| 7 | Fault Injection Attacks | |
| 8 | Side-Channel Attacks | |

**Evaluator:** ______________  
**Date:** ______________  
**Variant version/revision:** ______________
