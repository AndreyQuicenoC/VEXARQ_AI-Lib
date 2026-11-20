@.ai-vexarq/core/policies.xml
@.ai-vexarq/core/language.xml
@.ai-vexarq/core/economics.xml
@.ai-vexarq/workflows/economics/estimate.xml

Produce a **cost / effort estimate** for the scope below. Do not implement code in this turn.

## Binding contracts

- @.ai-vexarq/workflows/economics/estimate.xml
- @.ai-vexarq/core/economics.xml (currency, rates, labeling rules)

## Execution instructions

1. Ask for **currency** and **rates** when they are missing. Do not invent commercial numbers.
2. Break work into items with assumptions labeled INFERENCE or PENDING.
3. Write the estimate under `docs/estimates/` using the economics workflow output shape.
4. A trivial one-line fix does not belong in this template — use targeted-fix instead.

## Request metadata

| Field | Value |
| --- | --- |
| Currency | `[USD \| COP \| … or "ask me"]` |
| Rates | `[hourly / story point cost, or "ask me"]` |

## Scope to estimate

**Summary:** [Feature, refactor slice, audit, or phase.]

**Deliverables:** [Code, docs, tests, deployment, training.]

**Constraints:** [Deadline, team size, must-use stack.]

**Exclusions:** [Support, maintenance, license fees.]

---

## Expected output

- Estimate document in `docs/estimates/` with line items, assumptions, and confidence
- Explicit list of unknowns that would change the total