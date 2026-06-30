"""
DEE-RSA Statistical Report Generator

Generates formatted reports from benchmark results following
the DEE-RSA Phase III statistical reporting requirements.
"""

import json
import csv
import os
import sys
from math import sqrt
from statistics import mean, stdev


def load_results(json_path="data/benchmark_results.json"):
    """Load benchmark results from JSON file."""
    if not os.path.exists(json_path):
        print(f"Warning: {json_path} not found. Using sample data.")
        return None
    with open(json_path, "r") as f:
        return json.load(f)


def generate_latex_table(results, output_path="data/benchmark_table.tex"):
    """Generate LaTeX-formatted results table."""
    if results is None:
        print("No results to generate table from.")
        return

    lines = []
    lines.append(r"\begin{table}[!htbp]")
    lines.append(r"\centering")
    lines.append(r"\caption{DEE-RSA Phase III Benchmarking Results}")
    lines.append(r"\label{tab:dee_rsa_benchmark}")
    lines.append(r"\begin{tabular}{lcccccc}")
    lines.append(r"\toprule")
    lines.append(r"\textbf{Variant} & \textbf{Bits} & \textbf{KeyGen (ms)} & "
                   r"\textbf{Enc (ms)} & \textbf{Dec (ms)} & "
                   r"\textbf{Throughput} & \textbf{Trials} \\")
    lines.append(r"\midrule")

    for name, sizes in results.items():
        for bits, r in sizes.items():
            lines.append(
                f"{name} & {bits} & "
                f"{r['keygen_ms_mean']:.2f} $\\pm$ {r['keygen_ms_std']:.2f} & "
                f"{r['encrypt_ms_mean']:.2f} $\\pm$ {r['encrypt_ms_std']:.2f} & "
                f"{r['decrypt_ms_mean']:.2f} $\\pm$ {r['decrypt_ms_std']:.2f} & "
                f"{r['throughput_ops_per_sec']:.1f} & {r['trials']} \\\\"
            )

    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table}")

    with open(output_path, "w") as f:
        f.write("\n".join(lines))
    print(f"LaTeX table generated: {output_path}")


def generate_summary_md(results, output_path="data/benchmark_summary.md"):
    """Generate Markdown-formatted summary report."""
    if results is None:
        print("No results to generate summary from.")
        return

    lines = []
    lines.append("# DEE-RSA Phase III Benchmarking Summary")
    lines.append("")
    lines.append(f"**Generated:** {__import__('datetime').datetime.now().isoformat()}")
    lines.append("")

    for name, sizes in results.items():
        lines.append(f"## {name}")
        lines.append("")
        lines.append("| Key Size | KeyGen (ms) | Encrypt (ms) | Decrypt (ms) | Throughput (ops/s) | Trials |")
        lines.append("|----------|------------|-------------|-------------|-------------------|--------|")

        for bits, r in sizes.items():
            lines.append(
                f"| {bits} | "
                f"{r['keygen_ms_mean']:.2f} ± {r['keygen_ms_std']:.2f} | "
                f"{r['encrypt_ms_mean']:.2f} ± {r['encrypt_ms_std']:.2f} | "
                f"{r['decrypt_ms_mean']:.2f} ± {r['decrypt_ms_std']:.2f} | "
                f"{r['throughput_ops_per_sec']:.1f} | {r['trials']} |"
            )

        lines.append("")

    with open(output_path, "w") as f:
        f.write("\n".join(lines))
    print(f"Markdown summary generated: {output_path}")


if __name__ == "__main__":
    results = load_results()
    if results:
        generate_latex_table(results)
        generate_summary_md(results)
        print("DEE-RSA statistical reporting complete.")
    else:
        print("No benchmark results found. Run benchmark first:")
        print("  python -m src.benchmark")
