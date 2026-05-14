# Transformer Architecture

A deep learning architecture introduced in 2017 by Google
researchers ("Attention Is All You Need"). Uses a self-attention
mechanism to model relationships between all positions in a
sequence simultaneously, replacing recurrent networks (RNNs).

## Origin
Proposed by Vaswani et al. at Google Brain in 2017.
Self-attention allows the model to weigh the importance of every
token relative to every other — capturing long-range dependencies
far more efficiently than RNNs or LSTMs.

## Silicon–AI Connection
Transformer training scales with compute in a predictable
"scaling law": more parameters + more data + more compute
yield reliably better models. This direct coupling between
hardware and capability made [[Moore's Law]]-driven GPU scaling
the critical bottleneck for AI in the 2020s:
- NVIDIA's market cap surpassed $3.3 trillion in 2024 as demand
  for transformer training GPUs surged.
- The [[Large Language Models]] era is directly gated by GPU
  compute following [[Moore's Law]].

## Key Applications
- GPT series (OpenAI) — language generation; ChatGPT (2022)
  gained 100M users in two months
- Claude (Anthropic) — language understanding and reasoning
- Gemini (Google) — multimodal AI
- AlphaFold (DeepMind) — protein structure prediction
  (2024 Nobel Prize in Chemistry)

## Preceded By
The [[AlexNet]] 2012 breakthrough triggered the [[Deep Learning]]
era using CNNs. Transformers superseded CNNs for language tasks.
[[Geoffrey Hinton]]'s [[Backpropagation]] (1986) is the training
algorithm that makes transformers trainable.

## Related
- [[Deep Learning]] — the broader field
- [[Large Language Models]] — built on transformer architecture
- [[GPU Computing]] — primary hardware for training transformers
- [[Moore's Law]] — hardware scaling that enables LLM growth
- [[Neural Networks]] — ancestor architecture
- [[AlexNet]] — 2012 precursor that started the deep learning era
- [[Geoffrey Hinton]] — foundational backpropagation work
