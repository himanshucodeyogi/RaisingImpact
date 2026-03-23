# Website Structure & Content Blueprint: RaisingImpact.Org (v3.0)

RaisingImpact.Org (RIO) is an _Evidence-led_ and _Analytical_ organization. The website design must be clean, professional, and data-centric — reflecting credibility, trust, and rigour.

---

## Tech Stack

- **Framework:** Astro (static site generator)
- **Styling:** Tailwind CSS 4
- **3D Graphics:** Three.js (hero particle system)
- **Language:** TypeScript (strict mode)
- **Fonts:** Google Fonts (self-hosted preferred for performance)
- **Icons:** Inline SVGs only (Heroicons outline style) — no emojis anywhere in the UI

---

## Design System

### Color Palette

| Token       | Hex       | Usage                                    |
|-------------|-----------|------------------------------------------|
| Navy        | `#0F172A` | Dark backgrounds, primary headings       |
| Emerald     | `#10B981` | CTAs, accents, active states, highlights |
| Blue        | `#3B82F6` | Gradient accents, secondary highlights   |
| Purple      | `#7C3AED` | Tertiary accent (tags, category pills)   |
| Slate       | `#334155` | Body text                                |
| Light BG    | `#F8FAFC` | Section backgrounds                      |
| White       | `#FFFFFF` | Cards, clean sections                    |

### Typography

| Role         | Font Family    | Weights          | Usage                                    |
|--------------|----------------|------------------|------------------------------------------|
| Headings     | **Montserrat** | 600, 700, 800, 900 | h1-h4, logo, stats, buttons            |
| Body         | **Open Sans**  | 300, 400, 500, 600 | Paragraphs, descriptions, form labels  |
| Data/Mono    | **Inter**      | 400, 500, 600, 700 | Stats, numbers, data-heavy sections, Knowledge Hub filters |

> **Note:** Inter is imported but underutilized. Use it for data displays, report metadata, and filterable sections where a tighter, more technical feel is needed.

### Icon System

All icons must be **inline SVGs** (Heroicons outline style, 24x24 viewBox, stroke-based). No emojis, no icon fonts.

**Standard icon container:**
```html
<div class="w-14 h-14 rounded-2xl bg-gradient-to-br from-emerald-500/20 to-emerald-500/5 flex items-center justify-center text-[#10B981]">
  <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">...</svg>
</div>
```

**Icon mapping (replace all emojis):**

| Context                    | Old (emoji) | New (SVG description)                        |
|----------------------------|-------------|----------------------------------------------|
| Impact Multiple stat       | n/a         | Arrow-trending-up (chart with upward arrow)  |
| Evidence-Led Research stat | n/a         | Beaker / flask (scientific research)         |
| Philanthropists Advised    | n/a         | User-group (multiple people)                 |
| Years of Rigour            | n/a         | Shield-check (trust/verified)                |
| Mission card               | n/a         | Crosshair / target (bullseye)                |
| Vision card                | n/a         | Eye / telescope (forward-looking)            |
| Values card                | n/a         | Lightbulb (ideas/innovation)                 |
| Impact card                | n/a         | Chart-bar (data/analytics)                   |
| Checkmarks in lists        | n/a         | Check SVG icon (small, inline, emerald)      |
| Form success messages      | n/a         | Check-circle SVG icon                        |

### Animations

- **Fade-up:** Elements enter with `opacity: 0 -> 1` and `translateY(40px -> 0)` on scroll intersection
- **Stagger delays:** `.delay-100` through `.delay-400` (100ms increments)
- **Glow button:** Pulsing `box-shadow` animation on primary CTAs (emerald glow, 2.5s infinite)
- **Smooth scroll:** `scroll-behavior: smooth` globally

### Responsive Breakpoints

- Mobile-first approach
- `md:` (768px) — 2-column grids, desktop nav visible
- `lg:` (1024px) — 3-column grids, wider content areas

---

## Pages & Sections

### 1. Header (Navigation) — `Navbar.astro`

- **Logo:** Left side — emerald rounded square with "R" + "Raising**Impact**" wordmark (Montserrat bold)
- **Menu Items:** Home, About, Our Team, Contact
- **CTA Button:** "Partner With Us" (emerald background, rounded-xl, shadow)
- **Behavior:**
  - Fixed position, transparent on top
  - On scroll (>20px): navy background with backdrop blur + shadow
  - Mobile: hamburger menu icon toggles dropdown panel with backdrop blur

**Missing from current nav (add when pages are built):**
- Knowledge Hub
- Our Services

---

### 2. Home Page (`/`) — `index.astro`

#### 2a. Hero Section

- **Badge:** Pill with pulsing green dot — "Evidence-Led Philanthropy Research"
- **Headline:** "Guiding Philanthropy **With Rigour.**" (gradient text on "With Rigour")
- **Sub-headline:** "Helping philanthropists maximize social impact through rigorous, data-driven research and evidence-based advisory."
- **Primary CTA:** "Partner With Us" (glow button)
- **Secondary CTA:** "Our Approach" (ghost button with border)
- **Background:** Three.js 3D particle system (1500 particles in emerald/blue/white, wireframe sphere overlay, mouse parallax)
- **Gradient overlays:** Top-to-bottom and bottom fade for readability
- **Scroll indicator:** "Scroll" text + animated gradient line at bottom center

#### 2b. Stats Grid

4 stat cards in a 2x2 (mobile) / 4-column (desktop) grid on navy background.

| Stat   | Value  | Label                    | SVG Icon                        |
|--------|--------|--------------------------|---------------------------------|
| Stat 1 | 17x    | Average Impact Multiple  | Arrow-trending-up chart icon    |
| Stat 2 | 100%   | Evidence-Led Research    | Beaker / science flask icon     |
| Stat 3 | 50+    | Philanthropists Advised  | User-group / people icon        |
| Stat 4 | 3+     | Years of Rigour          | Shield-check / verified icon    |

**Card style:** `bg-white/5 border border-white/10 rounded-2xl` with emerald hover border

#### 2c. Core Approach (How We Work)

3 cards on light background:

| Card                   | SVG Icon          | Gradient                 |
|------------------------|-------------------|--------------------------|
| Analytically Rigorous  | Bar-chart icon    | emerald-500/20 gradient  |
| Regionally Rooted      | Globe icon        | blue-500/20 gradient     |
| Cost-Effective         | Currency icon     | purple-500/20 gradient   |

Each card: white background, rounded-3xl, shadow on hover, emerald border on hover.

#### 2d. Latest Insights (Research & Reports)

3 report preview cards:
- **Header area:** Dark gradient with decorative circles + colored tag pill (Education/Health/Livelihoods)
- **Body:** Date, read time, title, excerpt
- **Hover:** Shadow + emerald title color transition

**Reports shown:**
1. "ECCE Pilot Study: Early Childhood Interventions in Rural India" — Education — Dec 2024
2. "Maternal Health Outcomes Across Income Tiers" — Health — Oct 2024
3. "Skill Development ROI: A Cost-Benefit Analysis" — Livelihoods — Aug 2024

**Link:** "View All Research" pointing to Knowledge Hub (when built)

#### 2e. CTA Banner

- Navy background with emerald/blue gradient overlay + decorative circle
- Headline: "Ready to Maximize **Your Social Impact?**"
- Text: "Join a growing community of thoughtful philanthropists who make evidence-based giving decisions."
- CTA: "Start a Conversation" (glow button linking to /contact)

---

### 3. About Page (`/about`) — `about.astro`

#### 3a. Hero

- Section label: "About Us"
- Headline: "Bridging Intent & **Measurable Outcomes**" (gradient text)
- Sub-text about closing the gap between desire and evidence
- Decorative: Large border circles in top-right

#### 3b. Mission & Vision

Two-column layout:
- **Left:** "Why We Exist" narrative text (3 paragraphs about India's philanthropy gap)
- **Right:** 2x2 grid of value cards:

| Card    | SVG Icon                    | Description                                           |
|---------|-----------------------------|-------------------------------------------------------|
| Mission | Target/crosshair icon       | Rigorous, independent research for philanthropists    |
| Vision  | Eye/telescope icon          | Evidence-based giving as the norm in India            |
| Values  | Lightbulb icon              | Intellectual honesty, transparency, cost-consciousness |
| Impact  | Chart-bar/analytics icon    | 17x impact multiples through proven methodologies     |

#### 3c. Methodology (Our Process)

3-phase horizontal timeline with connecting gradient line:

| Phase | Step | Title            | Items (4 each)                                                |
|-------|------|------------------|---------------------------------------------------------------|
| 1     | 01   | Data Collection  | Literature review, field interviews, program docs, baselines  |
| 2     | 02   | Analysis         | Cost-effectiveness, causal attribution, benchmarking, quality |
| 3     | 03   | Action           | Recommendations, resource allocation, roadmap, monitoring     |

Each phase card has colored step badge (emerald/blue/purple) and checklist items with SVG check icons.

#### 3d. Inspiration (Standing on Giants' Shoulders)

2 cards on navy background featuring:
- **GiveWell** — Evidence-based charity evaluation
- **Founders Pledge** — High-impact giving for entrepreneurs

Each card: `bg-white/5 border border-white/10 rounded-3xl` with external link button (SVG arrow icon)

#### 3e. Journey Timeline

Vertical timeline with year badges:
- **2021:** The Founding Insight (Vikrant + Luke)
- **2022:** ECCE Pilot Study (highlighted/active state with emerald background)
- **2023:** Scaling Advisory
- **2024:** Growing Impact (50+ philanthropists)

---

### 4. Team Page (`/team`) — `team.astro`

#### 4a. Hero

- Centered layout
- Headline: "The People Behind **The Research**" (gradient text)

#### 4b. Culture Note

Split layout:
- **Left:** Quote + paragraph about deliberately small, senior team
- **Right:** 4 value pills — "Research First", "Open Collaboration", "Evidence Wins", "No Sacred Cows"

#### 4c. Team Grid (3-column)

| Name            | Role                        | Background           | Gradient Colors          |
|-----------------|-----------------------------|----------------------|--------------------------|
| Vikrant Bhargava | Co-Founder & Research Lead | Ex-Sattva Consulting | emerald-600 to teal-700  |
| Luke Ding       | Co-Founder & Advisory Lead  | Ex-Veddis Foundation | blue-600 to indigo-700   |
| Priya Sharma    | Senior Research Analyst     | Ex-J-PAL South Asia  | purple-600 to violet-700 |
| Aryan Mehta     | Policy Research Lead        | Ex-NITI Aayog Fellow | orange-600 to red-700    |
| Sunaina Kapoor  | Data Science & Analytics    | Ex-McKinsey Digital  | pink-600 to rose-700     |
| Rahul Nair      | Field Research Associate    | Ex-Aga Khan Foundation | cyan-600 to sky-700    |

Each card:
- Gradient header with initials in frosted glass square + decorative circles
- Name, role (emerald), background tag pill
- Bio text
- LinkedIn SVG icon button (navy bg, emerald on hover)

#### 4d. Join Our Team CTA

Gradient border card on navy background:
- "Are You Obsessively Curious About Social Impact?"
- Link to /contact

---

### 5. Contact Page (`/contact`) — `contact.astro`

#### 5a. Hero

- Centered layout
- Headline: "Let's Start a **Conversation**" (gradient text)

#### 5b. Contact Section (5-column grid)

**Left (2 cols) — Info panel:**
- Contact details with SVG icons:
  - Email: info@raisingimpact.org (envelope icon)
  - Location: New Delhi, India (map-pin icon)
  - Response Time: Within 48 hours (clock icon)
- Social links: LinkedIn + Twitter/X (SVG icons in bordered buttons)
- Newsletter signup: dark card with email input + "Join" button
  - Success message: SVG check-circle + "You're subscribed!"

**Right (3 cols) — Contact form:**
- Fields: Full Name*, Email*, Organization, Area of Interest (dropdown), Message*
- Interest options: Philanthropy Advisory, Research Collaboration, Education & ECCE, Health Interventions, Livelihoods & Skilling, General Inquiry
- Submit button: "Send Message" (navy bg, emerald on hover)
- Success: SVG check-circle + "Message sent! We'll be in touch shortly."

---

### 6. Knowledge Hub Page (`/knowledge-hub`) — NOT YET BUILT

This is a critical missing page from the PRD. It serves as the resource center.

#### 6a. Hero

- Headline: "Knowledge Hub" with sub-text about open-access research
- Filter bar: Category dropdown + search input

#### 6b. Report Grid (Filterable)

- **Filter categories:** All, Education, Health, Livelihoods, Environment, Cross-Sector
- **Card layout:** Image/gradient header, category tag, title, date, read time, excerpt, download button
- **Interactive:** Client-side filtering with Astro islands or vanilla JS

#### 6c. Report Types

- Sector-wise research reports (Education, Healthcare, Livelihoods, Environment)
- Cost-Effectiveness Playbooks
- Case Studies
- Policy Briefs

#### 6d. Featured Report

Full-width highlight card for the latest/flagship report (ECCE Pilot Study) with:
- Summary stats
- Key findings
- Download CTA

---

### 7. Services Page (`/services`) — NOT YET BUILT

#### 7a. Hero

- Headline: "Tailored Strategic Advisory"
- Sub-text about bespoke philanthropy advisory services

#### 7b. Service Cards

| Service        | Audience                    | Description                                           |
|----------------|-----------------------------|-------------------------------------------------------|
| For Donors     | HNWIs and Corporates        | Finding high-impact NGOs, due diligence, portfolio design |
| For NGOs       | Nonprofits and social enterprises | Improving execution quality and measurement          |
| For Foundations| Institutional philanthropies | Grant strategy, sector landscaping, impact frameworks  |

#### 7c. Methodology

Research -> Data Analysis -> Actionable Recommendations (visual flow)

#### 7d. Engagement CTA

"Partner With Us" leading to contact form

---

### 8. Impact Areas Section — NOT YET BUILT (can be standalone page or section on About)

#### Content

| Area                    | Highlight                              | SVG Icon              |
|-------------------------|----------------------------------------|-----------------------|
| Early Childhood (ECCE)  | 17x impact multiple research           | Academic cap icon     |
| Sustainable Agriculture  | Focus on small & marginal farmers     | Leaf / plant icon     |
| Maternal Health          | Income-tier outcome analysis          | Heart / health icon   |
| Livelihoods & Skilling   | Vocational training ROI              | Briefcase icon        |
| Public Knowledge Goods   | Open-access ecosystem resources      | Book-open icon        |

---

### 9. Footer — `Footer.astro`

4-column layout on navy background:

- **Brand (2 cols):** Logo + tagline + LinkedIn & Twitter SVG icon buttons
- **Navigation:** Home, About, Our Team, Knowledge Hub, Services, Contact
- **Contact:** Email (envelope SVG) + Location (map-pin SVG)
- **Bottom bar:** Copyright (update to 2026) + "Built with rigour, driven by purpose."

**Missing from footer (add when pages built):**
- Knowledge Hub link
- Services link
- Newsletter signup (or link to contact page newsletter)
- Terms of Service link
- Privacy Policy link

---

## SEO & Meta

- **Title format:** `{Page Title} | Raising Impact`
- **Meta description:** Unique per page, referencing evidence-led philanthropy
- **OG Tags:** Add `og:title`, `og:description`, `og:image`, `og:url` for social sharing
- **Twitter Card:** `twitter:card`, `twitter:title`, `twitter:description`
- **Favicon:** SVG format (already in `/public/favicon.svg`)
- **Canonical URLs:** Add `<link rel="canonical">` per page
- **Structured data:** Organization schema (JSON-LD) on homepage

---

## Accessibility

- Semantic HTML (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`)
- `aria-label` on all icon-only buttons and links
- Proper `<label>` elements on all form inputs with `required` attributes
- Focus-visible outlines on all interactive elements
- Color contrast ratios meet WCAG 2.1 AA (navy on white, white on navy, emerald on navy all pass)
- Mobile hamburger menu keyboard-accessible
- Skip-to-content link (add to Layout)
- Alt text on all images (when real images are added)

---

## Performance

- **Preconnect** to Google Fonts (already implemented)
- **Font display:** `swap` for faster rendering
- Intersection Observer for lazy scroll animations (already implemented)
- Static site generation via Astro (zero JS shipped unless needed)
- Three.js loaded only on homepage
- Image optimization: use Astro's `<Image>` component when real photos are added
- Target: Lighthouse 90+ across all categories

---

## Pending Items (Not Yet Implemented)

1. **Knowledge Hub page** — filterable report grid with download functionality
2. **Services page** — advisory offering details
3. **Impact Areas** — dedicated section or page
4. **Replace all emojis with SVGs** — stats grid (index.astro), mission/vision cards (about.astro), form success messages (contact.astro), methodology checklist marks (about.astro)
5. **Real team photos** — replace gradient+initials avatars with actual headshots
6. **Actual logo** — replace "R" placeholder with high-res transparent logo
7. **Real social links** — update LinkedIn/Twitter URLs from placeholder
8. **OG/social meta tags** — add to Layout.astro
9. **Privacy Policy & Terms of Service pages**
10. **404 page** — custom error page matching site design
11. **Analytics integration** — Google Analytics or Plausible
12. **Form backend** — connect contact form and newsletter to actual service (e.g., Formspree, Resend)
13. **Copyright year** — update footer from 2024 to 2026
14. **Skip-to-content link** — accessibility improvement in Layout
15. **Structured data** — JSON-LD Organization schema on homepage
16. **Sitemap** — auto-generate with Astro integration
17. **robots.txt** — add to /public
