# MRK Blogger Theme

Blogger XML theme for MRK Digital & Online Services Center.

## Files
- `theme/mrk-blogger-theme.xml` — installable Blogger XML theme.
- `assets/` — hero and service-card images referenced by HTTPS raw GitHub URLs in the XML.
- `scripts/validate_blogger_theme.py` — static XML and Blogger-structure checks.
- `.github/workflows/validate-theme.yml` — validates theme changes and uploads the XML as a workflow artifact when checks pass.

## Theme features
- Responsive navy-and-gold branding.
- Home-page hero section with a hosted image.
- Six image-backed service cards.
- Blog search form, blog post area, popular posts and labels widgets.
- Navigation and footer links, responsive layout, descriptive image alt text, and lazy loading for service-card images.
- Blogger page title and meta-description binding.

## Images and XML
The XML file references image assets hosted in this repository at `raw.githubusercontent.com`. The image bytes are not embedded inside the XML; Blogger loads them by URL. The images will render while the repository and file paths remain available. If assets are moved or renamed, update the URLs in the theme.

## Validation
GitHub Actions checks XML well-formedness and basic Blogger structure (skin, sections, unique IDs, widget types). These are static checks and do not emulate Blogger's server-side parser or guarantee live acceptance.

## Live installation limitation
The workflow does not install the theme on the live Blogger site. Blogger API v3 has no documented public theme upload/update endpoint. Back up the current Blogger theme, then upload the XML using Blogger's Theme interface and check the live site on desktop and mobile.

Do not store Google passwords, session cookies, or OAuth tokens in repository files or Git commits.

## Blog and direct download
- Blog: https://mrkdigitalservices.blogspot.com/
- **Direct XML download/view:** https://raw.githubusercontent.com/Meelad5815/BlogSpot-/main/theme/mrk-blogger-theme.xml
- GitHub file view: https://github.com/Meelad5815/BlogSpot-/blob/main/theme/mrk-blogger-theme.xml
- Assets: https://github.com/Meelad5815/BlogSpot-/tree/main/assets
- Actions: https://github.com/Meelad5815/BlogSpot-/actions
- Urdu installation guide: [INSTALL-UR.md](INSTALL-UR.md)

Navigation URLs are hard-coded to the current known page URLs. If a page slug changes, update the matching link in the XML.
