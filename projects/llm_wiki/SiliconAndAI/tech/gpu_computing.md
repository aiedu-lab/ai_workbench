# GPU Computing

The use of Graphics Processing Units (GPUs) for general-purpose
parallel computation (GPGPU). GPUs contain thousands of smaller
cores suited to parallel matrix operations — the dominant
workload in [[Deep Learning]].

## From Graphics to AI
GPUs were originally designed for 3D graphics rendering (massively
parallel pixel shading). NVIDIA's CUDA platform (2006) made them
programmable for general compute. The end of [[Dennard Scaling]]
(~2005) redirected chip design toward parallelism — perfectly
aligning with GPU architecture and, crucially, with [[Deep
Learning]] matrix operations.

## Transistor Scale (following Moore's Law)
- **2012 GTX 580:** ~3 billion transistors — [[AlexNet]] training
- **2022 A100:** ~54 billion transistors — GPT-3 training
- **2024 H100:** ~80 billion transistors — frontier LLM training
- **2025 GB202:** ~92.2 billion transistors

## The Turning Point: AlexNet (2012)
[[AlexNet]] was trained on two consumer GTX 580 GPUs in a
university lab. Before CUDA GPUs, similar experiments required
months on CPU clusters. GPU compute made the result achievable
in days, enabling rapid experimentation — the feedback loop
that accelerated [[Deep Learning]] adoption.

## Economic Impact
Demand for AI GPU compute created the most valuable chip company
in the world: NVIDIA surpassed $3.3 trillion in market cap in
2024 — the direct economic consequence of [[Moore's Law]] scaling
combined with the [[Deep Learning]] and [[Transformer Architecture]]
revolution.

## Related
- [[Moore's Law]] — transistor growth underpins GPU capability
- [[Dennard Scaling]] — its end drove the shift to GPU parallelism
- [[Deep Learning]] — the dominant workload GPU compute enables
- [[AlexNet]] — first major AI breakthrough on consumer GPUs
- [[Transformer Architecture]] — modern AI running on GPUs
- [[Integrated Circuit]] — the chip GPU is built on
- [[Transistor]] — the unit being scaled in each GPU generation
