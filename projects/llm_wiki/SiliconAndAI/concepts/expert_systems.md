# Expert Systems

AI programs that encode human expertise as hand-crafted rules
("if-then" production rules) to solve domain-specific problems.
Expert systems were the commercial flagship of [[Symbolic AI]] in
the 1980s — and their collapse helped trigger the second [[AI Winter]].

## History
- **1965:** DENDRAL (Feigenbaum, Stanford) — first expert system;
  inferred molecular structure from mass-spectrometry data.
- **1972:** MYCIN (Shortliffe, Stanford) — diagnosed blood infections
  with accuracy rivalling specialists.
- **1980s:** R1/XCON at DEC configured VAX systems; companies spent
  ~$1B/year on expert system development.
- **Late 1980s:** Maintenance costs exploded; rules became brittle
  outside their training domain; hardware limits prevented scaling.
  Japanese Fifth Generation Computer Project (1982–1992) failed to
  deliver promised hardware/software advances. Funding collapsed →
  second [[AI Winter]].

## Why They Failed
Expert systems required human experts to manually encode every rule.
Rules proliferated (XCON had 10,000+) and became unmaintainable.
Crucially, they didn't learn from data — making them the opposite of
[[Machine Learning]]. When [[Moore's Law]] scaling made data-driven
[[Neural Networks]] practical, expert systems became obsolete.

## Hardware Context
Expert systems ran on expensive Lisp machines (symbolic processing
hardware). When commodity x86 CPUs caught up via [[Moore's Law]],
the Lisp machine market collapsed (1987 AI Winter marker). Later,
[[GPU Computing]] didn't benefit expert systems at all — it benefited
[[Deep Learning]], completing the paradigm shift.

## Related
- [[Symbolic AI]] — paradigm expert systems exemplified
- [[AI Winter]] — expert systems' failure triggered the second winter
- [[Machine Learning]] — data-driven paradigm that replaced them
- [[Deep Learning]] — ML at hardware scale; the definitive replacement
- [[Moore's Law]] — commodity hardware that undercut Lisp machines
- [[John McCarthy]] — Symbolic AI founder whose Lisp powered DENDRAL
- [[Marvin Minsky]] — MIT AI Lab leader who championed symbolic systems
