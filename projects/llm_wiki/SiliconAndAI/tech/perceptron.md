# Perceptron

The earliest trainable single-layer [[Neural Networks|neural network]],
invented by Frank Rosenblatt at Cornell in 1958. The perceptron proved
that a machine could learn from examples — but its hardware limitations
and theoretical critiques triggered the first [[AI Winter]].

## History
- **1958:** Rosenblatt implements the perceptron on an IBM 704 — the
  first machine that could learn to classify inputs by adjusting weights.
- **1960:** Widrow and Hoff introduce the ADALINE, a continuous variant.
- **1969:** [[Marvin Minsky]] and Seymour Papert publish *Perceptrons*,
  proving single-layer networks cannot solve XOR — freezing
  [[Symbolic AI]] as the dominant paradigm and cutting funding
  for connectionist research (first [[AI Winter]]).
- **1986:** [[Geoffrey Hinton]]'s [[Backpropagation]] paper showed that
  multi-layer networks overcome the XOR limitation — rehabilitating
  the perceptron family.

## Hardware Context
Rosenblatt's perceptron ran on room-filling IBM hardware. Modern
neural networks — descended from the same weighted-sum math — run
on chips with 80B+ transistors (see [[GPU Computing]]). The algorithm
barely changed; the hardware improved by a factor of ~10 million.

## Conceptual Significance
The perceptron established the core update rule (adjust weights by
error signal) that persists in every modern network through
[[Backpropagation]]. It also established the pattern of hardware
bottlenecks gating AI capability — the perceptron's limitations were
partly algorithmic, but hardware made experimentation at scale impossible.

## Related
- [[Neural Networks]] — perceptron is the fundamental unit
- [[Backpropagation]] — algorithm that overcame perceptron limits
- [[Marvin Minsky]] — authored the critique that froze funding
- [[Geoffrey Hinton]] — revived connectionism post-*Perceptrons*
- [[Symbolic AI]] — paradigm that filled the vacuum
- [[AI Winter]] — funding freeze triggered partly by Minsky/Papert
- [[GPU Computing]] — hardware that enabled deep multi-layer nets
