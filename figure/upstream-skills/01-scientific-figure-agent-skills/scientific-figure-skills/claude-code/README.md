# Claude Code Package

This directory contains the Claude Code distribution of the Scientific Figure
Suite. See the [repository README](../README.md) for capabilities, installation,
and usage.

```text
skills/scientific-figure-suite/   # the skill (discovered via SKILL.md)
claude-commands/fig/              # optional /fig:<name> slash commands for ~/.claude/commands/fig/
quick_validate.py                 # full validation for this package
```

Install from the repository root with `bash install.sh` (Linux, macOS, WSL) or
`powershell -ExecutionPolicy Bypass -File .\install.ps1` (Windows). Validate
with `python claude-code/quick_validate.py`.
