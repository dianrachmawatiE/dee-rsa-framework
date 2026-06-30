# DEE-RSA Reviewer Evaluation Checklist

> Use this checklist when reviewing an RSA variant manuscript for DEE-RSA compliance. Mark Yes/No/Partial for each criterion.

## Phase I: Design — Candidate RSA Variant Specification

| # | Criterion | Yes | No | Partial | Comments |
|---|-----------|-----|----|---------|----------|
| D1 | Motivation explicitly stated with reference to existing RSA limitations | | | | |
| D2 | Mathematical formulation complete (modulus, keys, encryption, decryption) | | | | |
| D3 | Algebraic assumptions stated explicitly | | | | |
| D4 | Parameter bounds justified with cryptanalytic results | | | | |
| D5 | Wiener bound enforced (d > 1/3 N^(1/4)) | | | | |
| D6 | Boneh-Durfee bound enforced (d > N^0.292) | | | | |
| D7 | Fermat condition enforced (|p-q| > 2 N^(1/4)) | | | | |
| D8 | Key generation procedure fully specified | | | | |
| D9 | Entropy source identified | | | | |
| D10 | Modulus size ≥ 2048 bits or justified exception | | | | |

## Phase II: Evaluation — Validated RSA Variant

| # | Criterion | Yes | No | Partial | Comments |
|---|-----------|-----|----|---------|----------|
| E1 | Formal correctness proof provided | | | | |
| E2 | Dec(Enc(m)) = m established for all valid m | | | | |
| E3 | RSA Assumption formally stated | | | | |
| E4 | Factoring Assumption formally stated | | | | |
| E5 | Security property declared (IND-CPA/IND-CCA2/OW-CPA) | | | | |
| E6 | Wiener's attack evaluated | | | | |
| E7 | Boneh-Durfee attack evaluated | | | | |
| E8 | NFS/ECM/Fermat/GCD attacks evaluated | | | | |
| E9 | Timing attacks evaluated | | | | |
| E10 | Chosen ciphertext attacks evaluated | | | | |
| E11 | Partial key exposure attacks evaluated | | | | |
| E12 | Fault injection attacks evaluated | | | | |
| E13 | Side-channel attacks evaluated | | | | |

## Phase III: Experimentation — Experimental Validation Report

| # | Criterion | Yes | No | Partial | Comments |
|---|-----------|-----|----|---------|----------|
| X1 | Key generation time benchmarked (≥100 trials) | | | | |
| X2 | Encryption time benchmarked (≥100 trials) | | | | |
| X3 | Decryption time benchmarked (≥100 trials) | | | | |
| X4 | Throughput measured across key sizes | | | | |
| X5 | Memory usage reported | | | | |
| X6 | Mean ± std reported for each metric | | | | |
| X7 | 95% confidence intervals reported | | | | |
| X8 | Compared against Classical RSA baseline | | | | |
| X9 | Compared against established fast variant | | | | |
| X10 | Compared against recent variant | | | | |
| X11 | Hardware specifications documented | | | | |
| X12 | Software environment documented | | | | |

## Reproducibility

| # | Criterion | Yes | No | Partial | Comments |
|---|-----------|-----|----|---------|----------|
| R1 | Source code in public repository | | | | |
| R2 | README with execution instructions | | | | |
| R3 | Dependencies with version numbers | | | | |
| R4 | Parameter settings documented | | | | |
| R5 | Random seeds provided | | | | |
| R6 | Raw data (CSV/JSON) included | | | | |
| R7 | Output reproduces tables/figures | | | | |
| R8 | Docker/VM image provided | | | | |

## Overall Assessment

- **Design completeness:** ___ / 10 criteria met
- **Evaluation completeness:** ___ / 13 criteria met
- **Experimentation completeness:** ___ / 12 criteria met
- **Reproducibility:** ___ / 8 criteria met
- **Total DEE-RSA compliance score:** ___ / 43

### Recommendation:
[ ] Accept (≥ 38/43, all mandatory items met)
[ ] Accept with minor revisions (≥ 30/43)
[ ] Major revisions required (< 30/43)
[ ] Reject

**Reviewer:** ______________  
**Date:** ______________
