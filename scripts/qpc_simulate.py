"""Exercise the 3.1.0 recovery rule against a fixture command. Not a product test runner."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAX_ATTEMPTS = 3


def run_gate(command: list[str], workdir: Path) -> int:
    completed = subprocess.run(command, cwd=workdir, capture_output=True, text=True)
    return completed.returncode


def recover(command: list[str], workdir: Path, sha: str) -> str:
    attempts = []
    for attempt in range(1, MAX_ATTEMPTS + 1):
        code = run_gate(command, workdir)
        attempts.append(code)
        if code == 0:
            return f"PASSED sha={sha} attempts={attempts}"
    return f"BLOCKED sha={sha} attempts={attempts}"


def reject_stale(previous_sha: str, final_sha: str) -> str:
    if previous_sha != final_sha:
        return "REJECTED stale green result"
    return "ACCEPTED"


def main() -> int:
    node = ROOT / "tests" / "fixtures" / "qpc-node"
    python_dir = ROOT / "tests" / "fixtures" / "qpc-python"
    node_result = recover(["node", "fail.js"], node, "fixture-node")
    python_result = recover([sys.executable, "fail.py"], python_dir, "fixture-python")
    stale = reject_stale("old", "new")
    print(node_result)
    print(python_result)
    print(stale)
    expected = (
        node_result.startswith("BLOCKED")
        and python_result.startswith("BLOCKED")
        and stale == "REJECTED stale green result"
    )
    return 0 if expected else 1


if __name__ == "__main__":
    sys.exit(main())
