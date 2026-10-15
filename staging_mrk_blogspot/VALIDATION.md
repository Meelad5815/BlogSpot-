# Validation record

## Automated/static checks

The current theme will be checked with:

1. Python's XML parser (`xml.etree.ElementTree`) for well-formed XML.
2. `scripts/validate_blogger_theme.py` for the Blogger root, skin, unique section/widget IDs, required widget types/sections, core feature markers, and link targets.
3. The existing GitHub Actions workflow, which runs the validator and publishes the theme XML as an artifact when the checks pass.

Record the resulting pull-request check status here after the workflow completes. Static checks do **not** emulate Blogger's server-side template compiler or prove the theme was installed.

## Manual Blogger checklist

Back up the current theme before testing. Upload the XML only after reviewing the diff and automated checks.

- [ ] Blogger accepts `theme/mrk-blogger-theme.xml` without a template-parser error.
- [ ] Homepage hero, 8 service cards, portfolio callout, latest posts, topic widgets, About section, contact CTA, and footer render.
- [ ] The Pages widget shows the intended real pages in the visible navigation; Blog and WhatsApp links work.
- [ ] Search submits a query to Blogger and results render.
- [ ] Test mobile navigation with touch and keyboard; verify `aria-expanded`, Escape-to-close, and focus visibility.
- [ ] Check one post, one static page, a label page, archive, search results, pagination, comments, and a missing URL.
- [ ] Check images at desktop/mobile sizes; confirm fallback colors if an asset is temporarily unavailable.
- [ ] Inspect page source for one canonical URL, a useful page title/description, Blogger's Open Graph output, Twitter card metadata, and valid Website JSON-LD.
- [ ] Confirm the Header, PageList, Popular Posts, Label, and Blog widgets can be managed in Blogger Layout.
- [ ] Verify no existing posts, comments, labels, or permalinks were changed.
- [ ] If any live issue appears, restore the pre-install Blogger theme backup.

## Unverified without Blogger

The template has not been uploaded to the live Blogger account. Blogger-specific expression evaluation, actual widget rendering, server-generated metadata, comments, mobile behavior in the live theme, and page-type layouts require manual verification in Blogger. GitHub Pages or a static preview cannot validate those runtime behaviors.
