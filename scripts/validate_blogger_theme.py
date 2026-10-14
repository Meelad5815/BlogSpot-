#!/usr/bin/env python3
"""Static checks for the MRK Blogger XML theme. This cannot emulate Blogger's parser."""
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

THEME = Path("theme/mrk-blogger-theme.xml")
B = "{http://www.google.com/2005/gml/b}"

def main():
    if not THEME.exists():
        print(f"::error::Missing theme file: {THEME}")
        return 1
    try:
        root = ET.parse(THEME).getroot()
    except ET.ParseError as exc:
        print(f"::error::Theme XML is not well-formed: {exc}")
        return 1

    problems, warnings = [], []
    if not root.tag.endswith("html"):
        problems.append("Root element should be html.")
    if root.attrib.get(B + "version") != "2":
        warnings.append("Root b:version is not '2'; confirm this is intentional.")
    if root.find(f".//{B}skin") is None:
        problems.append("Missing b:skin element.")

    sections = root.findall(f".//{B}section")
    widgets = root.findall(f".//{B}widget")
    if not sections:
        problems.append("Missing Blogger b:section; editable widget sections are expected.")

    for label, elements in (("section", sections), ("widget", widgets)):
        seen = set()
        for element in elements:
            value = element.attrib.get("id", "").strip()
            if not value:
                problems.append(f"A Blogger {label} has no id.")
            elif value in seen:
                problems.append(f"Duplicate Blogger {label} id: {value}")
            else:
                seen.add(value)
            if label == "widget" and not element.attrib.get("type", "").strip():
                problems.append(f"Widget {value or '(no id)'} has no type.")

    source = THEME.read_text(encoding="utf-8")
    if "REPLACE_ME" in source or "YOUR_" in source:
        warnings.append("Potential placeholder text found; review before installation.")
    for problem in problems:
        print(f"::error::{problem}")
    for warning in warnings:
        print(f"::warning::{warning}")
    if problems:
        print(f"Theme validation failed with {len(problems)} error(s).")
        return 1
    print("PASS: XML is well-formed; Blogger skin, sections, widget IDs and widget types passed static checks.")
    print("LIMITATION: Static checks cannot confirm Blogger will accept or deploy the template.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
