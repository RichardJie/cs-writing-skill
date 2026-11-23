[CmdletBinding()]
param(
    [string]$EnvironmentRoot = (Join-Path ([Environment]::GetFolderPath('MyDocuments')) 'Codex\environments\biomedical-figure-production'),
    [string]$PythonExecutable = 'python'
)

$ErrorActionPreference = 'Stop'
$venvPath = Join-Path $EnvironmentRoot '.venv'
$venvPython = Join-Path $venvPath 'Scripts\python.exe'

if (-not (Test-Path -LiteralPath $EnvironmentRoot)) {
    New-Item -ItemType Directory -Path $EnvironmentRoot | Out-Null
}

if (-not (Test-Path -LiteralPath $venvPython)) {
    & $PythonExecutable -m venv $venvPath
}

& $venvPython -m pip install --upgrade pip setuptools wheel
& $venvPython -m pip install matplotlib seaborn scipy plotnine cnsplots pandas numpy pillow pyyaml

Write-Output "Biomedical figure Python environment: $venvPython"

