#!/usr/bin/env python3
"""Static checks for the MRK Blogger XML theme. This cannot emulate Blogger's parser."""
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

THEME = Path("theme/mrk-blogger-theme.xml")
B = "{http://www.google.com/2005/gml/b}"

def fail(message):
    print(f"::error::{message}")
    return False

def main():
    if not THEME.exists():
        fail(f"Missing theme file: {THEME}")
        return 1

    try:
        tree = ET.parse(THEME)
    except ET.ParseError as exc:
        fail(f"Theme XML is not well-formed: {exc}")
        return 1

    root = tree.getroot()
    problems = []
    warnings = []

    if not root.tag.endswith("html"):
        problems.append("Root element should be html.")
    if root.attrib.get(B + "version") != "2":
        warnings.append("Root b:version is not '2'; confirm this is intentional.")
    if root.find(f".//{B}skin") is None:
        problems.append("Missing b:skin element.")
    if root.find(f".//{B}section") is None:
        problems.append("Missing b:section; Blogger needs editable widget sections.")

    for element_name, label in ((f".//{B}widget", "widget"), (f".//{B}section", "section")):
        seen = set()
        for element in root.findall(element_name):
            key = "id" if label == "section" else "id"
            value = element.attrib.get(key, "").strip()
            if not value:
                problems.append(f"A Blogger {label} has no id.")
            elif value in seen:
                problems.append(f"Duplicate Blogger {label} id: {value}")
            else:
                seen.add(value)

    for element in root.iter():
        if element.tag.endswith("widget"):
            widget_type = element.attrib.get("type", "")
            if not widget_type:
                problems.append(f"Widget {element.attrib.get('id', '(no id)')} has no type.")
        if element.tag.endswith("section"):
            if not element.attrib.get("id"):
                problems.append("A Blogger section has no id.")

    text = THEME.read_text(encoding="utf-8")
    if "REPLACE_ME" in text or "YOUR_" in text:
        warnings.append("Potential placeholder text found; review before installation.")

    if problems:
        for problem in problems:
            fail(problem)
        for warning in warnings:
            print(f"::warning::{warning}")
        print(f"Theme validation failed with {len(problems)} error(s).")
        return 1

    for warning in warnings:
        print(f"::warning::{warning}")
    print("PASS: XML is well-formed; Blogger root, skin, sections, and widget IDs passed static checks.")
    print("LIMITATION: These static checks cannot confirm Blogger will accept the template or deploy it.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
