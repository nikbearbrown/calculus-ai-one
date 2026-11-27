# 5. Connect change and accumulation

*The level remembers earlier minutes even when the valve does not.*

Switching the rule for flow does not reset the amount in the tank. A correct formula needs both new local behavior and a carry-forward from what happened earlier. This is where differentiation and integration become checks on each other.

**By the end:** compute an accumulation using antiderivatives, build a continuous volume across a rate jump, and check a switched model against an independent calculation.

## Anchor the accumulation

Let $V(t)=10+\int_0^t q(u)\,du$. The variable $u$ runs through the earlier times; $t$ is the endpoint and remains a parameter. Where $q$ is continuous, the fundamental theorem gives $V'(t)=q(t)$. For small positive $h$, the quotient $[V(t+h)-V(t)]/h$ is the average flow over the small interval. If the rate is continuous at $t$, this average tends to the flow there. The backward quotient gives the same limit. Across the two branches, use definite integrals separately.

For $0\le t\le2$, integrating the first expression gives $V(t)=10+6t-t^3/3$. At the switch, $V(2)=58/3$. Start the second branch from that level, not from 10:
$$
V(t)=\frac{58}{3}+(t-4)^2-4,\qquad 2\le t\le7.
$$
The square is an antiderivative of the linear rate; subtract its value at minute 2 to anchor the new accumulation. This gives $V(4)=46/3$ and $V(7)=73/3$. Differentiate both formulas on their interiors and check that the two expressions give the same volume at 2.

## A corner can preserve the total

Use one-sided secants for positive small $h$. On the left, $[V(2)-V(2-h)]/h=2+2h-h^2/3$ tends to 2 L/min. On the right, $[V(2+h)-V(2)]/h=-4+h$ tends to −4 L/min. Both approaches give the same level at minute 2 because the small integrated amount shrinks with the interval. They do not give the same slope. The assigned $q(2)$ is not the derivative at the corner.

Two further independent checks: the triangular net flow on $[2,4]$ is −4 L and on $[4,7]$ it is +9 L. With $28/3$ L accumulated before switching, the net is $28/3-4+9=43/3$ L. And the sign trace from Chapter 3 predicts a rise, a fall, and another rise. A curve from software that contradicts either check needs investigation.

## Practice unaided

1. Give the exact volume at minute 3 and compare it with the initial volume.
2. Suppose the initial level is raised by two liters but the flow model is unchanged. Which outputs change and which stay the same?
3. Find the earliest minute at which volume returns to its minute-2 peak, **after** minute 2. Verify it using the second branch and explain why the search stops within the supplied interval.

In the [tank worksheet](../practice/worksheet.md), record a first attempt, defend your extrema and reject a bad numerical result. Only then use a peer or optional assistant to critique one step. [Worked checks](../practice/answer-key.md) · [Teaching and transfer](../teaching/README.md)
