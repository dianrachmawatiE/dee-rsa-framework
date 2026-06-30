# DEE-RSA: Design--Evaluation--Experimentation Framework for RSA Variants

A standardized three-phase methodology for the systematic development, validation, cryptanalysis, benchmarking, and reporting of novel RSA variants.

## Overview

DEE-RSA addresses the documented gap in RSA variant research: the absence of a unified methodology for evaluating RSA variants across all essential dimensions (security, performance, reproducibility). The framework comprises:

- **Phase I: Design** — Systematic variant specification (motivation, mathematical formulation, parameter selection, key generation design)
- **Phase II: Evaluation** — Correctness verification, security assessment, and an 8-point cryptanalysis checklist
- **Phase III: Experimentation** — Standardized benchmarking protocol with statistical reporting
- **Reproducibility Package** — 10-item checklist based on ACM artifact evaluation criteria

## Repository Structure

```
dee_rsa_repo/
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── LICENSE                            # MIT License
├── src/
│   ├── rsa_variants.py               # Implementations of RSA variants for benchmarking
│   ├── benchmark.py                   # DEE-RSA benchmarking harness
│   └── utils.py                       # Cryptographic utilities
├── scripts/
│   ├── run_benchmarks.ps1            # Windows PowerShell benchmark runner
│   ├── run_benchmarks.sh             # Unix/Linux benchmark runner
│   └── generate_reports.py           # Statistical report generation
├── templates/
│   ├── checklist_dee_rsa.md          # Comprehensive DEE-RSA checklist (30 items)
│   ├── template_benchmarking.md      # Benchmarking recording template
│   ├── template_reporting.md         # Manuscript reporting template
│   └── template_cryptanalysis.md     # Cryptanalysis evaluation template
├── checklists/
│   └── dee_rsa_checklist.md          # Reviewer-facing evaluation checklist
├── examples/
│   └── xrsa_case_study/              # Complete XRSA case study applying DEE-RSA
│       ├── xrsa_dee_rsa_report.md   # Full walkthrough report
│       └── xrsa_benchmark_results.csv # Benchmark data
└── data/
    └── sample_benchmark_results.csv  # Sample output format
```

## Quick Start

### Prerequisites

- Python 3.9 or later
- Dependencies listed in `requirements.txt`

### Installation

```bash
git clone https://github.com/<user>/dee-rsa.git
cd dee-rsa
pip install -r requirements.txt
```

### Running the Benchmarks

**Windows (PowerShell):**
```powershell
.\scripts\run_benchmarks.ps1
```

**Linux/macOS:**
```bash
bash scripts/run_benchmarks.sh
```

### Manual Execution

```python
from src.benchmark import DEEBenchmark

# Run DEE-RSA compliant benchmark
benchmark = DEEBenchmark(key_sizes=[1024, 2048, 4096], trials=100)
results = benchmark.run_all()

# Generate statistical report
from scripts.generate_reports import generate_report
generate_report(results, output="results/benchmark_report.pdf")
```

## How to Use DEE-RSA

1. **Start with the checklist** — Open `templates/checklist_dee_rsa.md` and review all requirements
2. **Design your variant** — Follow Phase I steps in the checklist (motivation, formulation, parameters, keygen)
3. **Evaluate security** — Complete the 8-point cryptanalysis checklist in `templates/template_cryptanalysis.md`
4. **Benchmark systematically** — Use the `Benchmark` class or the shell scripts, record results in `templates/template_benchmarking.md`
5. **Report comprehensively** — Organize your manuscript using `templates/template_reporting.md`
6. **Ensure reproducibility** — Complete all 10 items of the reproducibility checklist

## Citation

If you use DEE-RSA in your research, please cite:

```bibtex
@article{rachmawati2025deersa,
  title={DEE-RSA: A Standardized Framework for the Design, Evaluation,
         and Experimentation of Novel RSA Variants},
  author={Rachmawati, Dian and Lydia, Maya Silvi and
          Budiman, Mohammad Andri and Rahmat, Romi Fadillah},
  journal={MethodsX},
  year={2025}
}
```

## License

MIT License — see `LICENSE` file for details.

## Contributing

Contributions are welcome. Please ensure your contributions follow the DEE-RSA framework guidelines. For major changes, open an issue first to discuss the proposed modification.

## Contact

- Dian Rachmawati — dian.rachmawati@usu.ac.id
- Repository issues: https://github.com/<user>/dee-rsa/issues
