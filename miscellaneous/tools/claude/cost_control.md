# Tokenomics and Cost Control

## Claude Code pricing paths (April 2026)

| Path | Cost | Best for |
|---|---|---|
| Free tier | $0 | Try it out, very light use |
| Pro (monthly) | $20/month | Students, moderate use |
| Pro (annual) | $17/month ($200/year) | Save 15% vs monthly |
| Max 5x | $100/month | Daily heavy use |
| Max 20x | $200/month | Power users, large codebases |
| API pay-as-you-go | $3/$15 per MTok (Sonnet 4.6) | Scripts, occasional use |

## Model cost comparison (API)

| Model | Input | Output | Best use |
|---|---|---|---|
| Haiku 4.5 | $1/MTok | $5/MTok | Simple lookups, subagents |
| Sonnet 4.6 | $3/MTok | $15/MTok | Most coding tasks (default) |
| Opus 4.6 | $5/MTok | $25/MTok | Complex multi-file work only |

## Student and education discounts

* **Anthropic Education Plan** — Free Claude Pro for students, faculty,
  and staff at partner universities. Sign in at `claude.ai` with your
  school email — access is automatic if your university has a
  partnership. Known partners include Northeastern, LSE, Champlain
  College, University of San Francisco. Contact your IT department to
  apply if your school is not yet partnered.
* **Annual billing** — 15% savings ($200/year vs $240/year for Pro)
* **Promotional credits** — Anthropic occasionally grants credits when
  new models launch. Check `claude.ai → Settings → Usage` for active
  offers.
* **No individual student discount codes exist.** Any coupon codes on
  third-party sites are fake. Anthropic's help center confirms this.
* **Lovable student discount** — [50% off Pro at $12.50/month](https://lovable.dev/students)
  for verified students.

## Top 8 cost-saving practices

1. **Use Sonnet for 80% of tasks** — reserve Opus only for complex
   multi-file architecture work
2. **Use `/clear` between unrelated tasks** — accumulated context
   wastes tokens and degrades output quality
3. **Use Plan Mode first** — prevents expensive re-dos; ask Claude
   to plan before coding
4. **Keep CLAUDE.md concise** (100–200 lines max) — it loads every
   session; bloated CLAUDE.md burns tokens before a line is written
5. **Batch small changes into one prompt** — one session with 5
   changes costs far less than 5 separate sessions
6. **Use `-p` flag for scripts** — non-interactive mode exits after
   one response; no idle session overhead
7. **Prompt cache reuse** — for large repeated contexts, caching
   cuts input costs by up to 90% automatically
8. **Set `--max-turns`** in automated scripts — prevents runaway
   agent loops from burning tokens

## Lab cost estimate

A typical student session building the Hello World app:

* Single file generation: ~5,000 tokens ≈ $0.015 at Sonnet rates
* Incremental change + review: ~3,000 tokens ≈ $0.009
* Full exercise end-to-end: well under **$0.10**

For the lab, API pay-as-you-go is the most economical path for
students who are not heavy daily users.