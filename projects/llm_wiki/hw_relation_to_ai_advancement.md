# How Hardware Limitations Dictated the Timeline of AI Advancements
The wiki tells a single coherent story: AI's timeline is Moore's Law's timeline.

## Act 1 — The Gap (1956–1974): Algorithms Without Compute
The [[Dartmouth Workshop]] (1956) founded AI with grand ambitions. [[Allen Newell]] and [[Herbert Simon]] predicted human-level machines within 20 years. [[Frank Rosenblatt]] predicted his [[Perceptron]] would "learn, make decisions, and translate languages."

None of it happened — not because the ideas were wrong, but because the hardware wasn't there. By 1976, Hans Moravec had measured the gap precisely: computers were "millions of times too weak." ([[AI Winter]])

## Act 2 — The First Winter (1974–1980): Moore's Law Had Not Run Long Enough
The wiki is explicit: the First AI Winter's "core problem: insufficient compute — directly linked to Moore's Law not yet having delivered enough transistor doublings." ([[AI Winter]])

Funding collapsed. The algorithms sat waiting.

## Act 3 — A False Dawn (1980–1993): Hardware Killed Its Own Boom
[[Expert Systems]] briefly revived AI, growing into a billion-dollar industry by 1988. But the Second AI Winter was itself a hardware story: dedicated Lisp machines "failed to compete with commodity microprocessors following Moore's Law." ([[AI Winter]])

Moore's Law, running on general-purpose chips, made specialised AI hardware uneconomical. The boom collapsed.

## Act 4 — The Algorithms Wait (1986–2012): Backpropagation Without GPUs
[[Backpropagation]] was popularised in 1986. [[Deep Learning]] states plainly: "The algorithms for deep learning existed (in rough form) by the 1980s. What was missing was compute. Moore's Law — the doubling of transistors on integrated circuits every two years — delivered that compute over the following three decades."

The algorithms were correct. They simply had to wait 25 years for Moore's Law to catch up.

## Act 5 — The Unexpected Accelerant (~2005): Dennard Scaling Breaks
Here the wiki records an ironic twist. [[Dennard Scaling]] — which had multiplied Moore's Law gains by making smaller transistors also faster and cooler — collapsed at sub-90 nm. Clock speeds stopped rising; a "power wall" appeared.

The industry's response was to shift to massively parallel GPU designs. The wiki notes: "GPUs — with thousands of small cores — trade single-thread speed for throughput, and that throughput is exactly what neural networks and backpropagation require. The breakdown of Dennard Scaling thus inadvertently accelerated the Deep Learning revolution by pushing hardware toward the architecture AI needed." ([[Dennard Scaling]])

A hardware failure became AI's unlock.

## Act 6 — Breakthrough (2012) and LLMs (2017–present)
Three conditions converged in 2012 ([[Deep Learning]]): GPU compute, large datasets, and mature algorithms. AlexNet won ImageNet by a margin that shocked the field. Moore's Law had finally delivered.

The [[Large Language Models]] note closes the arc: GPT-3 training required "roughly 3,000 GPU-years of compute" and "represents the culmination of 70 years of AI research made possible by 60 years of Moore's Law scaling."

## Compute Evolution vs. AI Timeline

*Grounded in the wiki's [[Moore's Law]], [[AI Winter]],
[[Deep Learning]], [[Dennard Scaling]], [[Large Language Models]],
and [[Artificial Intelligence]] notes.*

---

### Legend

| Symbol | Meaning |
|--------|---------|
| 🔴 **Winter** | Compute too weak; ambition collapsed |
| 🟡 **Research** | Algorithms advancing; hardware catching up |
| 🟢 **Breakthrough** | Compute finally matched ambition |
| ⚡ | Hardware milestone |
| 🧠 | AI milestone |

---

### Timeline

| Period | Process Node / Transistors | Compute State | AI State | Key Event | Verdict |
|--------|---------------------------|---------------|----------|-----------|---------|
| **1943** | Vacuum tubes | Primitive | 🟡 Research | 🧠 Pitts & McCulloch: first mathematical [[Neural Networks\|neural network]] model | Ambition ahead of hardware by decades |
| **1950** | Discrete transistors | Pre-IC era | 🟡 Research | 🧠 [[Alan Turing]] publishes "Computing Machinery and Intelligence"; proposes the [[Turing Test]] | No machine capable of running the test |
| **1956** | ~10³ components/chip | Early transistors | 🟡 Research | 🧠 [[Dartmouth Workshop]] — AI founded. Logic Theorist debuts. Predictions: human-level AI in 20 years | Wildly optimistic; hardware nowhere near |
| **1958** | ~10³ | Early transistors | 🟡 Research | 🧠 [[Frank Rosenblatt]] invents the [[Perceptron]]. Predicts it will "learn, make decisions, translate languages" | Correct idea; no compute to scale it |
| **1965** | ~65 components/chip ([[Gordon Moore\|Moore]]'s baseline) | ⚡ [[Moore's Law]] paper published; projects 65K components by 1975 | 🟡 Research | 🧠 Early AI successes: algebra solvers, theorem provers — all "toys" | Hardware doubling begins its clock |
| **1969** | ~1K–10K | Growing | 🟡 Research | 🧠 [[Marvin Minsky]] & Papert's *Perceptrons* kills neural net funding for a decade | [[Symbolic AI]] wins the funding war |
| **1971** | **2,300 [[Transistors\|transistors]]** (Intel 4004) | ⚡ First [[Microprocessors\|microprocessor]] | 🟡 Research | 🧠 AI still limited to toy problems | Moravec: still millions of times too weak |
| **1974–1980** | ~10K–100K transistors; 6–3 µm nodes | ⚡ [[Moore's Law]] running; [[Dennard Scaling]] multiplying gains | 🔴 **First AI Winter** | 🧠 Lighthill Report; DARPA cuts $3M/yr grants. Core diagnosis: *"computers millions of times too weak"* | **Winter caused directly by hardware gap** |
| **1974** | ~10K | ⚡ [[Dennard Scaling]] formalised by [[Robert Dennard]] | 🔴 Winter | 🧠 — | Each transistor doubling now also yields free speed + efficiency gains |
| **1980–1987** | ~100K–1M transistors; 1–3 µm | ⚡ Commodity [[Microprocessors]] accelerating | 🟢 **Breakthrough (narrow)** | 🧠 [[Expert Systems]] boom; industry grows from millions → billions of dollars | Compute sufficient for rule-based systems; not for learning |
| **1986** | ~1M transistors | ⚡ Hardware improving | 🟡 Research | 🧠 **[[Backpropagation]] popularised** — the training algorithm for deep networks now exists | Algorithm ready. Compute still ~25 years short. |
| **1987–1993** | ~1M–10M transistors | ⚡ Commodity CPUs beating Lisp machines on [[Moore's Law]] curve | 🔴 **Second AI Winter** | 🧠 [[Expert Systems]] collapse; dedicated AI hardware killed by commodity CPUs | **Winter caused by [[Moore's Law]] — cheap CPUs undercut expensive AI chips** |
| **1993–2005** | 10M–100M transistors; 250–90 nm nodes | ⚡ [[Moore's Law]] relentless; [[Dennard Scaling]] still holding | 🟡 Research | 🧠 Statistical [[Machine Learning]] gains ground. 1997: Deep Blue beats Kasparov. | Compute growing; algorithms maturing |
| **~2005** | ~100M–1B transistors; sub-90 nm | ⚡ **[[Dennard Scaling]] breaks down.** Power wall hits. Clock speeds stall. Industry pivots to parallel GPUs | 🟡 Research | 🧠 — | GPU's thousands of parallel cores are exactly what [[Neural Networks]] need — an accidental gift |
| **2012** | **~1B transistors**; 22 nm | ⚡ GPU clusters; AlexNet trained on 2 GPUs | 🟢 **Breakthrough** | 🧠 **[[Deep Learning]] era begins.** AlexNet wins ImageNet by a shocking margin | **Compute finally matched 1986's algorithm — 26 years later** |
| **2017** | ~10B transistors; 10 nm | ⚡ Transformer-optimised GPU hardware | 🟢 **Breakthrough** | 🧠 **[[Transformer Architecture]]** ("Attention Is All You Need"). Parallelism scales perfectly with GPU throughput | Architecture designed to exploit [[Moore's Law]] parallelism |
| **2020** | ~50B transistors; 7 nm | ⚡ GPU clusters; ~3,000 GPU-years for one training run | 🟢 **Breakthrough** | 🧠 **GPT-3** (175B parameters); few-shot learning emerges at scale | [[Large Language Models\|LLMs]] only possible because 60 years of transistor doubling ran |
| **2022** | ~50–100B transistors; 5 nm | ⚡ Specialised AI accelerators (TPUs, H100s) — response to [[Dennard Scaling\|Dennard]] breakdown | 🟢 **Breakthrough** | 🧠 **ChatGPT** triggers current AI investment boom | Dennard's collapse → GPU/TPU architecture → [[Large Language Models\|LLMs]] |
| **2025** | **2 nm** process; trillions of ops/sec | ⚡ [[Moore's Law]] slowing but still running | 🟢 Active | 🧠 Claude 4, Gemini 2, Llama 3 — LLM era in full force | Culmination of 70 years of [[Artificial Intelligence\|AI]] research + 60 years of [[Moore's Law]] |

---

### The Correlation, Visualised as a Curve

```
Compute        ▁▁▂▂▃▃▄▄▅▅▅▅▆▆▆▇▇▇▇▇████████████████  (Moore's Law)
(transistors)
               │                              ↑ Dennard breaks →
               │                              GPU era unlocked

AI State       ──🟡──🟡──🟡──🔴──🟡──🔴──🟡──────🟢──🟢──🟢──🟢──▶
                                ↑      ↑            ↑
               1956           1974   1987          2012
               Dartmouth      1st    2nd           Deep
               Workshop       Winter Winter        Learning

Ambition       ████████████████████████████████████████████████████  (flat — always high)
```

---

### The Three Hardware Mechanisms

| Mechanism | Period Active | Effect on AI |
|-----------|--------------|-------------|
| **[[Moore's Law]]** (transistor doubling every ~2 years) | 1965 → present (slowing) | Set the pace of every AI era boundary |
| **[[Dennard Scaling]]** (free speed + efficiency per shrink) | ~1974 → ~2005 | Multiplied Moore's gains; then its *collapse* pivoted industry to GPUs |
| **GPU parallelism** (post-Dennard response) | ~2007 → present | Delivered the throughput [[Backpropagation]] and [[Transformer Architecture\|transformers]] require |

---

## Summary

> *Every breakthrough above follows a hardware milestone.
> Every winter sits in a period where the transistor count
> had not yet doubled enough. The pace of green-to-red-to-green
> transitions maps directly onto the [[Moore's Law]] doubling curve.*
>
> **Every AI breakthrough happened when compute caught up with
> ambition; every AI winter happened when it hadn't — and the
> pace of both was set entirely by the doubling of transistor
> counts on [[Integrated Circuits]].**
