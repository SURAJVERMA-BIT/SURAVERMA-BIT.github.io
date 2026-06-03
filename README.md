# XiteAI — Marketing Website

Static HTML/CSS/JS website for [xiteai.com](https://xiteai.com). No framework, no build step.

---

## Pages (32 HTML files)

| Route | Purpose |
|---|---|
| `/` | Homepage — hero, MAESTRO demo, student tools, pricing, CTA |
| `/waitlist/` | Early access signup (FormBold form) |
| `/thankyou/` | Post-signup confirmation page |
| `/features/` | Feature overview |
| `/pricing/` | Pricing tiers |
| `/company/` | About / vision |
| `/maestro/` | MAESTRO product page |
| `/superxite/` | SuperXite product page |
| `/document/` | Documentation hub |
| `/careers/` | Careers page |
| `/contact/` | Contact page |
| `/status/` | Service status page |
| `/legal/` | All policies index |
| `/privacy-policy/` | Privacy policy |
| `/terms-of-service/` | Terms of service |
| `/ai-disclaimer/` | AI disclaimer |
| `/responsible-ai/` | Responsible AI |
| `/beta-terms/` | Beta terms |
| `/acceptable-use-policy/` | AUP |
| `/cookie-policy/` | Cookie policy |
| `/copyright-policy/` | Copyright policy |
| `/data-deletion/` | Data deletion |
| `/fair-usage-policy/` | Fair usage |
| `/file-prompt-policy/` | File prompt policy |
| `/minors-policy/` | Minors policy |
| `/refund-policy/` | Refund policy |
| `/security/` | Security page |
| `/support-policy/` | Support policy |
| `/third-party-disclosure/` | Third-party disclosure |
| `/uptime-policy/` | Uptime policy |
| `/brand-guidelines/` | Brand guidelines |
| `404.html` | Custom 404 page |

---

## Features

- **MAESTRO animation** — live routing demo cycling through 4 AI prompts with phase steps, progress bar, and streaming output
- **Student tools section** — 4 panels (Cheat Sheet Studio, MCQ Studio, PYQ Analyzer, Exam Solver) each with an MP4 demo video
- **Video memory management** — videos unload their buffer when off-screen (`src` cleared + `load()` called), reload from browser cache on scroll-back; all paused on tab switch via `visibilitychange`
- **Pricing toggle** — monthly/yearly switch with animated number transitions (₹599/mo → ₹6,999/yr and ₹2,300/mo → ₹27,599/yr)
- **AI model marquee** — infinite scrolling strip of 12 AI model logos
- **Waitlist form** — FormBold (`/s/6rpBA`) with `_next` redirect to `/thankyou/`
- **Floating nav** — glassmorphism pill nav, scroll-aware border, mobile fullscreen overlay
- **Scroll fade-in** — `IntersectionObserver` on `.fade` elements, fires once
- **Cursor spotlight** — radial glow follows mouse inside hero section
- **Aurora background** — fixed CSS radial gradients with breathing animation
- **Clickjack protection** — `antiClickjack` inline style removed only when `self === top`
- **Image drag protection** — right-click and drag disabled on all images
- **SEO** — canonical tags, OG/Twitter meta, JSON-LD schema (Organization + SoftwareApplication)
- **Sitemap** — `sitemap.xml` at root
- **PWA manifest** — `site.webmanifest`

---

## Asset counts

| Type | Count |
|---|---|
| HTML pages | 32 |
| MP4 videos | 4 |
| Images (PNG/JPG/SVG) | 159 |
| Total files | 232 |

### Video files
```
assets/videos/student/cheatsheet.mp4
assets/videos/student/mcq.mp4
assets/videos/student/pyqplanner.mp4
assets/videos/student/solver.mp4
```

### Image folders
```
assets/images/Header/      — logo variants
assets/images/Page1/       — hero mockup screenshot
assets/images/FEATURES/    — feature section assets
assets/images/SuperXite/   — SuperXite product images
assets/images/Document/    — documentation assets
assets/images/page2/       — AI model logos (marquee)
assets/images/page3/       — misc section assets
assets/images/page9/       — pricing section assets
assets/images/persona/     — persona mode avatars
assets/images/status/      — status page assets
assets/images/thankyou/    — thank you page assets
assets/images/bottom/      — footer assets
assets/images/founder/     — founder photo
```

---

## Tech

- Pure HTML + CSS + vanilla JS — zero dependencies, no npm, no build
- Fonts: Inter (Google Fonts)
- Form backend: FormBold
- Hosting: static (deploy any folder to Netlify / Vercel / GitHub Pages)

## Deployment

Point any static host at the root folder. No build step, no config needed.

- Netlify / Vercel: connect repo, set publish directory to `/`
- GitHub Pages: serve from `main` branch root

## Branches

| Branch | Purpose |
|---|---|
| `main` | Production |
| `clean-empty` | Active development |

## Changing the form

FormBold form ID is in `waitlist/index.html` — `action` attribute on the `<form>` tag.  
To redirect elsewhere after submit, change the `_next` hidden field value on the same line.

## Contact emails

| Purpose | Address |
|---|---|
| Support | `support@xiteai.com` |
| General | `hello@xiteai.com` |
| Legal | `legal@xiteai.com` |
| Privacy | `privacy@xiteai.com` |
| Security | `security@xiteai.com` |
| Enterprise | `enterprise@xiteai.com` |
| Abuse | `abuse@xiteai.com` |

---

## Pricing

| Plan | Monthly | Yearly |
|---|---|---|
| Essentials | Free | Free |
| Prime | ₹599/mo | ₹6,999/yr |
| Ultimate | ₹2,300/mo | ₹27,599/yr |
| Enterprise | Custom | Custom |

---

## Company

XiteAI Technologies Pvt. Ltd. — Founded 2025  
Founder & CEO: Suraj Verma
