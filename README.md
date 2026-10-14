# MRK Blogger Theme

Repository for the MRK Digital & Online Services Center Blogger theme.

## Files
- `theme/mrk-blogger-theme.xml` — Blogger XML theme source.
- `.github/workflows/validate-theme.yml` — checks that the XML is well-formed and uploads a downloadable artifact.

## Important deployment limitation
GitHub is not automatically connected to Blogger's live theme. Blogger's public Blogger API v3 supports blog content (posts/pages) but does not provide a public theme upload/update endpoint. This workflow validates XML well-formedness and uploads a downloadable artifact; it does **not** publish or install the theme on Blogger. XML validation does not guarantee Blogger will accept the template, so test on a separate blog first if possible.

To apply a validated theme, download `theme/mrk-blogger-theme.xml`, then in Blogger use **Theme → (menu) → Backup** to save the current theme, and use **Restore/Upload** to install the new XML. Verify the preview and mobile layout before relying on it. Keep a backup so you can roll back.

## Blog
https://mrkdigitalservices.blogspot.com/

Navigation links are currently hard-coded to the known MRK page URLs. If a page URL changes, update the link in the theme source.


For Urdu installation steps, see [INSTALL-UR.md](INSTALL-UR.md).
