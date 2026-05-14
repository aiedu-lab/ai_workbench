# Dennard Scaling

The observation formulated by [[Robert Dennard]] at IBM in 1974
that as MOSFET transistors shrink, their power density stays
constant — so each transistor generation delivers both higher
speed and better energy efficiency simultaneously.

## Mechanism
As transistor dimensions scale by 0.7× per generation:
- Transistor density doubles (area halves)
- Clock speed increases ~40%
- Power per unit area stays constant

This meant that for ~30 years (1974–2005), engineers got free
performance and free efficiency with every new chip generation.

## End of Dennard Scaling (~2005–2010)
Current leakage at nanoscale made power density rise
uncontrollably. Chip designers could no longer simply shrink
transistors to gain free performance. The era of single-core
clock-speed doubling ended.

## Impact on AI Architecture
The end of Dennard Scaling forced a shift from fast single-core
CPUs to many-core parallel architectures — particularly
[[GPU Computing]]. GPUs with thousands of smaller cores proved
ideally suited to [[Deep Learning]] matrix operations, enabling
the 2012 [[AlexNet]] breakthrough.

Without Dennard Scaling's end driving GPU adoption, the
[[Deep Learning]] revolution would have been delayed further.

## Contrast with Moore's Law
[[Moore's Law]] (transistor count doubling) continued after
Dennard Scaling ended. But without Dennard's power benefit,
more transistors no longer automatically meant faster chips —
it meant more parallel cores instead.

## Related
- [[Moore's Law]] — transistor count law; continued after Dennard ended
- [[Robert Dennard]] — formulator
- [[Integrated Circuit]] — substrate of the scaling
- [[Transistor]] — the device being scaled
- [[GPU Computing]] — parallel architecture born from Dennard's end
- [[Deep Learning]] — benefited from GPU parallelism
- [[AI Winter]] — hardware limits contributed to AI stagnation
