#!/bin/bash
# DEE-RSA Benchmark Runner (Unix/Linux/macOS)

echo "=== DEE-RSA Phase III Benchmarking Protocol ==="
echo ""

PYTHON=$(command -v python3 || command -v python)
if [ -z "$PYTHON" ]; then
    echo "ERROR: Python not found. Please install Python 3.9+."
    exit 1
fi

echo "Python found: $PYTHON"

echo ""
echo "[1/3] Installing dependencies..."
pip install -r requirements.txt 2>/dev/null

echo ""
echo "[2/3] Running DEE-RSA benchmarks (100 trials x 3 key sizes x 4 variants)..."
echo "      This may take several minutes. Please wait..."
echo ""

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"

cd "$REPO_ROOT"
$PYTHON -m src.benchmark

echo ""
echo "[3/3] Generating statistical reports..."
$PYTHON scripts/generate_reports.py

echo ""
echo "=== DEE-RSA Benchmarking Complete ==="
echo "Results saved to:"
echo "  data/benchmark_results.csv"
echo "  data/benchmark_results.json"
