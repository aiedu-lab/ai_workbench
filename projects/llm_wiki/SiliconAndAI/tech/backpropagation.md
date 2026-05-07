# Backpropagation

The algorithm that makes training deep [[Neural Networks]] practical.
Computes gradients of the loss function with respect to every weight
in the network by propagating errors backward through the layers.

## History
- **1986:** [[Geoffrey Hinton]], David Rumelhart, and Ronald Williams
  published the landmark paper showing backprop works for multi-layer
  networks — restarting [[Deep Learning]] research after the first
  [[AI Winter]].
- **1989:** [[Yann LeCun]] applied backprop + CNNs to handwritten
  digit recognition (LeNet precursor) at Bell Labs.
- **2012:** [[AlexNet]] used backprop across 5 conv + 3 FC layers
  on [[GPU Computing|GPUs]], achieving breakthrough ImageNet accuracy.

## Why Hardware Mattered
Before [[GPU Computing]], backprop across even modest networks took
days on CPUs. Two GTX 580 [[GPU Computing|GPUs]] (each ~3B transistors)
made AlexNet's week-long training run feasible. Today, trillion-parameter
models require clusters of H100 GPUs (80B transistors each).

## Relationship to Scaling
Backprop's computational cost scales with network depth and width.
As [[Moore's Law]] doubled transistors, practitioners simply made
networks deeper and wider rather than inventing new algorithms —
the same backprop algorithm runs models millions of times larger
than what Hinton trained in 1986.

## Related
- [[Neural Networks]] — the architecture backprop trains
- [[Deep Learning]] — paradigm enabled by backprop at scale
- [[Geoffrey Hinton]] — popularised modern backprop formulation
- [[Yann LeCun]] — applied backprop to convolutional networks
- [[AlexNet]] — demonstrated backprop at GPU scale
- [[GPU Computing]] — hardware that made large-scale backprop practical
- [[Moore's Law]] — transistor growth that enabled deeper networks
- [[AI Winter]] — the freeze that delayed backprop's impact
