# DEE-RSA Benchmark Runner (Windows PowerShell)

Write-Host "=== DEE-RSA Phase III Benchmarking Protocol ===" -ForegroundColor Cyan
Write-Host ""

$pythonCmd = (Get-Command python -ErrorAction SilentlyContinue)
if (-not $pythonCmd) {
    $pythonCmd = (Get-Command python3 -ErrorAction SilentlyContinue)
}

if (-not $pythonCmd) {
    Write-Host "ERROR: Python not found. Please install Python 3.9+." -ForegroundColor Red
    exit 1
}

Write-Host "Python found: $($pythonCmd.Source)" -ForegroundColor Green

# Install dependencies
Write-Host "`n[1/3] Installing dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt 2>$null

# Run benchmarks
Write-Host "`n[2/3] Running DEE-RSA benchmarks (100 trials x 3 key sizes x 4 variants)..." -ForegroundColor Yellow
Write-Host "      This may take several minutes. Please wait...`n"

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Split-Path -Parent $repoRoot

Push-Location $repoRoot
try {
    python -m src.benchmark
} finally {
    Pop-Location
}

# Generate reports
Write-Host "`n[3/3] Generating statistical reports..." -ForegroundColor Yellow
Push-Location $repoRoot
try {
    python scripts/generate_reports.py
} finally {
    Pop-Location
}

Write-Host "`n=== DEE-RSA Benchmarking Complete ===" -ForegroundColor Cyan
Write-Host "Results saved to:" -ForegroundColor White
Write-Host "  data/benchmark_results.csv" -ForegroundColor Gray
Write-Host "  data/benchmark_results.json" -ForegroundColor Gray
