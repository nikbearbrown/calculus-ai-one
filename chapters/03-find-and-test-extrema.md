# 3. Find and test extrema

*The best point can sit where the derivative is zero, where it breaks, or at the end.*

The tank first fills, then drains, then fills again. If you stop scanning after the first peak, you might recommend the wrong time to read its greatest volume. We need the largest and smallest **over the entire supplied interval**, not just a high and low near the valve switch.

**By the end:** build a candidate set from sign changes, endpoints and points without derivatives; classify local extrema and compare absolute values.

## Use the rate to build a shortlist

Let $V(t)$ be the number of liters in the tank. On each open branch, $V'(t)=q(t)$; Chapter 5 justifies this rule. For $0<t<2$, the flow $6-t^2$ is positive. For $2<t<4$, $2(t-4)$ is negative. For $4<t<7$ it is positive again. Positive derivative implies increase and negative derivative implies decrease on each such interval by the mean value theorem. The theorem compares a secant with a tangent on an interval where the function is continuous on the closed interval and differentiable inside. Split the sign analysis at the switch rather than assuming differentiability through it.

Minute 2 is a local maximum: volume increases just before and decreases just after. Its derivative does not exist. Minute 4 is a local minimum: the derivative is zero and the sign moves from negative to positive. A zero derivative alone does not guarantee an extremum; the function $f(t)=t^3$ increases through the point where $f'(0)=0$. A second derivative can sometimes classify a stationary point; here $V''(4)=2>0$, consistent with the sign change. The first-derivative trace also handles the corner at minute 2.

## Check endpoints as well

A continuous function on a closed bounded interval attains both an absolute maximum and an absolute minimum. The values below follow from accumulation, which the bridge in Chapter 5 derives.

| Candidate time (min) | Volume (L) | Why test it? |
| ---: | ---: | --- |
| 0 | 10 | Left endpoint |
| 2 | $58/3$ | Nondifferentiable switch; local maximum |
| 4 | $46/3$ | Stationary point; local minimum |
| 7 | $73/3$ | Right endpoint |

The absolute minimum is minute 0 and the absolute maximum is minute 7. Compare exact values by putting them over the same denominator. A silent optimization routine that checks stationary points only would find minute 4 and miss both absolute extrema. Even a routine that adds the switch misses the endpoints. The closed interval is part of the question.

## Practice unaided

1. Re-rank the candidates if observations stop at minute 4. Identify the absolute maximum and minimum.
2. Find and classify the stationary point of $g(t)=(t-2)^2$ on $[0,3]$. Compare both endpoints.
3. Suppose a limiter stops the analysis at minute 2 precisely. Does a maximum exist if you use the open interval $(0,2)$? Explain existence rather than just giving a number.

Ask a checker for counterexamples to your candidate list only after writing it. Try the paper route by swapping lists and testing just the missing candidates. [Worked checks](../practice/answer-key.md) · [Next: accumulation](04-accumulate-a-changing-rate.md)
