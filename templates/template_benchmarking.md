# DEE-RSA Benchmarking Template

> Use this template to record benchmarking results following the DEE-RSA Phase III protocol. All times in milliseconds (ms) unless otherwise specified. Minimum 100 independent trials per metric.

## Hardware Specifications

| Item | Specification |
|------|---------------|
| CPU Model | |
| CPU Architecture | |
| Base Clock (GHz) | |
| Physical Cores | |
| RAM (GB) | |
| RAM Type | |
| OS Name & Version | |
| Hardware Acceleration | (AES-NI, AVX-512, etc.) |

## Software Environment

| Item | Specification |
|------|---------------|
| Programming Language | |
| Language Version | |
| Cryptographic Library | |
| Library Version | |
| Compiler/Interpreter Flags | |
| Additional Dependencies | |

## Parameter Settings

| Parameter | Value |
|-----------|-------|
| Key Sizes Tested (bits) | 1024, 2048, 4096 |
| Public Exponent (e) | 65537 |
| Trials per Measurement | 100 |
| Random Seed (optional) | |
| Miller-Rabin Rounds | 40 |

## Benchmark Results

### Variant: ______________

#### Key Size: 1024 bits

| Metric | Mean (μ) | Std Dev (σ) | 95% CI (μ ± 1.96·σ/√n) |
|--------|----------|-------------|---------------------------|
| Key Generation Time (ms) | | | |
| Encryption Time (ms) | | | |
| Decryption Time (ms) | | | |
| Throughput (ops/sec) | | N/A | N/A |
| Peak Memory (KB) | | | |

#### Key Size: 2048 bits

| Metric | Mean (μ) | Std Dev (σ) | 95% CI (μ ± 1.96·σ/√n) |
|--------|----------|-------------|---------------------------|
| Key Generation Time (ms) | | | |
| Encryption Time (ms) | | | |
| Decryption Time (ms) | | | |
| Throughput (ops/sec) | | N/A | N/A |
| Peak Memory (KB) | | | |

#### Key Size: 4096 bits

| Metric | Mean (μ) | Std Dev (σ) | 95% CI (μ ± 1.96·σ/√n) |
|--------|----------|-------------|---------------------------|
| Key Generation Time (ms) | | | |
| Encryption Time (ms) | | | |
| Decryption Time (ms) | | | |
| Throughput (ops/sec) | | N/A | N/A |
| Peak Memory (KB) | | | |

## Comparative Evaluation

| Variant | Key Size | Encrypt (ms) | Decrypt (ms) | Throughput (ops/s) | KeyGen (ms) | Memory (KB) |
|---------|----------|-------------|-------------|-------------------|------------|------------|
| Proposed Variant | 2048 | | | | | |
| Classical RSA (baseline) | 2048 | | | | | |
| CRT-RSA | 2048 | | | | | |
| [Recent Variant] | 2048 | | | | | |

## Notes

- All measurements conducted on ______ (date)
- Raw data file: `benchmark_data_YYYYMMDD.csv`
- Any anomalies or observations:
