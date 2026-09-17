# Run in the existing PowerShell session. No persistent execution-policy/PATH changes.
$ErrorActionPreference = 'Stop'
if ($env:PROCESSOR_ARCHITECTURE -eq 'ARM64' -or $env:PROCESSOR_ARCHITEW6432 -eq 'ARM64' -or -not [Environment]::Is64BitOperatingSystem) {
    throw 'This installer targets Windows x64. ARM64/32-bit needs separate validation; contact the maintainer.'
}
$pythonExe = $null
$candidates = @()
if (Get-Command py -ErrorAction SilentlyContinue) {
    $found = & py -3.12 -c "import sys; print(sys.executable)" 2>$null
    if ($LASTEXITCODE -eq 0) { $candidates += $found }
}
$pythonCommand = Get-Command python -ErrorAction SilentlyContinue
if ($pythonCommand -and $pythonCommand.Source -notlike '*WindowsApps*') {
    $found = & python -c "import sys; print(sys.executable)" 2>$null
    if ($LASTEXITCODE -eq 0) { $candidates += $found }
}
$candidates += "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe"
foreach ($candidate in $candidates) {
    if (Test-Path $candidate) {
        & $candidate -c "import sys; import platform, struct; assert (3,9) <= sys.version_info[:2] <= (3,12) and struct.calcsize('P') == 8 and platform.machine().lower() in ('amd64','x86_64')" 2>$null
        if ($LASTEXITCODE -eq 0) { $pythonExe = $candidate; break }
    }
}
if (-not $pythonExe) {
    if (-not (Get-Command winget -ErrorAction SilentlyContinue)) {
        throw 'Python and winget unavailable. Codex must diagnose App Installer / managed-device restrictions; do not change machine policy.'
    }
    & winget install --exact --id Python.Python.3.12 --source winget --scope user --architecture x64 --accept-source-agreements --accept-package-agreements --disable-interactivity
    if ($LASTEXITCODE -ne 0) { throw 'Python installation failed; inspect winget output before retrying.' }
    $pythonExe = "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe"
    if (-not (Test-Path $pythonExe)) { throw 'Python installed at an unexpected path; locate the executable before continuing.' }
}
& $pythonExe "$PSScriptRoot\setup.py"
if ($LASTEXITCODE -ne 0) { throw 'Isolated runtime setup failed.' }
