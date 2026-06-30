# DEE-RSA Reporting Template

> Use this template to structure an RSA variant manuscript following the DEE-RSA framework. Each section maps to a DEE-RSA Phase output.

---

## 1. Introduction

### 1.1 Motivation and Problem Statement
[Articulate the specific limitation of existing RSA constructions that the proposed variant addresses. Reference the classification framework of Imam et al. (2021).]

Key references: \cite{rivest1978method,boneh1999twenty,imam2021systematic}

### 1.2 Contributions
[List contributions following DEE-RSA structure:]

1. **Variant Specification** --- [Description of the novel RSA variant]
2. **Security Analysis** --- [Completed cryptanalysis using DEE-RSA checklist]
3. **Performance Evaluation** --- [DEE-RSA Phase III benchmarking results]
4. **Reproducibility Package** --- [Public repository and documentation]

## 2. Related Work

### 2.1 RSA Variants
[Position the proposed variant within the established taxonomy:
- Multi-Prime RSA variants
- Multi-Power RSA variants
- Rebalanced RSA variants
- CRT-based variants
- Recent proposals]

### 2.2 Existing Evaluation Practices
[Discuss gaps identified by Imam et al. (2021) and Boneh and Shacham (2002). Reference the reproducibility literature.]

## 3. Proposed Variant: [Name]

### 3.1 Mathematical Formulation (DEE-RSA Phase I)

**Modulus structure:**
[Define n = ...]

**Key relationship:**
[Define ed ≡ 1 mod ...]

**Encryption function:**
[Define c = Enc(pk, m)]

**Decryption function:**
[Define m = Dec(sk, c)]

**Algebraic assumptions:**
[State all assumptions explicitly]

### 3.2 Parameter Selection
[Document all parameter bounds with cryptanalytic justification:
- Modulus ≥ 2048 bits
- e = 65537
- Wiener bound: d > (1/3) N^(1/4)
- Boneh-Durfee bound: d > N^0.292
- Fermat condition: |p-q| > 2 N^(1/4)]

### 3.3 Key Generation Algorithm
[Provide complete keygen procedure:
1. Prime generation (entropy source, primality testing)
2. Modulus computation
3. Exponent derivation
4. Parameter validation (Wiener, Boneh-Durfee, Fermat checks)]

## 4. Security Evaluation (DEE-RSA Phase II)

### 4.1 Correctness Proof
[Formal proof that Dec(sk, Enc(pk, m)) = m for all valid m]

### 4.2 Hardness Assumptions
- **RSA Assumption:** [Formal statement]
- **Factoring Assumption:** [Formal statement]
- **Achieved Security:** [IND-CPA / IND-CCA2 / OW-CPA]

### 4.3 Cryptanalysis Checklist

| # | Attack | Status | Justification |
|---|--------|--------|---------------|
| 1 | Wiener's Continued Fraction | [Resistant/Vulnerable/N.A.] | |
| 2 | Boneh-Durfee Lattice | [Resistant/Vulnerable/N.A.] | |
| 3 | Factorization (NFS/ECM/Fermat/GCD) | [Resistant/Vulnerable/N.A.] | |
| 4 | Timing Attacks | [Resistant/Vulnerable/N.A.] | |
| 5 | Chosen Ciphertext Attacks | [Resistant/Vulnerable/N.A.] | |
| 6 | Partial Key Exposure | [Resistant/Vulnerable/N.A.] | |
| 7 | Fault Injection Attacks | [Resistant/Vulnerable/N.A.] | |
| 8 | Side-Channel Attacks | [Resistant/Vulnerable/N.A.] | |

## 5. Performance Evaluation (DEE-RSA Phase III)

### 5.1 Experimental Setup
- **Hardware:** [CPU, RAM, OS]
- **Software:** [Language, version, libraries]
- **Parameters:** [Key sizes, e value, trial count]

### 5.2 Benchmarking Results

[Include tables with μ, σ, 95% CI for all five metrics across all key sizes]

### 5.3 Comparative Evaluation

[Comparison tables against Classical RSA, established fast variant, and recent variant]

## 6. Reproducibility Package

### 6.1 Source Code Availability
- Repository URL: ______________
- Commit hash: ______________

### 6.2 Reproducibility Checklist

| # | Item | Status |
|---|------|--------|
| 1 | Source code publicly available | |
| 2 | README.md with execution instructions | |
| 3 | Dependencies with version numbers | |
| 4 | Parameter settings documented | |
| 5 | Hardware specifications reported | |
| 6 | Software environment specified | |
| 7 | Random seeds provided | |
| 8 | Raw data (CSV/JSON) included | |
| 9 | Output matches tables/figures | |
| 10 | Docker/VM image provided | |

## 7. Conclusion

[Summary of contributions, validation results, and call for community adoption of DEE-RSA]

## References

[Complete bibliography]
