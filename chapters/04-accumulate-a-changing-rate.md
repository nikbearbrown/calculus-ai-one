# 4. Accumulate a changing rate

*Every panel has a width and a rule. Both choices change the estimate.*

A flow meter reports liters per minute, not liters. For a constant rate $q$, the change across an interval of width $\Delta t$ is $q\Delta t$. For a changing rate, slice the time interval into panels; apply that same idea to each smaller piece. Negative contributions subtract. You are approximating net change, not the total amount that moved in either direction.

**By the end:** compute a midpoint sum, compare it with an exact benchmark, and diagnose a panel that interpolates through a jump.

## Use panels that respect the switch

Let $m_i$ be the midpoint of panel $i$ and $\Delta t_i$ its width. Sum $q(m_i)\Delta t_i$ over all panels. The dimensions are $\mathrm{(L/min)\cdot min=L}$. With one-minute panels on $[0,7]$, take midpoints $0.5,1.5,2.5,3.5,4.5,5.5,6.5$. The first two signed contributions are 5.75 and 3.75 L. The next five are −3, −1, 1, 3, 5 L. Add them to get 14.5 L net. You cannot call this a finishing volume before adding the initial 10 L.

The exact net in the next chapter is $43/3$ L. The midpoint result exceeds it by $1/6$ L. Halve the step to half a minute, still landing at the switch, and the estimate is $115/8=14.375$ L, $1/24$ L above the benchmark. The second branch is linear, so midpoint rectangles integrate it exactly; the first branch bends downward, and the midpoint overestimates there. The fourfold improvement here follows from these aligned grids and these branches. It is not an error bound for any grid or sensor trace.

## Explain the wrong trapezoid

A trapezoid uses endpoint samples. If you feed the common sample $q(2)=-4$ to both adjacent panels, the one-minute trapezoid total is 11 L. On the left side you have joined the first branch to a sample from the second. Using the left branch's approached value of 2 for the panel ending at minute 2 changes that particular panel by $(1/2)(2-(-4))=3$ L. The branchwise estimate becomes 14 L, still $1/3$ L below exact. They are different estimates of the same integral. Changing the rate assigned at one instant does not change the integral of this bounded, piecewise continuous function.

As the largest panel width shrinks, Riemann sums of this particular rate converge to the definite integral. The existence of the limit does not make every finite estimate good. Align breaks, report the rule, and check an exact case before trusting a new step size.

## Practice unaided

1. Compute the one-minute midpoint estimate on $[0,2]$ and compare it to the exact integral $28/3$.
2. Use the linear branch on $[2,4]$ to compute signed area geometrically and with a single midpoint panel.
3. At minute 2 substitute a display-only sample of zero into the unsplit one-minute trapezoid. What net estimate results? Does the exact integral change?

An optional tool may generate panel values. Verify their times and signed contributions against a small table made independently. [Worked checks](../practice/answer-key.md) · [Next: the fundamental theorem](05-connect-change-and-accumulation.md)
