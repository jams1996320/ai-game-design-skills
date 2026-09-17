# Run in the existing PowerShell session. No persistent execution-policy/PATH changes.
$ErrorActionPreference = 'Stop'
$pythonExe = $null
$candidates = @()
if (Get-Command py -ErrorAction SilentlyContinue) {
    $found = & py -3 -c "import sys; print(sys.executable)" 2>$null
    if ($LASTEXITCODE -eq 0) { $candidates += $found }
}
if (Get-Command python -ErrorAction SilentlyContinue) {
    $found = & python -c "import sys; print(sys.executable)" 2>$null
    if ($LASTEXITCODE -eq 0) { $candidates += $found }
}
$candidates += "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe"
foreach ($candidate in $candidates) {
    if (Test-Path $candidate) {
        & $candidate -c "import sys; assert sys.version_info >= (3,9)" 2>$null
        if ($LASTEXITCODE -eq 0) { $pythonExe = $candidate; break }
    }
}
if (-not $pythonExe) {
    if (-not (Get-Command winget -ErrorAction SilentlyContinue)) {
        throw 'Python and winget unavailable. Codex must diagnose App Installer / managed-device restrictions; do not change machine policy.'
    }
    & winget install --exact --id Python.Python.3.12 --source winget --scope user --accept-source-agreements --accept-package-agreements --disable-interactivity
    if ($LASTEXITCODE -ne 0) { throw 'Python installation failed; inspect winget output before retrying.' }
    $pythonExe = "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe"
    if (-not (Test-Path $pythonExe)) { throw 'Python installed at an unexpected path; locate the executable before continuing.' }
}
& $pythonExe "$PSScriptRoot\setup.py"
if ($LASTEXITCODE -ne 0) { throw 'Isolated runtime setup failed.' }
