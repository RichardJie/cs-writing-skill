"""Hold the per-user Illustrator execution lock until the MCP releases stdin."""
import fcntl
import os
from pathlib import Path
import sys


def main():
    lock_path = Path("/private/tmp") / f"codex-illustrator-execution-{os.getuid()}.lock"
    fd = os.open(lock_path, os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW, 0o600)
    try:
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print("ILLUSTRATOR_BUSY: another MCP operation is running", file=sys.stderr)
            return 75
        print("locked", flush=True)
        sys.stdin.buffer.read()
        return 0
    finally:
        os.close(fd)


if __name__ == "__main__":
    raise SystemExit(main())
