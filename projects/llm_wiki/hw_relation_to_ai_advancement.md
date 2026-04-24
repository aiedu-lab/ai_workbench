How Hardware Limitations Dictated the Timeline of AI Advancements
The wiki tells a single coherent story: AI's timeline is Moore's Law's timeline.

Act 1 — The Gap (1956–1974): Algorithms Without Compute
The [[Dartmouth Workshop]] (1956) founded AI with grand ambitions. [[Allen Newell]] and [[Herbert Simon]] predicted human-level machines within 20 years. [[Frank Rosenblatt]] predicted his [[Perceptron]] would "learn, make decisions, and translate languages."

None of it happened — not because the ideas were wrong, but because the hardware wasn't there. By 1976, Hans Moravec had measured the gap precisely: computers were "millions of times too weak." ([[AI Winter]])

Act 2 — The First Winter (1974–1980): Moore's Law Had Not Run Long Enough
The wiki is explicit: the First AI Winter's "core problem: insufficient compute — directly linked to Moore's Law not yet having delivered enough transistor doublings." ([[AI Winter]])

Funding collapsed. The algorithms sat waiting.

Act 3 — A False Dawn (1980–1993): Hardware Killed Its Own Boom
[[Expert Systems]] briefly revived AI, growing into a billion-dollar industry by 1988. But the Second AI Winter was itself a hardware story: dedicated Lisp machines "failed to compete with commodity microprocessors following Moore's Law." ([[AI Winter]])

Moore's Law, running on general-purpose chips, made specialised AI hardware uneconomical. The boom collapsed.

Act 4 — The Algorithms Wait (1986–2012): Backpropagation Without GPUs
[[Backpropagation]] was popularised in 1986. [[Deep Learning]] states plainly: "The algorithms for deep learning existed (in rough form) by the 1980s. What was missing was compute. Moore's Law — the doubling of transistors on integrated circuits every two years — delivered that compute over the following three decades."

The algorithms were correct. They simply had to wait 25 years for Moore's Law to catch up.

Act 5 — The Unexpected Accelerant (~2005): Dennard Scaling Breaks
Here the wiki records an ironic twist. [[Dennard Scaling]] — which had multiplied Moore's Law gains by making smaller transistors also faster and cooler — collapsed at sub-90 nm. Clock speeds stopped rising; a "power wall" appeared.

The industry's response was to shift to massively parallel GPU designs. The wiki notes: "GPUs — with thousands of small cores — trade single-thread speed for throughput, and that throughput is exactly what neural networks and backpropagation require. The breakdown of Dennard Scaling thus inadvertently accelerated the Deep Learning revolution by pushing hardware toward the architecture AI needed." ([[Dennard Scaling]])

A hardware failure became AI's unlock.

Act 6 — Breakthrough (2012) and LLMs (2017–present)
Three conditions converged in 2012 ([[Deep Learning]]): GPU compute, large datasets, and mature algorithms. AlexNet won ImageNet by a margin that shocked the field. Moore's Law had finally delivered.

The [[Large Language Models]] note closes the arc: GPT-3 training required "roughly 3,000 GPU-years of compute" and "represents the culmination of 70 years of AI research made possible by 60 years of Moore's Law scaling."

The One-Sentence Summary
Every AI breakthrough happened when compute caught up with ambition; every AI winter happened when it hadn't — and the pace of both was set entirely by the doubling of transistor counts on integrated circuits.
