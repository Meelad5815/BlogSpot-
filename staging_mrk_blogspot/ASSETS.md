# Theme asset manifest

The theme uses original generated editorial images hosted in this repository. The generated source files are **1024 × 1024 px (1:1)**; the theme crops them with `background-size: cover` for the wide hero and card areas. For future replacements, use compressed WebP or JPEG files with the recommended 16:9 crop below. Images are decorative; the related service heading and description carry the meaning. The CSS supplies a solid-color/gradient fallback, so the layout remains usable if a file is missing.

For best results, use compressed WebP or JPEG files with a 16:9 crop for wide cards. The current generated JPEGs are stored in `assets/` and are intended for direct use from the public repository. The text-based Blogger Header widget is the default logo; no generated lettering is baked into an image.

| Filename | Purpose | Recommended dimensions | Aspect ratio | Visual subject | Optional? |
|---|---|---:|---:|---|---|
| `assets/mrk-digital-hero.jpg` | Homepage hero background | 1600 × 900 px | 16:9 | Abstract digital network and laptop UI in navy/gold, with clear space for the headline | Optional; gradient fallback |
| `assets/website-development.jpg` | Website and WordPress cards | 1200 × 675 px | 16:9 | Small-business website design workspace with a generic screen and no readable text | Optional; gradient fallback |
| `assets/seo-marketing.jpg` | SEO and digital marketing card | 1200 × 675 px | 16:9 | Laptop with abstract analytics and a planning notebook | Optional; gradient fallback |
| `assets/online-services.jpg` | Government and online services card | 1200 × 675 px | 16:9 | Person using a laptop and phone with a generic, unbranded form UI | Optional; gradient fallback |
| `assets/freelancing.jpg` | Freelancing card | 1200 × 675 px | 16:9 | Freelancer at a home-office desk with a generic portfolio layout | Optional; gradient fallback |
| `assets/plc-automation.jpg` | PLC and industrial automation card | 1200 × 675 px | 16:9 | Neatly wired low-voltage training PLC bench in a workshop | Optional; gradient fallback |
| `assets/arduino-electronics.jpg` | Arduino and ESP32 card | 1200 × 675 px | 16:9 | Beginner electronics prototype with a development board, sensor, and LEDs | Optional; gradient fallback |
| `assets/graphic-design.jpg` | Graphic design card | 1200 × 675 px | 16:9 | Display with abstract color swatches and geometric composition, no legible wording | Optional; gradient fallback |
| `mrk-digital-logo.png` | Optional custom header image, if a logo is later supplied | 600 × 160 px | 15:4 | Simple wordmark/icon in navy and gold, transparent background, use the exact approved brand name | Optional; Header widget text remains |
| `mrk-digital-social.jpg` | Optional social-sharing image | 1200 × 630 px | 1.91:1 | Brand-neutral technology scene with safe space for an approved logo and headline | Optional; no separate file is required |

## Generation prompts

The generated images use these prompt concepts; request no readable text, logos, watermarks, official seals, or personal information:

- **Hero:** “Premium editorial technology photograph for a Pakistani digital services and learning brand website, wide 16:9 composition, deep midnight navy background with restrained gold highlights, luminous abstract network lines, laptop showing a generic website layout with no readable text, professional trustworthy studio look, clear negative space for a headline.”
- **Website development:** “Modern small-business website design and development workspace, wide editorial photo, desktop monitor with a clean generic responsive website UI, warm daylight, navy and subtle gold accents, no logos or watermark.”
- **PLC automation:** “Industrial PLC automation training bench in a clean workshop, compact controller, neatly wired sensors and status lights, safe low-voltage demonstration setup, navy and subtle gold palette, no readable labels.”
- **Arduino/electronics:** “Arduino and ESP32 learning project on an organized workbench, development board, jumper wires, sensor module and LED, safe beginner prototype, no readable text or branding.”
- **SEO/marketing:** “Digital marketing and SEO planning workspace, laptop with abstract analytics charts without readable labels, notebook with simple diagrams, navy and muted gold details.”
- **Graphic design:** “Graphic design workspace with abstract color swatches and geometric poster composition on a display, stylus and tablet, navy and gold accents, no legible text.”
- **Freelancing:** “Freelancer working from a bright home office, laptop with generic portfolio layout, notebook, warm natural light, approachable professional atmosphere, no logos.”
- **Online services:** “Person using a laptop and smartphone at a clean desk with a generic neutral online form UI, no official logos, seals, emblems, or private data, soft daylight, navy and gold details.”
- **Optional logo:** “Minimal, legible MRK Digital wordmark in navy and gold with a transparent background; use separately supplied approved lettering because generated text may be inaccurate.”
- **Optional social image:** “Wide 1.91:1 digital-services technology scene in navy and restrained gold, with empty space for the approved brand mark and headline; no generated lettering.”
