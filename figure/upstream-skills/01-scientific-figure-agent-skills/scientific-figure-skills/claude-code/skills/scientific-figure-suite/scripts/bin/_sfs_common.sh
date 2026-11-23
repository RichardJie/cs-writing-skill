#!/usr/bin/env bash
set -Eeuo pipefail

sfs_script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
sfs_skill_dir="$(cd "${sfs_script_dir}/../.." && pwd)"
# The package root is the nearest ancestor that carries quick_validate.py
# (the platform package in a checkout). When the skill is installed on its own
# (for example under ~/.claude/skills or ~/.codex/skills), fall back to
# SFS_REPO_ROOT or the skill directory itself.
sfs_find_repo_root() {
  local dir="${sfs_skill_dir}"
  local i
  for i in 1 2 3; do
    dir="$(cd "${dir}/.." && pwd)"
    if [[ -f "${dir}/quick_validate.py" ]]; then
      printf '%s\n' "${dir}"
      return 0
    fi
  done
  return 1
}
if [[ -n "${SFS_REPO_ROOT:-}" ]]; then
  sfs_repo_root="$(cd "${SFS_REPO_ROOT}" && pwd)"
elif sfs_repo_root="$(sfs_find_repo_root)"; then
  :
else
  sfs_repo_root="${sfs_skill_dir}"
fi
if [[ -n "${PYTHON:-}" ]]; then
  sfs_python="${PYTHON}"
elif command -v python >/dev/null 2>&1; then
  sfs_python="python"
else
  sfs_python="python3"
fi
export PYTHONDONTWRITEBYTECODE="${PYTHONDONTWRITEBYTECODE:-1}"

sfs_fail() {
  printf '[FAIL] %s\n' "$*" >&2
  exit 1
}

sfs_require_python() {
  command -v "${sfs_python}" >/dev/null 2>&1 || sfs_fail "python not found: ${sfs_python}"
}

sfs_run_skill() {
  (cd "${sfs_skill_dir}" && "$@")
}

sfs_run_repo() {
  (cd "${sfs_repo_root}" && "$@")
}

sfs_assert_inside_repo() {
  local target
  target="$(cd "$1" && pwd)"
  case "${target}" in
    "${sfs_repo_root}"|"${sfs_repo_root}"/*) ;;
    *) sfs_fail "refusing path outside repository: ${target}" ;;
  esac
}
