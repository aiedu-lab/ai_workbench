# Large Language Models

Neural language models with billions to trillions of parameters,
trained on internet-scale text using the [[Transformer Architecture]].
LLMs represent the current frontier of AI capability — and the
most direct demonstration that [[Moore's Law]] hardware scaling
translates to qualitative leaps in intelligence.

## Milestones
- **2017:** [[Transformer Architecture]] (Vaswani et al., Google) —
  the architectural foundation.
- **2018:** BERT (Google) — bidirectional transformer for understanding.
- **2019:** GPT-2 (OpenAI, 1.5B parameters) — coherent text generation.
- **2020:** GPT-3 (OpenAI, 175B parameters) — few-shot learning
  emergent capability; trained on ~1,000 A100 [[GPU Computing|GPUs]].
- **2022:** ChatGPT — LLM + RLHF (Reinforcement Learning from Human
  Feedback) → mass-market AI product.
- **2024:** GPT-4, Claude 3 Opus, Gemini Ultra — trillion-parameter
  scale; multimodal (text + vision).

## Hardware Requirements
LLMs are the most compute-intensive workloads ever built:
- GPT-3: ~3.14 × 10²³ FLOPs to train — required A100 cluster.
- GPT-4-class: estimated 10²⁵ FLOPs — required H100 cluster
  (80B [[Transistor|transistors]] per chip).
- Inference: billions of users × billions of tokens =
  permanent demand driver for [[GPU Computing]].

## Silicon-AI Loop
LLMs close the feedback loop that [[AlexNet]] opened:
```
Moore's Law → GPU scale → LLM capability →
LLM demand → GPU demand → Moore's Law investment
```
NVIDIA's $3.3T market cap (2024) is the economic signal of this loop.

## Related
- [[Transformer Architecture]] — the architecture LLMs are built on
- [[Deep Learning]] — paradigm LLMs extend
- [[GPU Computing]] — hardware LLMs require
- [[Moore's Law]] — transistor scaling enabling each LLM generation
- [[AlexNet]] — the earlier inflection point that started the loop
- [[Machine Learning]] — broader field LLMs belong to
- [[Neural Networks]] — architecture underlying LLMs
- [[Reinforcement Learning]] — RLHF used to align LLMs
