# DEE-RSA Comprehensive Checklist

> Use this checklist when developing and evaluating an RSA variant using the DEE-RSA framework. Mark each item as [x] completed, [ ] pending, or [-] not applicable.

## Phase I: Design

### 1.1 Motivation and Problem Statement
- [ ] Specific limitation of existing RSA constructions is clearly articulated
- [ ] Design objective is explicitly stated (speed, size, security, or adaptation)
- [ ] Variant is positioned within the RSA research taxonomy of Imam et al. (2021)

### 1.2 Mathematical Formulation
- [ ] Modulus structure is completely defined (e.g., n = pq, n = p^k q, n = Π p_i)
- [ ] Key relationship is specified (ed ≡ 1 mod φ(n) or mod λ(n))
- [ ] Encryption function is provided with domain and range
- [ ] Decryption function is provided with domain and range
- [ ] All algebraic assumptions are stated explicitly (e.g., gcd(e, φ(n)) = 1)

### 1.3 Parameter Selection
- [ ] Modulus size ≥ 2048 bits (or justified exception)
- [ ] Public exponent e = 65537 (or justified alternative)
- [ ] Wiener bound enforced: d > (1/3) N^(1/4)
- [ ] Boneh-Durfee bound enforced: d > N^0.292
- [ ] Fermat condition enforced: |p-q| > 2 N^(1/4)
- [ ] For multi-prime: ECM vulnerability analysis for smaller primes

### 1.4 Key Generation Design
- [ ] Entropy source identified (e.g., os.urandom, hardware RNG)
- [ ] Primality testing method and round count specified
- [ ] Rejection handling documented (e.g., gcd(e, φ(n)) ≠ 1)
- [ ] CRT pre-computation procedure specified (if applicable)

## Phase II: Evaluation

### 2.1 Correctness Verification
- [ ] Formal proof that Dec(sk, Enc(pk, m)) = m for all valid m
- [ ] Group-theoretic properties explicitly addressed
- [ ] CRT recombination correctness verified (if applicable)

### 2.2 Security Assessment
- [ ] RSA Assumption formally stated
- [ ] Factoring Assumption formally stated
- [ ] Achieved security property declared (IND-CPA, IND-CCA2, or OW-CPA)
- [ ] Reduction proofs provided where applicable

### 2.3 Cryptanalysis Checklist
- [ ] 1. Wiener's Continued Fraction Attack — evaluated
- [ ] 2. Boneh-Durfee Lattice Attack — evaluated
- [ ] 3. Factorization Attacks (NFS, ECM, Fermat, GCD) — evaluated
- [ ] 4. Timing Attacks — evaluated
- [ ] 5. Chosen Ciphertext Attacks (Bleichenbacher, ROBOT) — evaluated
- [ ] 6. Partial Key Exposure Attacks — evaluated
- [ ] 7. Fault Injection Attacks — evaluated
- [ ] 8. Side-Channel Attacks (power, thermal) — evaluated

## Phase III: Experimentation

### 3.1 Benchmarking Protocol
- [ ] Key Generation Time measured (ms, mean ± σ)
- [ ] Encryption Time measured (ms, mean ± σ)
- [ ] Decryption Time measured (ms, mean ± σ)
- [ ] Throughput measured (ops/sec across key sizes)
- [ ] Memory Usage measured (KB/MB peak)
- [ ] Minimum 100 independent trials per metric
- [ ] Fresh key generation per trial
- [ ] Hardware specifications fully documented
- [ ] Software environment fully documented

### 3.2 Comparative Evaluation
- [ ] Compared against Classical (textbook) RSA baseline
- [ ] Compared against at least one established fast variant (CRT-RSA or Multi-Prime)
- [ ] Compared against at least one recent variant
- [ ] Comparison table includes: key size, encrypt time, decrypt time, throughput, ciphertext size, keygen time, memory

### 3.3 Statistical Reporting
- [ ] Mean (μ) reported for all metrics
- [ ] Standard deviation (σ) reported for all metrics
- [ ] 95% confidence intervals (μ ± 1.96 * σ/√n) reported
- [ ] Raw data available in CSV/JSON format
- [ ] Visualizations provided (box plots or histograms)

## Reproducibility Package

### 4.1 Source Code Availability
- [ ] Complete source code in public persistent repository
- [ ] README.md with step-by-step execution instructions
- [ ] All dependencies listed with explicit version numbers
- [ ] License file included

### 4.2 Documentation
- [ ] Parameter settings completely documented
- [ ] Hardware specifications reported
- [ ] Software environment (OS, compiler, libraries) fully specified
- [ ] Random seeds provided for deterministic reproduction

### 4.3 Data Availability
- [ ] Raw experimental data (CSV/JSON) included in repository
- [ ] Output from running code matches tables/figures in paper
- [ ] Docker container or VM image provided (recommended)

---

**Checklist completed by:** ______________  
**Date:** ______________  
**Variant name:** ______________
