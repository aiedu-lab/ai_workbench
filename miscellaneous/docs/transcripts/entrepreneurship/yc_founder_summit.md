# YC Founder Summit

## Recap Notes 2026

*A two-day event where ~2,500 applicants (300 selected as "startup school" attendees, with an inner circle of ~15–20 tracked closely by YC partners) heard from founders, investors, and policymakers. Notes below are organized from a high-level summary down to per-speaker details.*

---

## 1. Executive Summary

- **Persistence over talent**: Nearly every speaker (Jensen Huang, Gray Baker, Patrick Collison, Alexander Wang, Sam Altman) had years of failure, rejection, or stagnation before their breakout success. The recurring lesson: *keep building, don't chase recognition.*
- **People remember people**: Careers pivoted on individual relationships (Tom Blomfield recruiting Gray Baker to YC; PG backing Sam Altman; Jensen's early investors staying loyal) far more than on pure technical merit.
- **Start from the fundamentals, then re-derive with each new paradigm**: Whether it's Jensen going back to textbooks, or Wim's robotics team re-tooling for CNNs → Transformers → VLMs, the winners kept returning to first principles instead of assuming old architectures were final.
- **Products started absurdly small**: Stripe's first version was ~400–500 lines of code that mocked almost everything except the arithmetic; Dependabot/GoCardless-style tools began as single-client experiments.
- **UK vs. US venture culture**: Multiple speakers (Gray Baker, YC partners) framed British VC as roughly where Indian VC was ~20 years ago — lower risk appetite, and GoCardless remains the *only* British YC unicorn to date.
- **AI-native takeaways**: Anthropic's Boris Turney noted models are more general than their scaffolding suggests — removing rigid harnesses sometimes reveals surprising raw capability. Physical Intelligence's Chelsea Finn described using "gradient of change" frame-sampling instead of full video to work around tiny context windows for robotics memory.

---

## 2. Day One

### 2.1 Jensen Huang — NVIDIA (founder story)
**Takeaways**
- Chase problems, not solutions — scope the solution *from* the problem.
- When stuck, go back to fundamentals: "It was in their disk, not their RAM."
- Perseverance mattered more than raw talent; NVIDIA had failed chips and rough early years.
- Never assume you know how big something will get — just keep learning without asking "where will I use this?"

**Details**
Huang spoke about NVIDIA's founding in his 30s, emphasizing that early struggles (including a failed chip) were met with radical honesty toward investors and teammates rather than concealment. He contrasted this openness with what the speakers described as an American cultural tolerance for early-stage failure, versus impatience seen elsewhere. His core message on lifelong learning: absorb information without needing an immediate application — compounding understanding pays off later, similar to Steve Jobs's "connecting the dots" idea. [Reference: NVIDIA's official history — https://www.nvidia.com/en-us/about-nvidia/corporate-timeline/]

---

### 2.2 Boris Turney — Anthropic (Claude)
**Takeaways**
- Models trained broadly absorb side-skills beyond their intended task.
- Heavy scaffolding/system prompts can *constrain* a model's latent ability.
- Stripping scaffolding and pointing a model at an unrelated task can reveal surprisingly strong performance (e.g., a model linked to OpenCV producing image outputs comparable to 2017–18 GANs).
- Suggests harnessing model power deliberately, then testing what happens when you remove the harness.

**Details**
Coming from an economics (not CS) background, Turney discussed his team's experiments with minimal scaffolding, arguing the field should treat scaffolding as a leaky abstraction to be periodically stripped away and rebuilt from first principles — echoing the "back to fundamentals" theme from Huang's talk. [Reference: Anthropic's Claude overview — https://www.anthropic.com/claude]

---

### 2.3 Gray Baker — YC Partner (formerly GoCardless, Dependabot-style startup, legal-tech startup)
**Takeaways**
- Self-taught in a library for six months before landing his first engineering job.
- "Builds something customers want, listen to your customers" — YC's central mantra.
- Founders should own the full customer-facing loop, not delegate all sales contact.
- British risk-aversion cost his company (GoCardless) a much larger exit — sold for $1.2B vs. an estimated possible $15B.
- Second startup (a code-dependency-tracking/automation tool, pre-dating today's "agents") sold to GitHub under competitive pressure — he later regretted moving too fast.
- Third startup (legal-tech contract AI, post-ChatGPT) grew to $8–10M ARR in 18 months but ended in a co-founder dispute; company sold for $70M with little personal payout.
- Relationship-driven career reboot: Tom Blomfield (GoCardless founder, later Monzo founder, then YC then Anthropic) personally recruited him into YC, where he became the fastest visiting-partner-to-full-time-partner in YC history.

**Details**
Baker's arc is the most detailed "hero's journey" in the talk: self-taught engineer → VP of Engineering → founder (twice) → YC partner. He explicitly tasked the ~15–20 students he mentored with building "the second British YC unicorn," calling it a patriotic duty since GoCardless remains the only one. [Reference: Y Combinator — https://www.ycombinator.com/]

---

### 2.4 Wim — Physical AI / Robotics
**Takeaways**
- Every major model paradigm shift (CNNs → Transformers/LLMs → VLMs) required the team to rebuild from scratch rather than resist change.
- Betting early — even partially — on unproven architectures (like applying text-sequence ideas to sensor/camera data) kept the team competitive with dedicated research labs.
- Rule of thumb: bet that models will keep improving; don't assume today's cost/latency limits are permanent.

**Details**
Wim (20+ years in the field) described the discipline of pioneering techniques like fusing different sensor embeddings and adapting matrix-multiplication-heavy pipelines as GPU compute became viable — a shift he said only really matured around 2022, despite NVIDIA's dominance feeling much older.

---

### 2.5 Michael Kratsios — US AI Policy
**Takeaways**
- His career stalled after a change in administration, then reignited when he was remembered and re-appointed — another "people remember people" story.
- Goal: US AI-related spending up to $200B by early 2030s.
- Warned against over-indexing purely on LLM/generative hype — classical ML and reinforcement learning deserve renewed attention too.

**Details**
Kratsios traced his policy career back to a 2019 Trump-era executive order on AI R&D, which gave him his first real opportunity, followed by a stagnant period and eventual reappointment. [Reference: White House AI policy — https://www.whitehouse.gov/ai/]

---

## 3. Day Two

### 3.1 Patrick Collison — Stripe
**Takeaways**
- Stripe's original MVP was ~400–500 lines of code, mocking almost everything except arithmetic.
- Built iteratively for a single trusted client over six months before expanding.
- "I dropped out of college, but I didn't drop out of Stripe" — deliberate timing matters more than performative urgency.
- Payments were a broken, high-stakes space; mistakes there don't get second chances, so extreme care with the first client was essential.

**Details**
Collison (with his brother) discovered the payments problem as a side-effect of a different project. Despite skepticism from PG and the difficulty of two 20-year-olds entering a space dominated by centuries-old banks, they iterated relentlessly with one client, adding one requested feature at a time (arithmetic logging → dashboard → payment confirmation, etc.) before opening up to the broader YC network and then the public market. [Reference: Stripe company info — https://stripe.com/about]

---

### 3.2 Alexander Wang — Scale AI
**Takeaways**
- Identified data labeling as the real bottleneck (alongside compute and models) for AI training around 2016–17.
- Pivoted from a failing healthcare-agent idea (per YC partner Jared Friedman's direct feedback) into a data-labeling API — his first real product.
- VCs who dismissed data as a "commodity" early on later called it "the new oil" — reinforcing that picking the right VCs matters as much as the right idea.

**Details**
Wang's path (project → prototype → MVP → product) is presented as a model for iterative pivoting under mentor pressure. He now also discussed his newer role at Meta, working on a cheaper (if less proven) model architecture. [Reference: Scale AI — https://scale.com/]

---

### 3.3 Chelsea Finn — Physical Intelligence
**Takeaways**
- Robots/physical AI can't hold "real memory" because video is extremely token-expensive relative to current LLM/VLM context windows.
- Solution: instead of storing raw video, use a small model to detect the highest "gradient of change" moments and keep only those key frames — compressing ~500,000 tokens of raw video into roughly 1,000 tokens of structured description.
- This frame-selection approach becomes the backbone of their world model's reasoning chain between states.

**Details**
Finn's talk was framed as an engineering-workaround lecture: naive strategies like downsampling didn't work well enough, so the team built a dedicated "delta-detection" model to select memory-worthy frames. [Reference: Physical Intelligence — https://www.physicalintelligence.company/]

---

### 3.4 Sam Altman — OpenAI
**Takeaways**
- His first company (Loopt, a location-sharing app) failed — arguably too early for the market.
- Spent time doing informal favors/odd jobs for YC before becoming YC president himself.
- OpenAI was dismissed as a "charity project" for ~5–6 years until the 2022 ChatGPT moment.
- Was briefly ousted from OpenAI and reinstated days later — framed by speakers as a now-legendary story of resilience.
- Core message: keep building despite criticism; surround yourself with great people.

**Details**
Altman's arc — YC president, ousted from YC, founding OpenAI as a non-profit, years of being overlooked, the 2023 firing/reinstatement — was told as the summit's closing "full circle" story on perseverance. [Reference: OpenAI company story — https://openai.com/about]

---

## 4. Broader Observations

**UK vs. US startup/VC culture**
- British investors are seen as lower risk-appetite than American counterparts; US investors reportedly stay engaged even through early failure, while UK investors may disengage faster.
- GoCardless remains the only British YC unicorn to date — cited repeatedly as a call to action for UK-based founders.
- Comparison drawn to Indian VC roughly 20 years ago in terms of maturity.

**Imperial College's rising profile at YC**
- Only 6–8 YC founders (through 2025) have had Imperial College alumni status — a small number, but growing.
- Attributed partly to Tom Blomfield's personal advocacy for Imperial talent before he left YC for Anthropic.
- Imperial's CS program's heavy "systems" emphasis (build an OS, compiler, distributed system by 3rd year) — championed ~15 years ago by former CS head Paul Kelly — is credited with building unusually strong engineering fundamals.

**YC Startup School**
- Free application-based program (~10–15 questions on background, projects, CV, AI outlook).
- ~2,500 applicants, with about 300 admitted per "season."
- No formal deliverable required afterward — described as pure "enablement" (mentorship, networking, exposure) rather than a structured curriculum.
- [Reference: YC Startup School — https://www.startupschool.org/]

---

## 5. Personal Takeaways / Next Steps (from the conversation)

- Plan to split a six-person friend group into two three-person teams rather than one large, unfocused founding team.
- One sub-team plans to build a "Dependabot for APIs" — an agent-based tool to track and manage breaking API/dependency changes, extending an idea 10 years old (Dependabot) into the agentic-AI era, as suggested directly by Gray Baker.
- Two months of summer allocated to build and test the idea before returning to their master's program — explicitly *not* dropping out, echoing Patrick Collison's "don't chase urgency" advice.

---
