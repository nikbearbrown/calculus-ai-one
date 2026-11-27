# 2. Derive the rate of change

*Divide by the interval before you try to make it vanish.*

On the tank's first branch the net flow decreases from 6 L/min to 5 L/min in the first minute. Average change in the flow is −1 liter per minute per minute. That is not the rate at every instant. If you zoom into the branch around minute 1, the curve changes more rapidly there than that first-minute average suggests.

**By the end:** derive a derivative by taking a limit, distinguish a quantity from its rate, and identify the branch and units to which the derivative applies.

## Take apart the quotient

For a function $f$, use two nearby inputs $t$ and $t+h$. The secant slope is $[f(t+h)-f(t)]/h$ for $h\ne0$. A derivative is the limit of the quotient as $h$ goes to zero, if that limit exists. Use both sides at an interior point. You cannot substitute zero while the denominator is still zero.

Inside the first flow branch, keep $t$ and $t+h$ in that branch. Expanding gives
$$
\frac{[6-(t+h)^2]-[6-t^2]}{h}
=\frac{-2th-h^2}{h}=-2t-h.
$$
The last expression applies for nonzero $h$. Its limit is $q'(t)=-2t$. Since the numerator of the quotient is in L/min and its denominator in min, $q'$ is in $\mathrm{L/min^2}$. The formula gives $-2$ in those units at $t=1$. Substituting $h=0.1$ yields a secant slope of −2.1; $h=-0.1$ yields −1.9. Those values check the algebra independently of the formal limit. The second branch is a line with $q'=2$ on its interior. Neither expression can be installed at the switch by choosing whichever number looks convenient.

## Name the thing changing

At $t=1$, $q(1)=5>0$: volume increases. At the same instant, $q'(1)=-2<0$: flow is declining, so the volume is rising less rapidly. At $t=3$, $q(3)=-2$ shows the tank losing fluid, while $q'(3)=2$ shows the loss rate easing. Confusing quantity, rate and change in rate is a forecasting bug, not a notational preference.

For a differentiable model, the tangent predicts small nearby changes: $q(t+h)\approx q(t)+q'(t)h$. At $t=1$ and $h=0.1$ it predicts 4.8 L/min; the exact value is 4.79 L/min. The difference is the discarded quadratic $-h^2$. This prediction uses a local branch and should not be carried across minute 2.

## Practice unaided

1. At minute 1.5, give $q$, $q'$ and the units of both. Say what each sign means.
2. Derive $q'$ on the second branch from the quotient; check it from two sampled points.
3. Estimate $q(1.2)$ from minute 1 with the tangent and find its signed error, estimate minus exact.

A calculator or model can propose a finite difference after your derivation. Test it with steps on both sides and check that neither crosses the switch. [Worked checks](../practice/answer-key.md) · [Next: extrema](03-find-and-test-extrema.md)
