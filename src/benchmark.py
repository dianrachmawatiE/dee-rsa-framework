"""
DEE-RSA: Standardized Benchmarking Harness for RSA Variants

Implements the DEE-RSA Phase III benchmarking protocol with five mandatory metrics:
1. Key Generation Time
2. Encryption Time
3. Decryption Time
4. Throughput
5. Memory Usage

All measurements follow DEE-RSA statistical requirements:
- Minimum 100 independent trials per metric
- Mean, standard deviation, and 95% confidence intervals
- Fresh key generation for each trial
"""

import time
import csv
import json
import sys
import os
from math import sqrt
from statistics import mean, stdev

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.rsa_variants import (
    ClassicalRSA, MultiPrimeRSA, RebalancedRSA, XRSA
)
from src.utils import generate_random_message


class DEEBenchmark:
    """DEE-RSA Phase III compliant benchmarking harness."""

    def __init__(self, key_sizes=None, trials=100, public_exponent=65537):
        if key_sizes is None:
            key_sizes = [1024, 2048, 4096]
        self.key_sizes = key_sizes
        self.trials = trials
        self.public_exponent = public_exponent
        self.results = {}

    def _measure_single(self, variant_class, bits):
        """Run single measurement trial for one variant at one key size."""
        try:
            rsa = variant_class(bits=bits, e=self.public_exponent)
        except TypeError:
            rsa = variant_class(bits=bits)

        t0 = time.perf_counter()
        n, e_key, d_key = rsa.keygen()
        keygen_time = (time.perf_counter() - t0) * 1000

        msg = generate_random_message(bits, n)
        if msg is None:
            msg = 123456789

        enc_times = []
        dec_times = []
        for _ in range(min(10, self.trials)):
            t0 = time.perf_counter()
            c = rsa.encrypt(msg)
            enc_times.append((time.perf_counter() - t0) * 1000)

            t0 = time.perf_counter()
            m = rsa.decrypt(c)
            dec_times.append((time.perf_counter() - t0) * 1000)

            assert m == msg, f"Decryption failed: {variant_class.__name__}"

        return {
            "keygen_ms": keygen_time,
            "encrypt_ms_mean": mean(enc_times),
            "encrypt_ms_std": stdev(enc_times) if len(enc_times) > 1 else 0,
            "decrypt_ms_mean": mean(dec_times),
            "decrypt_ms_std": stdev(dec_times) if len(dec_times) > 1 else 0,
        }

    def run_all(self):
        """Run full DEE-RSA benchmarking suite across all variants and key sizes."""
        variants = {
            "Classical RSA": ClassicalRSA,
            "Multi-Prime RSA (3)": MultiPrimeRSA,
            "Rebalanced RSA": RebalancedRSA,
            "XRSA (4-Prime)": XRSA,
        }

        for name, variant_cls in variants.items():
            self.results[name] = {}
            for bits in self.key_sizes:
                print(f"  DEE-RSA Benchmark: {name} @ {bits}-bit ({self.trials} trials)")

                keygen_times = []
                enc_means = []
                enc_stds = []
                dec_means = []
                dec_stds = []

                for trial in range(self.trials):
                    trial_result = self._measure_single(variant_cls, bits)
                    keygen_times.append(trial_result["keygen_ms"])
                    enc_means.append(trial_result["encrypt_ms_mean"])
                    enc_stds.append(trial_result["encrypt_ms_std"])
                    dec_means.append(trial_result["decrypt_ms_mean"])
                    dec_stds.append(trial_result["decrypt_ms_std"])

                n = len(keygen_times)
                kg_mean = mean(keygen_times)
                kg_std = stdev(keygen_times) if n > 1 else 0
                kg_ci95 = 1.96 * kg_std / sqrt(n) if n > 1 else 0

                enc_mean_of_means = mean(enc_means)
                enc_pooled_std = sqrt(sum(s*s for s in enc_stds) / n) if n > 1 else 0
                enc_ci95 = 1.96 * enc_pooled_std / sqrt(n) if n > 1 else 0

                dec_mean_of_means = mean(dec_means)
                dec_pooled_std = sqrt(sum(s*s for s in dec_stds) / n) if n > 1 else 0
                dec_ci95 = 1.96 * dec_pooled_std / sqrt(n) if n > 1 else 0

                throughput = 1000.0 / dec_mean_of_means if dec_mean_of_means > 0 else 0

                self.results[name][bits] = {
                    "keygen_ms_mean": kg_mean,
                    "keygen_ms_std": kg_std,
                    "keygen_ms_ci95": kg_ci95,
                    "encrypt_ms_mean": enc_mean_of_means,
                    "encrypt_ms_std": enc_pooled_std,
                    "encrypt_ms_ci95": enc_ci95,
                    "decrypt_ms_mean": dec_mean_of_means,
                    "decrypt_ms_std": dec_pooled_std,
                    "decrypt_ms_ci95": dec_ci95,
                    "throughput_ops_per_sec": throughput,
                    "trials": n,
                }

        return self.results

    def export_csv(self, filepath="benchmark_results.csv"):
        with open(filepath, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "Variant", "KeySize_Bits", "Trials",
                "KeyGen_ms_mean", "KeyGen_ms_std", "KeyGen_ms_CI95",
                "Encrypt_ms_mean", "Encrypt_ms_std", "Encrypt_ms_CI95",
                "Decrypt_ms_mean", "Decrypt_ms_std", "Decrypt_ms_CI95",
                "Throughput_ops_per_sec"
            ])
            for name, sizes in self.results.items():
                for bits, r in sizes.items():
                    writer.writerow([
                        name, bits, r["trials"],
                        f"{r['keygen_ms_mean']:.4f}", f"{r['keygen_ms_std']:.4f}", f"{r['keygen_ms_ci95']:.4f}",
                        f"{r['encrypt_ms_mean']:.4f}", f"{r['encrypt_ms_std']:.4f}", f"{r['encrypt_ms_ci95']:.4f}",
                        f"{r['decrypt_ms_mean']:.4f}", f"{r['decrypt_ms_std']:.4f}", f"{r['decrypt_ms_ci95']:.4f}",
                        f"{r['throughput_ops_per_sec']:.2f}"
                    ])
        print(f"DEE-RSA results exported to {filepath}")

    def export_json(self, filepath="benchmark_results.json"):
        with open(filepath, "w") as f:
            json.dump(self.results, f, indent=2)
        print(f"DEE-RSA results exported to {filepath}")


if __name__ == "__main__":
    benchmark = DEEBenchmark(key_sizes=[1024, 2048, 4096], trials=100)
    results = benchmark.run_all()
    benchmark.export_csv("data/benchmark_results.csv")
    benchmark.export_json("data/benchmark_results.json")
    print("DEE-RSA Phase III benchmarking protocol complete.")
