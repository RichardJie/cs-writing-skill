#!/usr/bin/env bash
# Install the Scientific Figure Suite skill for Claude Code and/or OpenAI Codex.
#
#   bash install.sh                       install for Claude Code (default)
#   bash install.sh --platform codex      install for Codex
#   bash install.sh --platform all        install for both
#   bash install.sh --link                symlink instead of copying (keeps this checkout as the source)
#   bash install.sh --no-commands         Claude Code: skip the /fig:* command pack
#   bash install.sh --project             install into ./.claude and/or ./.codex of the current project
#
# Targets: Claude Code -> $CLAUDE_HOME (default ~/.claude), Codex -> $CODEX_HOME (default ~/.codex)
set -Eeuo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
platform="claude"
mode="copy"
with_commands=1
project=0
for arg in "$@"; do
  case "${arg}" in
    --platform=*) platform="${arg#--platform=}" ;;
    --platform) : ;;  # handled below via positional pairing
    claude|codex|all) platform="${arg}" ;;
    --link) mode="link" ;;
    --no-commands) with_commands=0 ;;
    --project) project=1 ;;
    -h|--help) sed -n '2,11p' "${BASH_SOURCE[0]}"; exit 0 ;;
    *) printf '[FAIL] unknown option: %s\n' "${arg}" >&2; exit 1 ;;
  esac
done
case "${platform}" in claude|codex|all) ;; *) printf '[FAIL] --platform must be claude, codex, or all\n' >&2; exit 1 ;; esac

install_tree() {
  local src="$1" dst="$2"
  [[ -e "${src}" ]] || { printf '[FAIL] source missing: %s\n' "${src}" >&2; exit 1; }
  mkdir -p "$(dirname "${dst}")"
  if [[ -L "${dst}" || -e "${dst}" ]]; then rm -rf "${dst}"; fi
  if [[ "${mode}" == "link" ]]; then
    ln -s "${src}" "${dst}"
  else
    cp -R "${src}" "${dst}"
    find "${dst}" -name '__pycache__' -type d -prune -exec rm -rf {} + 2>/dev/null || true
  fi
  printf '[OK] %s -> %s (%s)\n' "${src}" "${dst}" "${mode}"
}

install_claude() {
  local home
  if [[ "${project}" -eq 1 ]]; then home="$(pwd)/.claude"; else home="${CLAUDE_HOME:-${HOME}/.claude}"; fi
  install_tree "${repo_root}/claude-code/skills/scientific-figure-suite" "${home}/skills/scientific-figure-suite"
  if [[ "${with_commands}" -eq 1 ]]; then
    install_tree "${repo_root}/claude-code/claude-commands/fig" "${home}/commands/fig"
  fi
  printf '[INFO] Claude Code: start a new session, then try  /scientific-figure-suite  or  /fig:scope ...\n'
}

install_codex() {
  local home
  if [[ "${project}" -eq 1 ]]; then home="$(pwd)/.codex"; else home="${CODEX_HOME:-${HOME}/.codex}"; fi
  install_tree "${repo_root}/codex/skills/scientific-figure-suite" "${home}/skills/scientific-figure-suite"
  printf '[INFO] Codex: restart Codex or reload skills, then try  $scientific-figure-suite ...  or  fig-scope ...\n'
}

case "${platform}" in
  claude) install_claude ;;
  codex) install_codex ;;
  all) install_claude; install_codex ;;
esac
printf 'Python dependencies for the suite scripts: python -m pip install -r %s/requirements-dev.txt\n' "${repo_root}"
