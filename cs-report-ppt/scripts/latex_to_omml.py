#!/usr/bin/env python3
r"""
latex_to_omml.py
Converts LaTeX math expressions into native Office Math Markup Language (OMML) XML.
Supports DrawingML 2010 OpenXML wrappers (<a14:m>) and direct PPTX in-place injection.

Usage:
    python3 latex_to_omml.py --latex "\frac{1}{N} \sum_{i=1}^N x_i"
    python3 latex_to_omml.py --latex "E = mc^2" --display
    python3 latex_to_omml.py --inject --input deck_stage1.pptx --output final_deck.pptx
"""

import os
import sys
import re
import zipfile
import shutil
import tempfile
import argparse
from typing import List, Tuple, Optional, Any, Union
import xml.etree.ElementTree as ET

# Namespaces
OMML_NS = "http://schemas.openxmlformats.org/officeDocument/2006/math"
A14_NS = "http://schemas.microsoft.com/office/drawing/2010/main"
A_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"
P_NS = "http://schemas.openxmlformats.org/presentationml/2006/main"
R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"

# Register namespaces so ET doesn't generate ns0, ns1 prefixes unnecessarily
ET.register_namespace("m", OMML_NS)
ET.register_namespace("a14", A14_NS)
ET.register_namespace("a", A_NS)
ET.register_namespace("p", P_NS)
ET.register_namespace("r", R_NS)


class LatexParsingError(Exception):
    """Exception raised when LaTeX parsing fails."""
    pass


# ============================================================================
# Unicode Symbol & Macro Dictionaries
# ============================================================================

GREEK_SYMBOLS = {
    r"\alpha": "α", r"\beta": "β", r"\gamma": "γ", r"\delta": "δ",
    r"\epsilon": "ε", r"\varepsilon": "ε", r"\zeta": "ζ", r"\eta": "η",
    r"\theta": "θ", r"\vartheta": "ϑ", r"\iota": "ι", r"\kappa": "κ",
    r"\lambda": "λ", r"\mu": "μ", r"\nu": "ν", r"\xi": "ξ",
    r"\pi": "π", r"\varpi": "ϖ", r"\rho": "ρ", r"\varrho": "ϱ",
    r"\sigma": "σ", r"\varsigma": "ς", r"\tau": "τ", r"\upsilon": "υ",
    r"\phi": "ϕ", r"\varphi": "φ", r"\chi": "χ", r"\psi": "ψ", r"\omega": "ω",
    r"\Gamma": "Γ", r"\Delta": "Δ", r"\Theta": "Θ", r"\Lambda": "Λ",
    r"\Xi": "Ξ", r"\Pi": "Π", r"\Sigma": "Σ", r"\Upsilon": "Υ",
    r"\Phi": "Φ", r"\Psi": "Ψ", r"\Omega": "Ω",
    r"\nabla": "∇", r"\partial": "∂"
}

RELATION_AND_OPERATOR_SYMBOLS = {
    r"\le": "≤", r"\leq": "≤", r"\ge": "≥", r"\geq": "≥",
    r"\neq": "≠", r"\ne": "≠", r"\approx": "≈", r"\sim": "∼",
    r"\simeq": "≃", r"\cong": "≅", r"\equiv": "≡", r"\propto": "∝",
    r"\in": "∈", r"\notin": "∉", r"\ni": "∋", r"\subset": "⊂",
    r"\subseteq": "⊆", r"\supset": "⊃", r"\supseteq": "⊇",
    r"\cup": "∪", r"\cap": "∩", r"\setminus": "∖",
    r"\times": "×", r"\cdot": "·", r"\pm": "±", r"\mp": "∓",
    r"\circ": "∘", r"\bullet": "•", r"\otimes": "⊗", r"\oplus": "⊕",
    r"\odot": "⊙", r"\star": "⋆", r"\ast": "∗",
    r"\to": "→", r"\rightarrow": "→", r"\leftarrow": "←",
    r"\Rightarrow": "⇒", r"\Leftarrow": "⇐", r"\leftrightarrow": "↔",
    r"\Leftrightarrow": "⇔", r"\mapsto": "↦",
    r"\infty": "∞", r"\forall": "∀", r"\exists": "∃", r"\nexists": "∄",
    r"\dots": "…", r"\ldots": "…", r"\cdots": "⋯", r"\vdots": "⋮", r"\ddots": "⋱",
    r"\perp": "⊥", r"\parallel": "∥", r"\angle": "∠",
    r"\top": "⊤", r"\bot": "⊥",
    r"\ll": "≪", r"\gg": "≫", r"\prime": "′", r"\hbar": "ℏ",
    r"\ell": "ℓ", r"\Re": "ℜ", r"\Im": "ℑ", r"\aleph": "ℵ", r"\emptyset": "∅",
    r"\mid": "|"
}

BLACKBOARD_BOLD = {
    "R": "ℝ", "E": "𝔼", "N": "ℕ", "Z": "ℤ", "C": "ℂ",
    "Q": "ℚ", "P": "ℙ", "H": "ℍ", "1": "𝟙", "0": "𝟘",
    "K": "𝕂", "F": "𝔽", "L": "𝕃", "M": "𝕄", "T": "𝕋",
    "X": "𝕏", "Y": "𝕐", "V": "𝕍", "W": "𝕎", "S": "𝕊",
    "A": "𝔸", "B": "𝔹", "D": "𝔻", "G": "𝔾", "I": "𝕀", "J": "𝕁", "U": "𝕌"
}

MATHCAL = {
    "A": "𝒜", "B": "ℬ", "C": "𝒞", "D": "𝒟", "E": "ℰ",
    "F": "ℱ", "G": "𝒢", "H": "ℋ", "I": "ℐ", "J": "𝒥",
    "K": "𝒦", "L": "ℒ", "M": "ℳ", "N": "𝒩", "O": "𝒪",
    "P": "𝒫", "Q": "𝒬", "R": "ℛ", "S": "𝒮", "T": "𝒯",
    "U": "𝒰", "V": "𝒱", "W": "𝒲", "X": "𝒳", "Y": "𝒴", "Z": "𝒵"
}

ACCENT_MAP = {
    r"\hat": "̂",
    r"\tilde": "̃",
    r"\bar": "̄",
    r"\vec": "⃗",
    r"\dot": "̇",
    r"\ddot": "̈",
    r"\acute": "́",
    r"\grave": "̀",
    r"\check": "̌",
    r"\breve": "̆"
}

NARY_MAP = {
    r"\sum": ("∑", "undOvr"),
    r"\prod": ("∏", "undOvr"),
    r"\coprod": ("∐", "undOvr"),
    r"\int": ("∫", "subSup"),
    r"\iint": ("∬", "subSup"),
    r"\iiint": ("∭", "subSup"),
    r"\oint": ("∮", "subSup"),
    r"\bigcup": ("⋃", "undOvr"),
    r"\bigcap": ("⋂", "undOvr"),
    r"\bigoplus": ("⨁", "undOvr"),
    r"\bigotimes": ("⨂", "undOvr"),
    r"\bigodot": ("⨀", "undOvr"),
    r"\bigsqcup": ("⨆", "undOvr")
}

SPACING_COMMANDS = {
    r"\quad": "  ",
    r"\qquad": "    ",
    r"\,": " ",
    r"\:": " ",
    r"\;": " ",
    r"\!": "",
    r"\ ": " ",
    r"~": " "
}

NAMED_FUNCTIONS = {
    r"\sin", r"\cos", r"\tan", r"\sec", r"\csc", r"\cot",
    r"\arcsin", r"\arccos", r"\arctan", r"\sinh", r"\cosh", r"\tanh",
    r"\ln", r"\log", r"\exp", r"\min", r"\max", r"\inf", r"\sup",
    r"\lim", r"\liminf", r"\limsup", r"\arg", r"\det", r"\dim",
    r"\gcd", r"\deg", r"\ker", r"\hom", r"\Pr", r"\argmin", r"\argmax"
}


# ============================================================================
# Tokenizer
# ============================================================================

class Token:
    def __init__(self, kind: str, value: str, pos: int):
        self.kind = kind
        self.value = value
        self.pos = pos

    def __repr__(self):
        return f"Token({self.kind}, {repr(self.value)})"


def tokenize(latex: str) -> List[Token]:
    tokens = []
    i = 0
    n = len(latex)

    while i < n:
        c = latex[i]

        if c.isspace():
            i += 1
            continue

        if c == '\\':
            if i + 1 < n and latex[i + 1] == '\\':
                tokens.append(Token("DBL_BSLASH", r"\\", i))
                i += 2
                continue
            if i + 1 < n and latex[i + 1] in r"{}_&%$# \:,;!|":
                cmd = latex[i:i + 2]
                tokens.append(Token("COMMAND", cmd, i))
                i += 2
                continue
            # Alpha command like \frac, \alpha
            match = re.match(r"\\[a-zA-Z]+", latex[i:])
            if match:
                cmd = match.group(0)
                tokens.append(Token("COMMAND", cmd, i))
                i += len(cmd)
                continue
            tokens.append(Token("CHAR", c, i))
            i += 1
            continue

        if c == '{':
            tokens.append(Token("OPEN_BRACE", "{", i))
            i += 1
        elif c == '}':
            tokens.append(Token("CLOSE_BRACE", "}", i))
            i += 1
        elif c == '[':
            tokens.append(Token("OPEN_BRACKET", "[", i))
            i += 1
        elif c == ']':
            tokens.append(Token("CLOSE_BRACKET", "]", i))
            i += 1
        elif c == '_':
            tokens.append(Token("SUB", "_", i))
            i += 1
        elif c == '^':
            tokens.append(Token("SUP", "^", i))
            i += 1
        elif c == '&':
            tokens.append(Token("AMP", "&", i))
            i += 1
        elif c == '~':
            tokens.append(Token("COMMAND", "~", i))
            i += 1
        elif c == "'":
            tokens.append(Token("CHAR", "′", i))
            i += 1
        else:
            tokens.append(Token("CHAR", c, i))
            i += 1

    tokens.append(Token("EOF", "", n))
    return tokens


# ============================================================================
# AST Nodes
# ============================================================================

class ASTNode:
    def to_omml(self) -> str:
        raise NotImplementedError


def escape_xml(text: str) -> str:
    """Escapes XML reserved characters strictly for text nodes."""
    return (
        text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&apos;")
    )


class MathRun(ASTNode):
    def __init__(self, text: str, bold: bool = False, script: Optional[str] = None, normal: bool = False):
        self.text = text
        self.bold = bold
        self.script = script
        self.normal = normal

    def to_omml(self) -> str:
        rpr = ""
        if self.bold:
            rpr += '<m:rPr><m:sty m:val="b"/></m:rPr>'
        elif self.script:
            rpr += f'<m:rPr><m:scr m:val="{self.script}"/></m:rPr>'
        elif self.normal:
            rpr += '<m:rPr><m:nor/></m:rPr>'

        safe = escape_xml(self.text)
        return f"<m:r>{rpr}<m:t>{safe}</m:t></m:r>"


def merge_runs(nodes: List[ASTNode]) -> List[ASTNode]:
    """Merges adjacent MathRun nodes with matching formatting attributes."""
    if not nodes:
        return []
    merged = []
    current_run: Optional[MathRun] = None

    for node in nodes:
        if isinstance(node, MathRun):
            if current_run is not None and (
                current_run.bold == node.bold and
                current_run.script == node.script and
                current_run.normal == node.normal
            ):
                current_run.text += node.text
            else:
                if current_run is not None:
                    merged.append(current_run)
                current_run = MathRun(node.text, bold=node.bold, script=node.script, normal=node.normal)
        else:
            if current_run is not None:
                merged.append(current_run)
                current_run = None
            merged.append(node)

    if current_run is not None:
        merged.append(current_run)

    return merged


class Fraction(ASTNode):
    def __init__(self, num: ASTNode, den: ASTNode):
        self.num = num
        self.den = den

    def to_omml(self) -> str:
        return (
            "<m:f>"
            '<m:fPr><m:type m:val="bar"/></m:fPr>'
            f"<m:num>{self.num.to_omml()}</m:num>"
            f"<m:den>{self.den.to_omml()}</m:den>"
            "</m:f>"
        )


class Subscript(ASTNode):
    def __init__(self, base: ASTNode, sub: ASTNode):
        self.base = base
        self.sub = sub

    def to_omml(self) -> str:
        return (
            "<m:sSub>"
            f"<m:e>{self.base.to_omml()}</m:e>"
            f"<m:sub>{self.sub.to_omml()}</m:sub>"
            "</m:sSub>"
        )


class Superscript(ASTNode):
    def __init__(self, base: ASTNode, sup: ASTNode):
        self.base = base
        self.sup = sup

    def to_omml(self) -> str:
        return (
            "<m:sSup>"
            f"<m:e>{self.base.to_omml()}</m:e>"
            f"<m:sup>{self.sup.to_omml()}</m:sup>"
            "</m:sSup>"
        )


class SubSuperscript(ASTNode):
    def __init__(self, base: ASTNode, sub: ASTNode, sup: ASTNode):
        self.base = base
        self.sub = sub
        self.sup = sup

    def to_omml(self) -> str:
        return (
            "<m:sSubSup>"
            f"<m:e>{self.base.to_omml()}</m:e>"
            f"<m:sub>{self.sub.to_omml()}</m:sub>"
            f"<m:sup>{self.sup.to_omml()}</m:sup>"
            "</m:sSubSup>"
        )


class NaryOp(ASTNode):
    def __init__(self, chr_val: str, lim_loc: str, sub: Optional[ASTNode] = None, sup: Optional[ASTNode] = None, body: Optional[ASTNode] = None):
        self.chr_val = chr_val
        self.lim_loc = lim_loc
        self.sub = sub
        self.sup = sup
        self.body = body

    def to_omml(self) -> str:
        safe_chr = escape_xml(self.chr_val)
        pr_items = [f'<m:chr m:val="{safe_chr}"/>', f'<m:limLoc m:val="{self.lim_loc}"/>']
        if self.sub is None:
            pr_items.append('<m:subHide m:val="1"/>')
        if self.sup is None:
            pr_items.append('<m:supHide m:val="1"/>')

        sub_xml = f"<m:sub>{self.sub.to_omml()}</m:sub>" if self.sub else "<m:sub/>"
        sup_xml = f"<m:sup>{self.sup.to_omml()}</m:sup>" if self.sup else "<m:sup/>"
        body_xml = f"<m:e>{self.body.to_omml()}</m:e>" if self.body else ""

        return (
            "<m:nary>"
            f"<m:naryPr>{''.join(pr_items)}</m:naryPr>"
            f"{sub_xml}"
            f"{sup_xml}"
            f"{body_xml}"
            "</m:nary>"
        )


class Delimiter(ASTNode):
    def __init__(self, beg_chr: str, end_chr: str, body: ASTNode):
        self.beg_chr = beg_chr
        self.end_chr = end_chr
        self.body = body

    def to_omml(self) -> str:
        safe_beg = escape_xml(self.beg_chr)
        safe_end = escape_xml(self.end_chr)
        return (
            "<m:d>"
            f'<m:dPr><m:begChr m:val="{safe_beg}"/><m:endChr m:val="{safe_end}"/><m:grow m:val="1"/></m:dPr>'
            f"<m:e>{self.body.to_omml()}</m:e>"
            "</m:d>"
        )


class Radical(ASTNode):
    def __init__(self, body: ASTNode, deg: Optional[ASTNode] = None):
        self.body = body
        self.deg = deg

    def to_omml(self) -> str:
        if self.deg is None:
            return (
                "<m:rad>"
                '<m:radPr><m:degHide m:val="1"/></m:radPr>'
                "<m:deg/>"
                f"<m:e>{self.body.to_omml()}</m:e>"
                "</m:rad>"
            )
        else:
            return (
                "<m:rad>"
                "<m:radPr/>"
                f"<m:deg>{self.deg.to_omml()}</m:deg>"
                f"<m:e>{self.body.to_omml()}</m:e>"
                "</m:rad>"
            )


class Accent(ASTNode):
    def __init__(self, chr_val: str, body: ASTNode):
        self.chr_val = chr_val
        self.body = body

    def to_omml(self) -> str:
        safe_chr = escape_xml(self.chr_val)
        return (
            "<m:acc>"
            f'<m:accPr><m:chr m:val="{safe_chr}"/></m:accPr>'
            f"<m:e>{self.body.to_omml()}</m:e>"
            "</m:acc>"
        )


class Matrix(ASTNode):
    def __init__(self, rows: List[List[ASTNode]]):
        self.rows = rows

    def to_omml(self) -> str:
        rows_xml = []
        for row in self.rows:
            elem_xml = "".join(f"<m:e>{cell.to_omml()}</m:e>" for cell in row)
            rows_xml.append(f"<m:mr>{elem_xml}</m:mr>")
        inner = "".join(rows_xml)
        return f'<m:m><m:mPr><m:baseJc m:val="center"/></m:mPr>{inner}</m:m>'


class NodeList(ASTNode):
    def __init__(self, nodes: List[ASTNode]):
        self.nodes = merge_runs(nodes)

    def to_omml(self) -> str:
        return "".join(node.to_omml() for node in self.nodes)


# ============================================================================
# Recursive Descent Parser
# ============================================================================

class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0

    def peek(self) -> Token:
        return self.tokens[self.pos]

    def advance(self) -> Token:
        tok = self.tokens[self.pos]
        if self.pos < len(self.tokens) - 1:
            self.pos += 1
        return tok

    def match(self, kind: str, value: Optional[str] = None) -> bool:
        tok = self.peek()
        if tok.kind == kind:
            if value is None or tok.value == value:
                self.advance()
                return True
        return False

    def expect(self, kind: str, value: Optional[str] = None) -> Token:
        tok = self.peek()
        if tok.kind != kind or (value is not None and tok.value != value):
            raise LatexParsingError(f"Expected {kind} {value or ''} at position {tok.pos}, found {tok}")
        return self.advance()

    def parse(self) -> ASTNode:
        nodes = []
        while self.peek().kind != "EOF":
            prev_pos = self.pos
            node = self.parse_primary_or_subsup()
            if node is not None:
                nodes.append(node)
            elif self.pos == prev_pos:
                self.advance()
            if self.pos == prev_pos:
                self.advance()
        if len(nodes) == 1:
            return nodes[0]
        return NodeList(nodes)

    def parse_sequence(self, stop_tokens: Tuple[str, ...]) -> ASTNode:
        nodes = []
        while self.peek().kind != "EOF" and self.peek().kind not in stop_tokens:
            if self.peek().kind == "COMMAND" and self.peek().value in stop_tokens:
                break
            prev_pos = self.pos
            node = self.parse_primary_or_subsup()
            if node is not None:
                nodes.append(node)
            elif self.pos == prev_pos:
                self.advance()
            if self.pos == prev_pos:
                self.advance()
        if len(nodes) == 1:
            return nodes[0]
        return NodeList(nodes)

    def parse_group_or_single(self) -> ASTNode:
        """Parses {group} or a single token argument."""
        if self.match("OPEN_BRACE"):
            node = self.parse_sequence(("CLOSE_BRACE",))
            self.match("CLOSE_BRACE")
            return node
        else:
            return self.parse_atom()

    def parse_primary_or_subsup(self) -> ASTNode:
        atom = self.parse_atom()
        if atom is None:
            return None

        # Check for subscript and/or superscript
        sub = None
        sup = None

        while True:
            if self.peek().kind == "SUB" and sub is None:
                self.advance()
                sub = self.parse_group_or_single()
            elif self.peek().kind == "SUP" and sup is None:
                self.advance()
                sup = self.parse_group_or_single()
            else:
                break

        if sub is not None and sup is not None:
            return SubSuperscript(atom, sub, sup)
        elif sub is not None:
            return Subscript(atom, sub)
        elif sup is not None:
            return Superscript(atom, sup)
        return atom

    def parse_atom(self) -> ASTNode:
        tok = self.peek()

        if tok.kind == "EOF":
            return MathRun("")

        # Braces
        if tok.kind == "OPEN_BRACE":
            self.advance()
            node = self.parse_sequence(("CLOSE_BRACE",))
            self.match("CLOSE_BRACE")
            return node

        # Open Bracket [ ... ]
        if tok.kind == "OPEN_BRACKET":
            self.advance()
            body = self.parse_sequence(("CLOSE_BRACKET",))
            self.match("CLOSE_BRACKET")
            return Delimiter("[", "]", body)

        # Delimiters in standard parens ( ... )
        if tok.kind == "CHAR" and tok.value == "(":
            self.advance()
            body = self.parse_sequence_until_char(")")
            self.match("CHAR", ")")
            return Delimiter("(", ")", body)

        # Ampersand & outside matrix
        if tok.kind == "AMP":
            self.advance()
            return MathRun("&")

        # Double Backslash \\ outside matrix
        if tok.kind == "DBL_BSLASH":
            self.advance()
            return MathRun(" ")

        # Delimiters and sub/sup tokens appearing unexpectedly
        if tok.kind == "CLOSE_BRACE":
            self.advance()
            return MathRun("}")

        if tok.kind == "CLOSE_BRACKET":
            self.advance()
            return MathRun("]")

        if tok.kind == "SUB":
            self.advance()
            return MathRun("_")

        if tok.kind == "SUP":
            self.advance()
            return MathRun("^")

        # Characters
        if tok.kind == "CHAR":
            self.advance()
            val = tok.value
            return MathRun(val)

        # Commands
        if tok.kind == "COMMAND":
            cmd = tok.value
            self.advance()

            # Fractions
            if cmd in (r"\frac", r"\tfrac", r"\dfrac"):
                num = self.parse_group_or_single()
                den = self.parse_group_or_single()
                return Fraction(num, den)

            # Radicals
            if cmd == r"\sqrt":
                deg = None
                if self.match("OPEN_BRACKET"):
                    deg = self.parse_sequence(("CLOSE_BRACKET",))
                    self.match("CLOSE_BRACKET")
                body = self.parse_group_or_single()
                return Radical(body, deg)

            # N-ary Operators (\sum, \prod, \int, ...)
            if cmd in NARY_MAP:
                chr_val, lim_loc = NARY_MAP[cmd]
                sub = None
                sup = None
                while True:
                    if self.peek().kind == "COMMAND" and self.peek().value in (r"\limits", r"\nolimits"):
                        lim_cmd = self.advance().value
                        if lim_cmd == r"\limits":
                            lim_loc = "undOvr"
                        else:
                            lim_loc = "subSup"
                    elif self.peek().kind == "SUB" and sub is None:
                        self.advance()
                        sub = self.parse_group_or_single()
                    elif self.peek().kind == "SUP" and sup is None:
                        self.advance()
                        sup = self.parse_group_or_single()
                    else:
                        break
                return NaryOp(chr_val, lim_loc, sub, sup, None)

            # Delimiters (\left ... \right)
            if cmd == r"\left":
                left_delim = self.parse_delim_char()
                body = self.parse_sequence_until_command(r"\right")
                self.match("COMMAND", r"\right")
                right_delim = self.parse_delim_char()
                return Delimiter(left_delim, right_delim, body)

            # Accents (\hat, \tilde, \bar, \vec, \dot, \ddot)
            if cmd in ACCENT_MAP:
                acc_chr = ACCENT_MAP[cmd]
                body = self.parse_group_or_single()
                return Accent(acc_chr, body)

            # Blackboard Bold (\mathbb)
            if cmd in (r"\mathbb", r"\mathbfbb"):
                text_content = self.extract_text_argument()
                mapped = "".join(BLACKBOARD_BOLD.get(ch, ch) for ch in text_content)
                return MathRun(mapped)

            # MathCal (\mathcal)
            if cmd in (r"\mathcal", r"\mathscr"):
                text_content = self.extract_text_argument()
                mapped = "".join(MATHCAL.get(ch, ch) for ch in text_content)
                return MathRun(mapped)

            # Bold Vectors (\mathbf, \boldsymbol, \bm, \pmb)
            if cmd in (r"\mathbf", r"\boldsymbol", r"\bm", r"\pmb"):
                body = self.parse_group_or_single()
                return self.apply_bold(body)

            # Text / Roman / Normal font (\text, \mathrm, \operatorname)
            if cmd in (r"\text", r"\mathrm", r"\operatorname", r"\operatorname*", r"\mathit", r"\mathsf", r"\mathtt", r"\mbox"):
                text_content = self.extract_text_argument()
                return MathRun(text_content, normal=True)

            # Greek symbols
            if cmd in GREEK_SYMBOLS:
                return MathRun(GREEK_SYMBOLS[cmd])

            # Relations and Operators
            if cmd in RELATION_AND_OPERATOR_SYMBOLS:
                return MathRun(RELATION_AND_OPERATOR_SYMBOLS[cmd])

            # Spacing
            if cmd in SPACING_COMMANDS:
                return MathRun(SPACING_COMMANDS[cmd])

            # Named Functions (\sin, \cos, \log, etc.)
            if cmd in NAMED_FUNCTIONS:
                name = cmd.lstrip("\\")
                return MathRun(name, normal=True)

            # Delimiter symbols as commands (\{, \}, \|, \langle, \rangle)
            if cmd == r"\{":
                return MathRun("{")
            if cmd == r"\}":
                return MathRun("}")
            if cmd in (r"\|", r"\|"):
                return MathRun("‖")
            if cmd == r"\langle":
                return MathRun("⟨")
            if cmd == r"\rangle":
                return MathRun("⟩")
            if cmd == r"\%":
                return MathRun("%")
            if cmd == r"\&":
                return MathRun("&")
            if cmd == r"\_":
                return MathRun("_")

            # Environment (\begin{matrix}, \begin{bmatrix}, etc.)
            if cmd == r"\begin":
                env_name = self.extract_text_argument().strip()
                matrix_node = self.parse_matrix_env(env_name)
                return matrix_node

            # Default fallback for unknown commands
            clean_cmd = cmd.lstrip("\\")
            return MathRun(clean_cmd)

        # Fallback: advance unknown token to ensure progress
        tok = self.advance()
        return MathRun(tok.value if tok.value else "")

    def extract_text_argument(self) -> str:
        """Extracts plain text inside {arg} or next token."""
        if self.match("OPEN_BRACE"):
            text_parts = []
            brace_depth = 1
            while self.peek().kind != "EOF" and brace_depth > 0:
                tok = self.peek()
                if tok.kind == "OPEN_BRACE":
                    brace_depth += 1
                    text_parts.append(tok.value)
                    self.advance()
                elif tok.kind == "CLOSE_BRACE":
                    brace_depth -= 1
                    if brace_depth > 0:
                        text_parts.append(tok.value)
                    self.advance()
                else:
                    if tok.kind == "COMMAND" and tok.value in GREEK_SYMBOLS:
                        text_parts.append(GREEK_SYMBOLS[tok.value])
                    elif tok.kind == "COMMAND" and tok.value in RELATION_AND_OPERATOR_SYMBOLS:
                        text_parts.append(RELATION_AND_OPERATOR_SYMBOLS[tok.value])
                    elif tok.kind == "COMMAND":
                        text_parts.append(tok.value.lstrip("\\"))
                    else:
                        text_parts.append(tok.value)
                    self.advance()
            return "".join(text_parts)
        else:
            tok = self.advance()
            if tok.kind == "COMMAND" and tok.value in GREEK_SYMBOLS:
                return GREEK_SYMBOLS[tok.value]
            elif tok.kind == "COMMAND":
                return tok.value.lstrip("\\")
            return tok.value

    def parse_delim_char(self) -> str:
        tok = self.peek()
        if tok.kind == "CHAR":
            self.advance()
            return tok.value
        elif tok.kind == "OPEN_BRACKET":
            self.advance()
            return "["
        elif tok.kind == "CLOSE_BRACKET":
            self.advance()
            return "]"
        elif tok.kind == "OPEN_BRACE":
            self.advance()
            return "{"
        elif tok.kind == "CLOSE_BRACE":
            self.advance()
            return "}"
        elif tok.kind == "COMMAND":
            cmd = tok.value
            self.advance()
            if cmd == r"\{":
                return "{"
            if cmd == r"\}":
                return "}"
            if cmd in (r"\|", r"\|"):
                return "‖"
            if cmd == r"\langle":
                return "⟨"
            if cmd == r"\rangle":
                return "⟩"
            if cmd == r"\lfloor":
                return "⌊"
            if cmd == r"\rfloor":
                return "⌋"
            if cmd == r"\lceil":
                return "⌈"
            if cmd == r"\rceil":
                return "⌉"
            if cmd == r".":
                return ""
            return cmd.lstrip("\\")
        if tok.kind != "EOF":
            self.advance()
            return tok.value
        return ""

    def parse_sequence_until_command(self, end_cmd: str) -> ASTNode:
        nodes = []
        while self.peek().kind != "EOF":
            if self.peek().kind == "COMMAND" and self.peek().value == end_cmd:
                break
            prev_pos = self.pos
            node = self.parse_primary_or_subsup()
            if node is not None:
                nodes.append(node)
            elif self.pos == prev_pos:
                self.advance()
            if self.pos == prev_pos:
                self.advance()
        if len(nodes) == 1:
            return nodes[0]
        return NodeList(nodes)

    def parse_sequence_until_char(self, end_char: str) -> ASTNode:
        nodes = []
        while self.peek().kind != "EOF":
            if self.peek().kind == "CHAR" and self.peek().value == end_char:
                break
            prev_pos = self.pos
            node = self.parse_primary_or_subsup()
            if node is not None:
                nodes.append(node)
            elif self.pos == prev_pos:
                self.advance()
            if self.pos == prev_pos:
                self.advance()
        if len(nodes) == 1:
            return nodes[0]
        return NodeList(nodes)

    def parse_matrix_env(self, env_name: str) -> ASTNode:
        rows: List[List[ASTNode]] = []
        current_row: List[ASTNode] = []
        current_cell_nodes: List[ASTNode] = []

        def flush_cell():
            if len(current_cell_nodes) == 1:
                current_row.append(current_cell_nodes[0])
            elif len(current_cell_nodes) > 1:
                current_row.append(NodeList(list(current_cell_nodes)))
            else:
                current_row.append(MathRun(""))
            current_cell_nodes.clear()

        def flush_row():
            flush_cell()
            if current_row:
                rows.append(list(current_row))
                current_row.clear()

        while self.peek().kind != "EOF":
            if self.peek().kind == "COMMAND" and self.peek().value == r"\end":
                self.advance()
                end_env = self.extract_text_argument().strip()
                if end_env == env_name:
                    break
                else:
                    raise LatexParsingError(f"Mismatched environment end: expected {env_name}, got {end_env}")

            if self.peek().kind == "AMP":
                self.advance()
                flush_cell()
                continue

            if self.peek().kind == "DBL_BSLASH":
                self.advance()
                flush_row()
                continue

            prev_pos = self.pos
            node = self.parse_primary_or_subsup()
            if node is not None:
                current_cell_nodes.append(node)
            elif self.pos == prev_pos:
                self.advance()
            if self.pos == prev_pos:
                self.advance()

        flush_row()
        matrix_node = Matrix(rows)

        # Add enclosing delimiters based on matrix flavor
        if env_name == "bmatrix":
            return Delimiter("[", "]", matrix_node)
        elif env_name in ("pmatrix", "matrix*"):
            return Delimiter("(", ")", matrix_node)
        elif env_name == "vmatrix":
            return Delimiter("|", "|", matrix_node)
        elif env_name == "Vmatrix":
            return Delimiter("‖", "‖", matrix_node)
        elif env_name == "Bmatrix":
            return Delimiter("{", "}", matrix_node)
        return matrix_node

    def apply_bold(self, node: ASTNode) -> ASTNode:
        if isinstance(node, MathRun):
            return MathRun(node.text, bold=True, script=node.script, normal=node.normal)
        elif isinstance(node, NodeList):
            return NodeList([self.apply_bold(n) for n in node.nodes])
        elif isinstance(node, Subscript):
            return Subscript(self.apply_bold(node.base), node.sub)
        elif isinstance(node, Superscript):
            return Superscript(self.apply_bold(node.base), node.sup)
        elif isinstance(node, SubSuperscript):
            return SubSuperscript(self.apply_bold(node.base), node.sub, node.sup)
        return node


# ============================================================================
# Main Converter API
# ============================================================================

def latex_to_omml(latex: str, display_mode: bool = False, wrap_drawingml: bool = True) -> str:
    r"""
    Converts a LaTeX math expression into Office Math Markup Language (OMML) XML.

    Args:
        latex: Raw LaTeX string (e.g. "\\frac{1}{N} \\sum_{i=1}^N x_i")
        display_mode: True for block/centered math (<m:oMathPara>), False for inline math (<m:oMath>)
        wrap_drawingml: True to wrap in PowerPoint DrawingML tag (<a14:m>)

    Returns:
        XML string representation of the formula.
    """
    latex_clean = latex.strip()
    if not latex_clean:
        raise ValueError("LaTeX math expression cannot be empty.")

    # Remove outer math delimiters if present: $...$, $...$, \(...\), \[...\]
    if (latex_clean.startswith("$$") and latex_clean.endswith("$$")) or (latex_clean.startswith("\\[") and latex_clean.endswith("\\]")):
        latex_clean = latex_clean[2:-2].strip()
        display_mode = True
    elif (latex_clean.startswith("$") and latex_clean.endswith("$")) or (latex_clean.startswith("\\(") and latex_clean.endswith("\\)")):
        latex_clean = latex_clean[1:-1].strip() if latex_clean.startswith("$") else latex_clean[2:-2].strip()

    try:
        tokens = tokenize(latex_clean)
        parser = Parser(tokens)
        ast = parser.parse()
        omml_body = ast.to_omml()
    except Exception as e:
        # Graceful fallback: render escaped text run
        safe_fallback = escape_xml(latex_clean)
        omml_body = f"<m:r><m:t>{safe_fallback}</m:t></m:r>"

    # Build XML hierarchy
    if display_mode:
        omml_xml = (
            f'<m:oMathPara xmlns:m="{OMML_NS}">'
            f"<m:oMath>{omml_body}</m:oMath>"
            "</m:oMathPara>"
        )
    else:
        omml_xml = f'<m:oMath xmlns:m="{OMML_NS}">{omml_body}</m:oMath>'

    if wrap_drawingml:
        return f'<a14:m xmlns:a14="{A14_NS}" xmlns:m="{OMML_NS}">{omml_xml}</a14:m>'
    return omml_xml


# ============================================================================
# PPTX In-Place Injection
# ============================================================================

MATH_PLACEHOLDER_REGEX = re.compile(
    r"(\{\{MATH(?:_(?:DISPLAY|INLINE))?:\s*(.*?)\s*\}\}|\[\[MATH(?:_(?:DISPLAY|INLINE))?:\s*(.*?)\s*\]\]|<<MATH(?:_(?:DISPLAY|INLINE))?:\s*(.*?)\s*>>)",
    re.DOTALL
)


def _process_slide_xml(xml_bytes: bytes) -> bytes:
    """
    Processes a single slide XML file, replacing math placeholder runs with <a14:m> nodes.
    """
    xml_str = xml_bytes.decode("utf-8")
    if "MATH" not in xml_str:
        return xml_bytes

    try:
        root = ET.fromstring(xml_bytes)
    except ET.ParseError:
        return xml_bytes

    # Find all paragraph elements: <a:p>
    paragraphs = root.findall(f".//{{{A_NS}}}p")
    modified = False

    for p in paragraphs:
        # Check if any child run contains math placeholders
        runs = list(p)
        for child_idx, child in enumerate(runs):
            if child.tag == f"{{{A_NS}}}r":
                t_elem = child.find(f"{{{A_NS}}}t")
                if t_elem is not None and t_elem.text:
                    text_content = t_elem.text
                    matches = list(MATH_PLACEHOLDER_REGEX.finditer(text_content))
                    if not matches:
                        continue

                    # We have math placeholders in this text run!
                    modified = True
                    parent = p

                    # Remove the original <a:r> run
                    p_index = list(parent).index(child)
                    parent.remove(child)

                    # Split text and insert runs / math nodes
                    last_idx = 0
                    insert_offset = 0

                    for m in matches:
                        start, end = m.span()
                        full_tag = m.group(1)
                        latex_expr = next((g for g in [m.group(2), m.group(3), m.group(4)] if g is not None), "")
                        is_display = "DISPLAY" in full_tag or "INLINE" not in full_tag

                        # Preceding text
                        if start > last_idx:
                            pre_text = text_content[last_idx:start]
                            pre_r = ET.Element(f"{{{A_NS}}}r")
                            # Copy formatting properties if present
                            orig_rpr = child.find(f"{{{A_NS}}}rPr")
                            if orig_rpr is not None:
                                pre_r.append(ET.fromstring(ET.tostring(orig_rpr)))
                            pre_t = ET.SubElement(pre_r, f"{{{A_NS}}}t")
                            pre_t.text = pre_text
                            parent.insert(p_index + insert_offset, pre_r)
                            insert_offset += 1

                        # Generate OMML XML
                        omml_snippet = latex_to_omml(latex_expr, display_mode=is_display, wrap_drawingml=True)
                        try:
                            math_elem = ET.fromstring(omml_snippet)
                            parent.insert(p_index + insert_offset, math_elem)
                            insert_offset += 1
                        except ET.ParseError:
                            # If parsing snippet fails, put as text
                            err_r = ET.Element(f"{{{A_NS}}}r")
                            err_t = ET.SubElement(err_r, f"{{{A_NS}}}t")
                            err_t.text = latex_expr
                            parent.insert(p_index + insert_offset, err_r)
                            insert_offset += 1

                        last_idx = end

                    # Trailing text
                    if last_idx < len(text_content):
                        post_text = text_content[last_idx:]
                        post_r = ET.Element(f"{{{A_NS}}}r")
                        orig_rpr = child.find(f"{{{A_NS}}}rPr")
                        if orig_rpr is not None:
                            post_r.append(ET.fromstring(ET.tostring(orig_rpr)))
                        post_t = ET.SubElement(post_r, f"{{{A_NS}}}t")
                        post_t.text = post_text
                        parent.insert(p_index + insert_offset, post_r)
                        insert_offset += 1

    if modified:
        return ET.tostring(root, encoding="utf-8", xml_declaration=True)
    return xml_bytes


def inject_omml_into_pptx(pptx_path: str, output_path: str) -> None:
    """
    Unpacks PPTX, locates all {{MATH:...}} / [[MATH:...]] placeholders in slide XML files,
    replaces text runs with native <a14:m> elements, ensures namespaces, and repacks into output_path.

    Args:
        pptx_path: Source .pptx file path.
        output_path: Destination .pptx file path.
    """
    if not os.path.exists(pptx_path):
        raise FileNotFoundError(f"Input PPTX file not found: {pptx_path}")

    temp_dir = tempfile.mkdtemp(prefix="omml_inject_")
    try:
        with zipfile.ZipFile(pptx_path, "r") as zip_in:
            zip_in.extractall(temp_dir)

        slides_dir = os.path.join(temp_dir, "ppt", "slides")
        if os.path.exists(slides_dir):
            for fname in os.listdir(slides_dir):
                if fname.startswith("slide") and fname.endswith(".xml"):
                    slide_path = os.path.join(slides_dir, fname)
                    with open(slide_path, "rb") as f:
                        content = f.read()
                    processed_content = _process_slide_xml(content)
                    with open(slide_path, "wb") as f:
                        f.write(processed_content)

        out_dir = os.path.dirname(os.path.abspath(output_path))
        if out_dir:
            os.makedirs(out_dir, exist_ok=True)

        with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as zip_out:
            for root_dir, _, files in os.walk(temp_dir):
                for file in files:
                    full_path = os.path.join(root_dir, file)
                    rel_path = os.path.relpath(full_path, temp_dir)
                    zip_out.write(full_path, rel_path)

    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)


# ============================================================================
# CLI Interface
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Convert LaTeX math expressions to OMML DrawingML XML or inject into PPTX."
    )
    parser.add_argument("--latex", type=str, help="LaTeX math expression to convert")
    parser.add_argument("--display", action="store_true", help="Format as display/block math (<m:oMathPara>)")
    parser.add_argument("--no-wrap", action="store_true", help="Do not wrap in DrawingML <a14:m> wrapper")
    parser.add_argument("--inject", action="store_true", help="Run PPTX post-processing injection mode")
    parser.add_argument("--input", type=str, help="Input PPTX path for --inject mode")
    parser.add_argument("--output", type=str, help="Output PPTX path for --inject mode")

    args = parser.parse_args()

    if args.inject:
        if not args.input or not args.output:
            print("Error: --inject requires both --input and --output paths.", file=sys.stderr)
            sys.exit(1)
        try:
            inject_omml_into_pptx(args.input, args.output)
            print(f"Successfully injected OMML into presentation: {args.output}")
            sys.exit(0)
        except Exception as e:
            print(f"Error during PPTX OMML injection: {e}", file=sys.stderr)
            sys.exit(1)

    if args.latex:
        try:
            omml_out = latex_to_omml(
                args.latex,
                display_mode=args.display,
                wrap_drawingml=not args.no_wrap
            )
            print(omml_out)
            sys.exit(0)
        except Exception as e:
            print(f"Error converting LaTeX to OMML: {e}", file=sys.stderr)
            sys.exit(1)

    parser.print_help()
    sys.exit(1)


if __name__ == "__main__":
    main()
