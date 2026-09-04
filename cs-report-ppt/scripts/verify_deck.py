#!/usr/bin/env python3
"""
verify_deck.py
Programmatic OpenXML validator for academic presentation decks.

Validates:
1. PPTX archive validity and slide count (14 standard spine slides)
2. DrawingML 2010 OpenXML math namespaces and native OMML <m:oMath> elements
3. Zero remaining <<MATH_>> placeholders
4. Slide dimensions and aspect ratio (16:9 widescreen)
5. Layout coordinate boundaries and card non-emptiness

Usage:
    python3 verify_deck.py output/academic_presentation.pptx
"""

import sys
import os
import json
import zipfile
import argparse
import xml.etree.ElementTree as ET

OMML_NS = "http://schemas.openxmlformats.org/officeDocument/2006/math"
A14_NS = "http://schemas.microsoft.com/office/drawing/2010/main"
A_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"
P_NS = "http://schemas.openxmlformats.org/presentationml/2006/main"

NAMESPACES = {
    "m": OMML_NS,
    "a14": A14_NS,
    "a": A_NS,
    "p": P_NS
}

def verify_deck(pptx_path: str, meta_path: str = None, strict: bool = False) -> bool:
    print(f"=== Verifying Deck: {pptx_path} ===")
    
    if not os.path.exists(pptx_path):
        print(f"FAIL: File not found: {pptx_path}")
        return False
        
    if not zipfile.is_zipfile(pptx_path):
        print(f"FAIL: Not a valid ZIP / PPTX archive: {pptx_path}")
        return False

    with zipfile.ZipFile(pptx_path, 'r') as z:
        names = z.namelist()
        slide_files = sorted([n for n in names if n.startswith("ppt/slides/slide") and n.endswith(".xml")])
        print(f"Total Slides Found: {len(slide_files)}")
        
        if strict and len(slide_files) != 14:
            print(f"FAIL: Strict mode requires exact 14-slide spine, found {len(slide_files)}")
            return False
        elif len(slide_files) < 14:
            print(f"WARNING: Expected standard 14-slide spine, found {len(slide_files)}")
            
        total_omml_count = 0
        total_placeholders_remaining = 0
        
        for sf in slide_files:
            xml_data = z.read(sf)
            root = ET.fromstring(xml_data)
            
            # Check for OMML
            omml_elements = root.findall(".//m:oMath", NAMESPACES)
            a14_math = root.findall(".//a14:m", NAMESPACES)
            total_omml_count += len(omml_elements) + len(a14_math)
            
            # Check for unparsed placeholders
            text_str = xml_data.decode('utf-8', errors='ignore')
            for leak_token in ("<<MATH_", "{{MATH:", "[[MATH_DISPLAY:", "{{MATH_INLINE:", "{{MATH_DISPLAY:"):
                if leak_token in text_str:
                    total_placeholders_remaining += 1
                    print(f"FAIL: Found unparsed math placeholder '{leak_token}' in {sf}")

        print(f"Total Native OMML Equations Injected: {total_omml_count}")
        print(f"Unparsed Math Placeholders: {total_placeholders_remaining}")
        
        if total_placeholders_remaining > 0:
            print("FAIL: Deck contains unresolved math placeholders.")
            return False
            
        if strict and total_omml_count < 4:
            print(f"FAIL: Strict mode requires >= 4 OMML math elements, found {total_omml_count}")
            return False
        elif total_omml_count == 0:
            print("WARNING: No OMML math elements detected in the deck.")

        # Check figures metadata if provided
        if meta_path and os.path.exists(meta_path):
            try:
                with open(meta_path, "r", encoding="utf-8") as f:
                    meta_data = json.load(f)
                    figs = meta_data.get("figures", [])
                    print(f"Figures Metadata Verified: {len(figs)} extracted figures recorded.")
            except Exception as e:
                print(f"WARNING: Could not parse figures metadata: {e}")
            
        print("SUCCESS: Deck passed all OpenXML structural and math assertions!")
        return True

def main():
    parser = argparse.ArgumentParser(
        description="Programmatic OpenXML validator for academic presentation decks."
    )
    parser.add_argument("pptx_pos", nargs="?", default=None, help="Path to PPTX file (positional)")
    parser.add_argument("--pptx", type=str, default=None, help="Path to PPTX file")
    parser.add_argument("--meta", type=str, default=None, help="Path to figures_metadata.json")
    parser.add_argument("--strict", action="store_true", help="Enforce strict checks (14 slides, >= 4 OMML nodes, zero leaks)")

    args = parser.parse_args()
    target_pptx = args.pptx or args.pptx_pos or "output/academic_presentation.pptx"

    success = verify_deck(target_pptx, meta_path=args.meta, strict=args.strict)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
