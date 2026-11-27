# Worked checks

## Local change

1. **Limits.** $q(0)=6$ and $q(4)=0$, in L/min. Minute 8 is outside the interval. Relabeling the switch sample as 0 leaves the left and right limits 2 and −4, so the two-sided limit still does not exist. As time approaches 7 from the left the rate tends to 6 L/min. No inputs to its right are modeled.
2. **Derivative.** At minute 1.5 the flow is 3.75 L/min, so volume grows. The derivative is −3 L/min², so flow is falling. For the linear branch the difference quotient is $[2(t+h-4)-2(t-4)]/h=2$; for example, flow moves from −2 at minute 3 to 0 at minute 4. For minute 1.2 the tangent predicts $5-2(0.2)=4.6$ L/min; the exact value is 4.56, so estimate minus exact is 0.04 L/min.
3. **Extrema.** On $[0,4]$, 10 L at 0 is the absolute minimum and $58/3$ L at 2 is the absolute maximum. For $(t-2)^2$ on $[0,3]$, its derivative $2(t-2)$ changes from negative to positive at 2, so 0 is the absolute minimum value there; endpoint values 4 and 1 establish the absolute maximum at 0. On $(0,2)$ the tank volume increases strictly and has no attained maximum. Its supremum is $58/3$ L.

## Accumulation

4. **Numerical rules.** On $[0,2]$, 5.75 + 3.75 = 9.5 L, exceeding $28/3$ by $1/6$ L. The negative triangle on $[2,4]$ is $-(2)(4)/2=-4$ L, matching the midpoint rate −2 times width 2. Replacing the unsplit sample −4 with 0 raises the one-minute trapezoid by 4 L to 15 L; exact integration is unchanged.
5. **The fundamental theorem.** Minute 3 has $58/3+1-4=49/3$ L, still above the 10 L start. An extra 2 L at the start shifts the whole volume curve up 2 L; rates, net change, all volume slopes and extremum times stay the same. The minute-2 peak is reached again when $(t-4)^2=4$, giving $t=2$ or 6, so the answer after the switch is 6.

## Worksheet and transfer

The switch has left rate 2, right rate −4, and sample −4 L/min. The first-branch derivative is $-2t$ L/min². The volume is $10+6t-t^3/3$ through 2 and $58/3+(t-4)^2-4$ thereafter. The two volumes meet but the slopes are the two unequal one-sided rate limits. At 0, 2, 4 and 7 the volumes are 10, $58/3$, $46/3$ and $73/3$ L. The absolute minimum is at 0 and the maximum at 7, not at 2.

Split by the switch and the zero: $28/3-4+9=43/3$ L net. One- and half-minute midpoint estimates are 14.5 and 14.375 L, with errors $1/6$ and $1/24$ L. The one-minute trapezoid uses the wrong side of the jump for the last point of the first branch, lowering 14 L to 11 L. Neither is a final volume; adding the 10 L start to the exact net gives $73/3$ L.

In the transfer, $V(2)$ remains $58/3$ L and its right slope is now −2 L/min. The new continuation is $58/3+(t-3)^2-1$. Minute 3 is the stationary local minimum at $55/3$ L. Minute 4 returns to $58/3$ L, because the negative and positive triangles on $[2,3]$ and $[3,4]$ cancel. Minutes 2 and 4 are **both** absolute maximizers on the new interval; minute 0 remains the absolute minimum.
