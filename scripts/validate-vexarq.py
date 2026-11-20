"""Structural checks for the VEXARQ library. Not copied into consumer projects."""

from __future__ import annotations

import hashlib
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIB = ROOT / ".ai-vexarq"
CANON = {
    "sources/canon/backlog-hu-generator.md": "76a2db84caa6c1f80bab0532e8974d64c5ddaab7c8694ed1317f6e16bba691df",
    "sources/canon/archetype-prompt.xml": "619712fb444fd7f50ecc37634e7c3d3338b428b3dfe3b211070a4bfa75d03b8e",
}
failures: list[str] = []


def fail(message: str) -> None:
    failures.append(message)


def main() -> int:
    xml_files = list(LIB.rglob("*.xml"))
    for path in xml_files:
        try:
            ET.parse(path)
        except ET.ParseError as exc:
            fail(f"XML parse {path}: {exc}")
        text = path.read_text(encoding="utf-8")
        if "3.2.0" in text:
            fail(f"forbidden version in {path}")

    manifest = ET.parse(LIB / "manifest.xml")
    for module in manifest.findall(".//module"):
        relative = module.attrib.get("path", "")
        if not (LIB / relative).is_file():
            fail(f"manifest module missing: {relative}")

    for path in xml_files:
        tree = ET.parse(path)
        for node in tree.findall(".//referencia"):
            target = node.attrib.get("path")
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.is_file():
                fail(f"unresolved reference in {path.name}: {target}")

    for relative, expected in CANON.items():
        digest = hashlib.sha256((LIB / relative).read_bytes()).hexdigest()
        if digest != expected:
            fail(f"canon changed: {relative}")

    if failures:
        print("\n".join(failures))
        return 1
    print(f"OK xml={len(xml_files)} modules={len(manifest.findall('.//module'))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
