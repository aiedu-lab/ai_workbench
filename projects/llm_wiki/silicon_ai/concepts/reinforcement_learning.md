# Reinforcement Learning

A [[Machine Learning]] paradigm in which an agent learns by
interacting with an environment and receiving reward signals.
Unlike supervised learning, no labelled examples are required —
the agent discovers optimal strategies through trial and error.

## Hardware Connection
RL simulations are computationally expensive: millions of game
episodes or environment steps must run faster than real time.
Before modern [[GPU Computing]], RL was limited to toy problems.

Key milestones gated by hardware:
- **1992:** TD-Gammon — RL for backgammon on 1990s hardware.
- **2013:** Deep Q-Network (DeepMind) — RL + [[Deep Learning]]
  on GPUs achieves human Atari performance.
- **2016:** AlphaGo — RL + [[Deep Learning]] on TPU clusters
  defeats world Go champion; Go's search space ~10¹⁷⁰ positions.
- **2017:** AlphaZero — self-play RL masters chess, shogi, Go
  from scratch in ~9 hours on TPU hardware.

## AlphaGo vs. Deep Blue
[[Deep Blue]] (1997) used exhaustive search + hand-coded heuristics
([[Symbolic AI]]). AlphaGo used RL + [[Deep Learning]] — a
fundamentally different approach. The hardware available in 1997
could not have run AlphaGo's training loop; TPU clusters with
[[Moore's Law]] decades of scaling were required.

## RLHF and LLMs
Reinforcement Learning from Human Feedback (RLHF) is the technique
used to align [[Large Language Models]] (ChatGPT, Claude). It adds
a reward model trained on human preferences to fine-tune the base
LLM — requiring additional GPU compute on top of pre-training.

## Related
- [[Machine Learning]] — paradigm RL belongs to
- [[Deep Learning]] — combined with RL for AlphaGo/AlphaZero
- [[Large Language Models]] — aligned with RLHF
- [[GPU Computing]] — hardware enabling modern RL at scale
- [[Deep Blue]] — predecessor milestone using Symbolic AI, not RL
- [[Transformer Architecture]] — architecture used in modern RL agents
- [[Moore's Law]] — transistor scaling that enabled RL at game-scale
