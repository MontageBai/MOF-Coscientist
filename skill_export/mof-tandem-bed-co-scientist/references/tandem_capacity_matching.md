# Tandem Capacity-Matching Protocol

## Purpose

Calculate a transparent first-pass mass ratio for serial adsorption beds from feed-matched multicomponent single-bed breakthrough curves. The equation allocates downstream mass to the residual duty left by the upstream bed. It does not prove a global optimum.

## Definitions

- `U`: upstream material, evaluated per unit upstream mass.
- `D`: downstream material, evaluated per unit downstream mass.
- `B`: upstream-duty impurity set.
- `G`: downstream residual-duty component set.
- `theta`: breakthrough threshold, such as 0.05.
- `x`: time or another monotonically increasing run coordinate.
- `F_i`: inlet molar flow of component `i`.
- `L_i`: feed load rate on the same normalization basis as `F_i`.
- `y_i(x)=C_i/C_i,0`: normalized outlet response.

Units must close. If `F_i` is mmol min-1 and `x` is min, the curve integral is mmol and must be divided by sorbent mass. If `x` is already min g-1, the result is already mmol g-1 and must not be divided by mass again.

## Common Upstream Cutoff

Find each threshold crossing `x_U,i(theta)` by linear interpolation. Use:

```text
x_B(theta) = min_i x_U,i(theta), i in B
q_U,i(theta) = F_i * integral[0 to x_B] [1-y_U,i(x)] dx
q_U,B(theta) = sum_i q_U,i(theta)
tau_U = q_U,B(theta) / L_B
L_B = sum_i L_i, i in B
```

Also integrate upstream retention of each downstream-duty component `g` to the same cutoff:

```text
q_U,g(theta) = F_g * integral[0 to x_B] [1-y_U,g(x)] dx
b_g,res = max(0, L_g*tau_U - q_U,g)
```

## Downstream Capacity And Ratio

For each candidate downstream material, calculate feed-matched dynamic capacity for every `g`. By default, integrate each component to its own threshold crossing. If the experiment uses a common product cutoff, state and use that alternative consistently.

```text
r_g = b_g,res / q_D,g
m_D/m_U = max_g r_g
m_U/m_D = 1/max_g r_g
```

The component with maximum `r_g` controls the downstream mass. If any required `q_D,g` is zero or unavailable, a finite ratio is not established.

A group-sum form is permitted only if the group members can be treated as interchangeable duty on a justified process basis:

```text
m_D/m_U = sum_g b_g,res / sum_g q_D,g
```

Report that choice explicitly because it can hide a poorly captured individual impurity.

## Numerical Rules

- Sort the run coordinate and reject duplicate or decreasing coordinates unless reconciled.
- Use linear interpolation for threshold crossing and trapezoidal integration.
- Include an interpolated point exactly at the cutoff.
- Do not clamp overshoot by default; report it. A sensitivity analysis may additionally clamp `y` to `[0,1]`.
- Flag no crossing, initial response already above threshold, negative response, overshoot, strong non-monotonicity, and truncated runs.
- State whether capacities are total-bed or mass-normalized.

## Interpretation

The result assumes that single-bed usable capacities transfer to the serial arrangement, the upstream effluent seen by `D` is adequately represented, and sequence interactions are limited. Tandem results may show otherwise. Use experimental discrepancy to update an interpretable utilization factor or test range, not to rewrite the raw capacity.

## Minimum Report

Report data sources and conditions, role sets, threshold, cutoff, integrated capacities, residual duties, controlling component, calculated ratio, quality flags, assumptions, and the separation between equation output and later judgment.
