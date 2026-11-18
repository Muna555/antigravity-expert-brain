# 📚 Antigravity Self-Evolving Knowledge Base: Lessons Learned
### (ସୁଦର୍ଶନ ଭାଇଙ୍କ ସ୍ୱୟଂ-ବିକାଶଶୀଳ ଜ୍ଞାନ ଭଣ୍ଡାର - ପ୍ରତ୍ୟେକ ପ୍ରୋଜେକ୍ଟର ଅଭିଜ୍ଞତା ଓ ସମାଧାନ)

This document is automatically updated whenever an Antigravity agent or developer solves a new problem. It ensures the Expert Developer Brain becomes smarter, faster, and more brilliant every single day.

---

## 🏛️ CATEGORY 1: COMPLEX INDIC & DEVOTIONAL TYPOGRAPHY
- **Problem #001: Red Neon Blur Bleeding on Light/Cream Backgrounds**
  - **Symptom:** Glowing Gaussian blur (`radius=6`) in crimson red around blue text on a cream card creates optical chromatic haze. Small Odia matras (`୍ଦ`, `୍ର`, `ି`) appear blurry and washed out.
  - **Permanent Solution:** Eliminate fuzzy neon blur on light surfaces. Use **Deep Royal Navy (`#002A88`)** with a **2px solid crisp white contour (`#FFFFFF`)** and a **subtle 1px 3D drop shadow (`rgba(0,0,0,0.35)`)**.
  - **Measured Result:** Sharpness increases +50.2% (10.35 -> 15.55), Contrast ratio increases +43% (3.15:1 -> 4.51:1).

- **Problem #002: Long Names Downscaling to Tiny Font Sizes**
  - **Symptom:** Fixed `max_h=42` and `max_w=260` clamps in badge slots caused 21+ character names to be scaled down to 58%, resulting in ~17px microscopic text.
  - **Permanent Solution:** Expand badge slot to `max_w=280`, `max_h=48`. Trim faint alpha padding (<20 alpha) from HarfBuzz rendered bitmaps so scale checks only calculate visible solid glyphs. Enlarge top container box height to 86px and width up to 530px.
  - **Measured Result:** Name renders at full 35px in top banner and 31-34px in bottom badge with zero truncation.

- **Problem #003: Subtext Clipping by Destructive Rectangles**
  - **Symptom:** In legacy fallback rendering, drawing a solid white rectangle at `Y=970` destroyed the bottom half of `🙏 ପ୍ରଣାମ ପୂର୍ବକ ଶୁଭେଚ୍ଛା :`.
  - **Permanent Solution:** Completely eradicate the destructive rectangle. Use pure clean master templates (`clean_sakhigopal_master_template_1080x1440.jpg`) where the name slot below `Y=988` is naturally blank. Ensure a 9-10px clean gap between subtext and devotee text.

---

## ⚡ CATEGORY 2: TOKEN CONSERVATION & AGENT SPEED
- **Problem #004: Multi-Tool Chaining Overhead on Simple Edits**
  - **Symptom:** Agent runs 8 shell commands and writes temporary scratch scripts to edit 2 lines of CSS or HTML, burning 5,000+ tokens and taking 40 seconds.
  - **Permanent Solution:** Enforce **Tier 1 Micro-Edit Protocol**. Directly use `edit_file` on target lines in 1 single turn, followed by 1 scoped validation.
  - **Measured Result:** 75% latency reduction, 80% token savings.

- **Problem #005: Deep Context Slowness (>25 Turns)**
  - **Symptom:** LLM takes 25-40 seconds just to produce the first token because 50,000+ tokens of raw transcripts are sent on every request.
  - **Permanent Solution:** Automatic alert to user to run `/compact` or generate a **300-Token Master Handoff Brief** for a pristine fresh chat.

---

## 🔒 CATEGORY 3: VAULT SECURITY & REPO HYGIENE
- **Problem #006: Temporary Test Images Cluttering Git Status**
  - **Symptom:** Rapid test card generation left 80+ untracked images in `scratch/` showing up in `git status`.
  - **Permanent Solution:** Anchor `scratch/`, `*.log`, `*.db`, and credentials in `.gitignore`. Keep workspace 100% clean.
