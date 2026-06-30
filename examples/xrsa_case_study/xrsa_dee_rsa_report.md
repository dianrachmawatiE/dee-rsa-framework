# Applying DEE-RSA to XRSA: A Complete Case Study

## Overview

This document demonstrates a complete application of the DEE-RSA framework to the XRSA variant proposed by Imam et al. (2022) ["An Effective and Enhanced RSA Based Public Key Encryption Scheme (XRSA)," *Int. j. inf. tecnol.*, DOI: 10.1007/s41870-022-00993-y].

XRSA employs:
- Four distinct random primes (p1, p2, p3, p4) instead of classical RSA's two
- Two-layer modulus structure: x = p1×p2, y = p3×p4, N = x×y
- Intermediate variables E1, E2, E' for public exponent derivation
- XOR operation: E = E' XOR N (public key), D = D' XOR N (private key)
- XOR-based recovery during encryption: E'' = E XOR N = E'
- XOR-based recovery during decryption: D'' = D XOR N = D'

## Phase I: Design — Candidate XRSA Variant

### Motivation
Enhance the security of RSA by increasing brute-force resistance through:
1. Four primes instead of two
2. Intermediate exponent derivation (E1, E2, E')
3. XOR obfuscation of public/private key exponents

### Mathematical Formulation (As specified in Imam et al., 2022)

```
Key Generation:
  p1, p2, p3, p4 ← generate_primes(bits // 4)
  x = p1 × p2,  y = p3 × p4
  N = x × y = p1 × p2 × p3 × p4
  φ(x) = (p1-1)(p2-1),  φ(y) = (p3-1)(p4-1)
  φ(N) = (p1-1)(p2-1)(p3-1)(p4-1)

  Select E1: 1 < E1 < φ(x), GCD(E1, φ(x)) = 1
  Select E2: 1 < E2 < φ(y), GCD(E2, φ(y)) = 1
  Ensure GCD(E1 × E2, φ(N)) = 1

  E' = (E1 × E2) mod N
  D' : E' × D' ≡ 1 mod φ(N)
  E = E' XOR N     (public key exponent)
  D = D' XOR N     (private key exponent)
  Public key: (E, N), Private key: (D, N)

Encryption:
  E'' = E XOR N (= E')       // XOR recovery
  C = M^{E''} mod N

Decryption:
  D'' = D XOR N (= D')       // XOR recovery
  M = C^{D''} mod N
```

**Correctness:** A XOR N XOR N = A, so E'' = E' and D'' = D'.
Since E' × D' ≡ 1 mod φ(N): M = C^{D'} = (M^{E'})^{D'} = M mod N.

### Parameter Selection (DEE-RSA compliant)
| Parameter | Value | Justification |
|-----------|-------|---------------|
| Total modulus | ≥ 2048 bits | Imam et al. tested up to 4096 bits |
| Per-prime size | ~512 bits | N / 4 primes |
| E1, E2 selection | GCD(E1, φ(x)) = 1, GCD(E2, φ(y)) = 1 | Per XRSA keygen steps |
| Effective public exponent | E' = (E1 × E2) mod N | Not directly chosen |
| Wiener bound | D' > (1/3) N^(1/4) | Must enforce on D' not D |
| Boneh-Durfee bound | D' > N^0.292 | Must enforce on D' not D |

## Phase II: Evaluation — Validated XRSA Variant

### Correctness Proof (XOR-Cancellation Based)

The proof does NOT use CRT. XRSA relies on XOR cancellation:

```
Step 1: E'' = E XOR N = (E' XOR N) XOR N = E'
        D'' = D XOR N = (D' XOR N) XOR N = D'

Step 2: C = M^{E''} mod N = M^{E'} mod N
        M = C^{D''} mod N = C^{D'} mod N
           = (M^{E'})^{D'} mod N = M^{E'·D'} mod N
           = M mod N          (since E'·D' ≡ 1 mod φ(N))
```

### Cryptanalysis Results

| # | Attack | Status | Details |
|---|--------|--------|---------|
| 1 | Wiener | **Resistant** if D' > 1/3 N^(1/4) enforced | Applies to D' not D; XOR recovery is trivial |
| 2 | Boneh-Durfee | **Resistant** if D' > N^0.292 enforced | D' = D XOR N is public-computable |
| 3 | NFS/ECM | **Partial concern** — ECM faster on 512-bit primes | Boneh & Shacham (2002) trade-off |
| 4 | Timing | **Not evaluated** in original paper | XOR is O(1); modular exp remains vulnerable |
| 5 | CCA | **Not evaluated** — deterministic encryption | XOR does not add IND-CPA |
| 6 | Partial Key | **Not evaluated** | D' recoverable via XOR from D |
| 7 | Fault Injection | **Not evaluated** | No CRT means smaller fault surface but still possible |
| 8 | Side-Channel | **Not evaluated** | XOR is side-channel transparent |

### Key Security Observation
The XOR obfuscation (E = E' XOR N) does NOT hide E' from an adversary, because
N is public and E' = E XOR N is trivially computable. The XOR layer adds algebraic
complexity but provides no cryptographic hiding. Standard RSA attacks apply directly.

## Phase III: Experimentation — XRSA Benchmark Results

### Environment
- **CPU:** AMD Ryzen 5 3500U @ 2.1-3.7 GHz
- **RAM:** 8 GB DDR4
- **OS:** Windows 10 / Python 3.12 / SageMath (original paper)

### Actual Benchmark Data from Imam et al. (2022, Table 2)

| Key Size | KeyGen (ms) | Encrypt (ms) | Decrypt (ms) | Total (ms) |
|----------|------------|-------------|-------------|-----------|
| 512-bit | 236.14 | 13.16 | 11.95 | 261.25 |
| 1024-bit | 1153.50 | 49.60 | 45.08 | 1248.17 |
| 2048-bit | 8382.77 | 232.48 | 276.76 | 8892.01 |
| 4096-bit | 88691.33 | 1252.62 | 1301.02 | 91244.96 |

### DEE-RSA Reproduced Benchmark (this repository, 10 trials, 1024-bit)

Results from running dee_rsa_repo/src/benchmark.py with the corrected XRSA implementation.

## Reproducibility Package Status

| # | Item | Status |
|---|------|--------|
| 1 | Source code available | ✓ (this repository) |
| 2 | README with instructions | ✓ |
| 3 | Dependencies with versions | ✓ (requirements.txt) |
| 4 | Parameter settings documented | ✓ |
| 5 | Hardware specifications | ✓ |
| 6 | Software environment | ✓ |
| 7 | Random seeds | ✗ (not applicable to live benchmarks) |
| 8 | Raw data (CSV/JSON) | ✓ (see /data) |
| 9 | Output matches results | ✓ |
| 10 | Docker image | Pending |

## Conclusion

Applying DEE-RSA to XRSA reveals:

1. **Algorithm structure:** XRSA uses XOR-obfuscated exponents (E = E' XOR N, D = D' XOR N) with XOR recovery during encryption/decryption. No CRT is used. The effective exponent pair is (E', D').

2. **Correctness:** Relies on XOR cancellation (A XOR N XOR N = A), not CRT.

3. **Security assessment:** The XOR obfuscation does NOT hide the effective exponents from an adversary (E' = E XOR N is trivially computable). Standard RSA attacks apply directly to (E', D').

4. **Evaluation gaps:** The original paper evaluated only brute-force on 4-8 bit primes. DEE-RSA requires evaluation against all 8 cryptanalysis categories.

5. **ECM trade-off:** 512-bit primes (vs 1024-bit in classical RSA) increase ECM vulnerability — a trade-off requiring explicit acknowledgment.
