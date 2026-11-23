# Install the Scientific Figure Suite skill for Claude Code and/or OpenAI Codex on Windows.
#
#   powershell -ExecutionPolicy Bypass -File .\install.ps1                      Claude Code (default)
#   powershell -ExecutionPolicy Bypass -File .\install.ps1 -Platform codex      Codex
#   powershell -ExecutionPolicy Bypass -File .\install.ps1 -Platform all        both
#   powershell -ExecutionPolicy Bypass -File .\install.ps1 -NoCommands          Claude Code: skip the /fig:* command pack
#   powershell -ExecutionPolicy Bypass -File .\install.ps1 -Project             install into .\.claude and/or .\.codex
#
# Targets: Claude Code -> $env:CLAUDE_CONFIG_DIR (default %USERPROFILE%\.claude),
#          Codex       -> $env:CODEX_HOME        (default %USERPROFILE%\.codex)
param(
  [ValidateSet("claude", "codex", "all")] [string]$Platform = "claude",
  [switch]$NoCommands,
  [switch]$Project
)
$ErrorActionPreference = "Stop"
$repo = Split-Path -Parent $MyInvocation.MyCommand.Path

function Install-Tree([string]$src, [string]$dst) {
  if (-not (Test-Path $src)) { throw "source missing: $src" }
  New-Item -ItemType Directory -Force -Path (Split-Path -Parent $dst) | Out-Null
  if (Test-Path $dst) { Remove-Item -Recurse -Force $dst }
  Copy-Item -Recurse -Force $src $dst
  Get-ChildItem -Path $dst -Recurse -Directory -Filter "__pycache__" -ErrorAction SilentlyContinue | Remove-Item -Recurse -Force
  Write-Host "[OK] $src -> $dst"
}

function Install-Claude {
  if ($Project) { $home_ = Join-Path (Get-Location) ".claude" }
  elseif ($env:CLAUDE_CONFIG_DIR) { $home_ = $env:CLAUDE_CONFIG_DIR }
  else { $home_ = Join-Path $HOME ".claude" }
  Install-Tree (Join-Path $repo "claude-code\skills\scientific-figure-suite") (Join-Path $home_ "skills\scientific-figure-suite")
  if (-not $NoCommands) {
    Install-Tree (Join-Path $repo "claude-code\claude-commands\fig") (Join-Path $home_ "commands\fig")
  }
  Write-Host "[INFO] Claude Code: start a new session, then try  /scientific-figure-suite  or  /fig:scope ..."
}

function Install-Codex {
  if ($Project) { $home_ = Join-Path (Get-Location) ".codex" }
  elseif ($env:CODEX_HOME) { $home_ = $env:CODEX_HOME }
  else { $home_ = Join-Path $HOME ".codex" }
  Install-Tree (Join-Path $repo "codex\skills\scientific-figure-suite") (Join-Path $home_ "skills\scientific-figure-suite")
  Write-Host "[INFO] Codex: restart Codex or reload skills, then try  `$scientific-figure-suite ...  or  fig-scope ..."
}

switch ($Platform) {
  "claude" { Install-Claude }
  "codex"  { Install-Codex }
  "all"    { Install-Claude; Install-Codex }
}
Write-Host "Python dependencies for the suite scripts: python -m pip install -r $repo\requirements-dev.txt"
