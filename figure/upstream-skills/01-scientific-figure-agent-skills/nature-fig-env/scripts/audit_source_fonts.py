"""Statically flag explicit Python font settings below the skill minimum."""

from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path


FONT_KEYS = {
    "font.size",
    "axes.labelsize",
    "axes.titlesize",
    "xtick.labelsize",
    "ytick.labelsize",
    "legend.fontsize",
}


def numeric_value(node: ast.AST) -> float | None:
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return float(node.value)
    return None


def string_value(node: ast.AST) -> str | None:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    return None


class FontVisitor(ast.NodeVisitor):
    def __init__(self, minimum_pt: float) -> None:
        self.minimum_pt = minimum_pt
        self.findings: list[dict[str, object]] = []

    def add(self, node: ast.AST, value: float, setting: str) -> None:
        if value < self.minimum_pt:
            self.findings.append(
                {
                    "rule_id": "FONT-01",
                    "line": getattr(node, "lineno", None),
                    "setting": setting,
                    "value_pt": value,
                    "minimum_pt": self.minimum_pt,
                    "message": f"explicit {setting}={value:g} pt is below {self.minimum_pt:g} pt",
                }
            )

    def visit_Call(self, node: ast.Call) -> None:
        for keyword in node.keywords:
            if keyword.arg == "fontsize":
                value = numeric_value(keyword.value)
                if value is not None:
                    self.add(keyword, value, "fontsize")
        self.generic_visit(node)

    def visit_Dict(self, node: ast.Dict) -> None:
        for key_node, value_node in zip(node.keys, node.values):
            if key_node is None:
                continue
            key = string_value(key_node)
            value = numeric_value(value_node)
            if key in FONT_KEYS and value is not None:
                self.add(value_node, value, key)
        self.generic_visit(node)

    def visit_Assign(self, node: ast.Assign) -> None:
        value = numeric_value(node.value)
        if value is not None:
            for target in node.targets:
                if isinstance(target, ast.Subscript):
                    key = string_value(target.slice)
                    if key in FONT_KEYS:
                        self.add(node, value, key)
        self.generic_visit(node)


def audit_file(path: Path, minimum_pt: float) -> list[dict[str, object]]:
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except (OSError, SyntaxError, UnicodeDecodeError) as exc:
        return [{"rule_id": "FILE-02", "file": str(path), "line": None, "message": str(exc)}]
    visitor = FontVisitor(minimum_pt)
    visitor.visit(tree)
    for finding in visitor.findings:
        finding["file"] = str(path)
    return visitor.findings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    parser.add_argument("--minimum-pt", type=float, default=13.0)
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()
    files = [args.path] if args.path.is_file() else sorted(args.path.rglob("*.py"))
    findings = [item for path in files for item in audit_file(path, args.minimum_pt)]
    if args.format == "json":
        print(json.dumps({"status": "FAIL" if findings else "PASS", "findings": findings}, indent=2))
    elif findings:
        print("SOURCE FONT AUDIT FAILED")
        for item in findings:
            print(f"- [{item['rule_id']}] {item['file']}:{item['line']}: {item['message']}")
    else:
        print(f"SOURCE FONT AUDIT PASSED: no explicit font setting below {args.minimum_pt:g} pt.")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
