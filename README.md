# MRK Blogger Theme

Repository for the MRK Digital & Online Services Center Blogger theme.

## Files
- `theme/mrk-blogger-theme.xml` — Blogger XML theme source.
- `scripts/validate_blogger_theme.py` — static XML and Blogger-structure checks.
- `.github/workflows/validate-theme.yml` — runs checks on theme changes, writes a workflow summary, and uploads the XML as an artifact when checks pass.

## What is automated
When the theme or validation files change, GitHub Actions automatically checks:
- XML is well-formed.
- The template has a Blogger skin and widget sections.
- Blogger widget/section IDs are present and not duplicated.
- A validation summary is added to the Actions run, and a theme artifact is created if the checks pass.

These are **static checks only**. They cannot emulate Blogger's server-side template parser, inspect all live visual behavior, or automatically repair every runtime issue.

## Live deployment limitation
The workflow does **not** upload or install the theme on the live Blogger site. Blogger API v3 supports content operations such as posts and pages, but has no documented public theme upload/update endpoint. Adding OAuth credentials as GitHub Secrets cannot create an API capability that Blogger does not expose.

Do not store Google passwords, session cookies, or refresh tokens in repository files. Do not add secrets until there is a specific, supported API action that actually needs them. Never put credentials in a normal document or commit them to Git.

For a live theme change, first back up the current theme in Blogger, then install the validated XML through Blogger's Theme interface. XML validation does not guarantee Blogger will accept the template. Keep the backup so you can roll back.

## Blog
https://mrkdigitalservices.blogspot.com/

Navigation links are hard-coded to the known MRK page URLs. If a page URL changes, update the link in the theme source.

For Urdu instructions, see [INSTALL-UR.md](INSTALL-UR.md).
