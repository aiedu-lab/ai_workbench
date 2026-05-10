# Machine Learning

A sub-field of AI in which systems improve their performance on a
task through experience (data) rather than explicit programming.
Machine learning displaced [[Symbolic AI]] as the dominant paradigm
when hardware became powerful enough to train large models.

## Core Approaches
- **Supervised learning:** Learn from labelled examples
  (classification, regression).
- **Unsupervised learning:** Find structure in unlabelled data
  (clustering, generative models).
- **[[Reinforcement Learning]]:** Learn by trial-and-error reward
  signals (game play, robotics).
- **[[Deep Learning]]:** ML with many-layer [[Neural Networks]];
  dominant since [[AlexNet]] (2012).

## Hardware Dependence
Early ML (1980s–1990s) worked on small datasets because [[Moore's Law]]
hadn't yet produced the compute needed for large models. The end of
[[Dennard Scaling]] (~2005) redirected chip design toward parallelism,
making [[GPU Computing]] the engine of modern ML.

Key milestones gated by hardware:
- **1990:** LeNet ([[Yann LeCun]]) — feasible on small CPU clusters.
- **2006:** Geoffrey Hinton's deep belief nets — still too slow for
  large data.
- **2012:** [[AlexNet]] on [[GPU Computing|GPUs]] — broke the scale
  barrier; modern ML era begins.
- **2017:** [[Transformer Architecture]] — scaled ML to language at
  GPT/Claude scale.

## Relationship to AI Winter
The first and second [[AI Winter|AI Winters]] were partly caused by
ML algorithms that worked in theory but couldn't be trained at
meaningful scale on the hardware of the day. The ML renaissance of
the 2010s was enabled by [[GPU Computing]] following [[Moore's Law]].

## Related
- [[Deep Learning]] — dominant ML paradigm since 2012
- [[Neural Networks]] — architecture underlying most modern ML
- [[Transformer Architecture]] — ML architecture for language
- [[Reinforcement Learning]] — reward-based ML paradigm
- [[GPU Computing]] — hardware enabling large-scale ML
- [[Moore's Law]] — transistor growth that unblocked ML scaling
- [[Dennard Scaling]] — its end drove GPU-parallel ML workloads
- [[AlexNet]] — inflection point for hardware-enabled ML
- [[Symbolic AI]] — paradigm ML displaced
- [[AI Winter]] — periods when hardware couldn't match ML ambition
