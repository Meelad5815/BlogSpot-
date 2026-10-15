# MRK Digital Pro — Blogger theme

An installable Blogger XML theme for [MRK Digital & Online Services Center](https://mrkdigitalservices.blogspot.com/). The primary artifact is `theme/mrk-blogger-theme.xml`; this repository also contains setup guidance, original image assets, a static visual preview, and validation notes.

## Files

- `theme/mrk-blogger-theme.xml` — the Blogger theme source to upload.
- `assets/` — optional generated editorial images used by the theme. CSS color fallbacks remain if an image cannot load.
- `PREVIEW.html` — static visual preview; it is not a replacement for the Blogger XML theme.
- `ASSETS.md` — image inventory, recommended sizes, and generation prompts.
- `VALIDATION.md` — static validation results and the manual Blogger acceptance checklist.
- `scripts/validate_blogger_theme.py` — XML and template-structure checks run by GitHub Actions.
- `.github/workflows/validate-theme.yml` — existing automated check and theme-artifact workflow.
- `INSTALL-UR.md` — Urdu installation notes.

## Back up the current theme first

1. Sign in to Blogger and open the MRK Digital blog.
2. Open **Theme** and use the theme menu to download a backup of the current theme.
3. Keep the downloaded backup outside GitHub. Do not replace the live theme until the backup is safely stored.

## Upload the XML theme

1. Download `theme/mrk-blogger-theme.xml` from the repository after reviewing the pull request and its checks.
2. In Blogger, open **Theme**, open the theme menu, and choose the restore/upload option.
3. Upload the XML file. If Blogger reports a template error, keep the backup and do not retry blindly; inspect the indicated line and compare against the supported Blogger template syntax.
4. Open the live blog in a private browser window and check the homepage, an article, a static page, a label page, archive, search results, and a missing URL.

GitHub Actions can confirm well-formed XML and static theme invariants, but only Blogger's own upload can confirm that its server-side template parser accepts the file. No live upload has been performed by this project.

## Configure the layout

- **Navigation:** In Blogger **Layout**, edit the **Pages** (PageList) widget in the Navigation section. Select and reorder the real pages you want shown. A separate **Blog** link points to the homepage's latest-articles section.
- **Logo and title:** The theme uses Blogger's Header widget. Edit the blog title or choose a header image in Layout. The theme's text styling remains the fallback if no image is configured.
- **WhatsApp:** The visible WhatsApp links use the number already published on the site's Contact page. To change it, replace `https://wa.me/923270447263` in `theme/mrk-blogger-theme.xml` with the verified WhatsApp URL, then re-run validation and upload the updated theme.
- **Social profiles:** Add only verified profile URLs using the empty **Social Links** section in Layout. None are invented or pre-filled.
- **Ads:** Add AdSense or another supported ad widget in the empty **Advertisements** section after configuring that service in Blogger. No publisher ID is embedded in this theme.
- **Homepage content:** The services cards and portfolio callout use current MRK topics and known live page URLs. Optional widgets can be added in the Homepage Extras section.
- **Images:** The theme references files under `assets/` from the public repository's `main` branch. They appear after this change is merged to `main`; if you test the unmerged review branch, image backgrounds may use the CSS fallback colors. If you fork the repository, update the raw GitHub base URL in the theme.

## Customization and troubleshooting

- Navigation pages come from Blogger's PageList widget, so changing a page's permalink does not require editing a hard-coded menu URL.
- The service-page, portfolio-page, About-page, Contact-page, and footer links use verified URLs from the live Blogger site. Recheck these links if you later change page permalinks.
- Image backgrounds are decorative and have color fallbacks. If an image is missing, check that the repository is public and the `assets/` filename and branch URL are correct.
- The search form uses Blogger's `/search?q=` route. Confirm that search works on the public blog after uploading.
- The small mobile-menu script is inline and dependency-free. If you customize it, test keyboard operation, Escape-to-close, and small screens.
- Do not add passwords, OAuth tokens, API keys, or other secrets to XML, documentation, or GitHub commits.

## Restore the previous theme

In Blogger, open **Theme**, use the theme menu's restore/upload option, and upload the backup you downloaded before installation. Then check the live homepage and an article to confirm the rollback.

## Preview and validation

Open `PREVIEW.html` from a local checkout to see a static visual representation. It does not execute Blogger's dynamic widgets. For verified test scope and the live-install checklist, see `VALIDATION.md`.
