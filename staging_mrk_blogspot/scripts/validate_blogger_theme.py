#!/usr/bin/env python3
"""Static checks for the MRK Blogger XML theme; cannot emulate Blogger's parser."""
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

THEME = Path("theme/mrk-blogger-theme.xml")
B = "{http://www.google.com/2005/gml/b}"
REQUIRED_WIDGETS = {"Header", "PageList", "Blog", "PopularPosts", "Label", "BlogArchive"}
REQUIRED_SECTIONS = {"header", "navigation", "main", "sidebarwidgets", "homepageextras", "sociallinks", "advertisements"}
REQUIRED_MARKERS = (
    "all-head-content",
    "twitter:card",
    "application/ld+json",
    "site-search",
    "primary-menu",
    "latest-posts",
    "https://wa.me/923270447263",
    "https://mrkdigitalservices.blogspot.com/p/services.html",
    "https://mrkdigitalservices.blogspot.com/p/projects-learning-portfolio-mrk-digital.html",
)


def main() -> int:
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
    section_ids = set()
    widget_ids = set()
    for label, elements, seen in (
        ("section", sections, section_ids),
        ("widget", widgets, widget_ids),
    ):
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

    missing_sections = REQUIRED_SECTIONS - section_ids
    if missing_sections:
        problems.append("Missing expected Blogger section(s): " + ", ".join(sorted(missing_sections)))

    widget_types = {element.attrib.get("type", "") for element in widgets}
    missing_widgets = REQUIRED_WIDGETS - widget_types
    if missing_widgets:
        problems.append("Missing expected Blogger widget type(s): " + ", ".join(sorted(missing_widgets)))

    nav = next((element for element in sections if element.attrib.get("id") == "navigation"), None)
    if nav is None or not any(w.attrib.get("type") == "PageList" for w in nav.findall(f".//{B}widget")):
        problems.append("The navigation section must contain a Blogger PageList widget.")

    source = THEME.read_text(encoding="utf-8")
    for marker in REQUIRED_MARKERS:
        if marker not in source:
            problems.append(f"Missing required theme feature marker: {marker}")
    if source.count("rel='canonical'") or source.count('rel="canonical"'):
        warnings.append("A custom canonical link exists; check that it does not duplicate Blogger's all-head-content output.")
    if "REPLACE_ME" in source or "YOUR_" in source:
        warnings.append("Potential placeholder text found; review before installation.")

    for problem in problems:
        print(f"::error::{problem}")
    for warning in warnings:
        print(f"::warning::{warning}")
    if problems:
        print(f"Theme validation failed with {len(problems)} error(s).")
        return 1
    print("PASS: XML is well-formed; required Blogger sections/widgets, IDs, navigation, SEO, search, contact, and page-link markers passed static checks.")
    print("LIMITATION: Static checks cannot confirm Blogger's server-side template parser or live deployment.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
