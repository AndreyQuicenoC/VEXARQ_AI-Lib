@.ai-vexarq/core/policies.xml
@.ai-vexarq/core/language.xml
@.ai-vexarq/core/documentation-governance.xml
@.ai-vexarq/core/quality-pipeline.xml
@.ai-vexarq/workflows/factory/orchestrator.xml

Implement a change that **does not have to be a user story**. The factory classifies complexity, selects specialists, and holds completion to the quality pipeline.

## Binding contracts

- @.ai-vexarq/workflows/factory/orchestrator.xml
- @.ai-vexarq/workflows/agents/registry.xml (specialists loaded only when routing selects them)
- Execution contract fields defined in the factory orchestrator

## Execution instructions

1. Discover project roots and existing docs (planning, design, quality, development, legacy `docs/vexarq/`).
2. Write **`docs/development/implementation-report.md`** execution contract **before** code: goal, scope, labeled requirements, acceptance criteria, specialists, gates, documents to update.
3. Ambiguities that change architecture, data, or security **block** until clarified; other gaps are INFERENCE or PENDING, never silent CONFIRMED.
4. Implement with the smallest correct change. After each code change, rerun the quality pipeline from G-00.
5. Update `docs/vexarq/status.html` when the factory orchestrator requires it. Do not push unless the user asks.

## Request metadata

| Field | Value |
| --- | --- |
| Domain | `[frontend \| backend \| full-stack \| api \| data \| integration \| infrastructure \| observability \| ai \| documentation]` |
| Complexity hint | `[optional: trivial \| moderate \| critical]` |
| Roots | `[paths]` |

## What to build

**Problem / opportunity:** [Plain description.]

**Acceptance criteria (testable):**

1. [Criterion]
2. [Criterion]

**Interfaces and data:** [APIs, schemas, events, or "unchanged".]

**Security / compliance:** [Auth, PII, payments, or "none".]

**Out of scope:** [Explicit exclusions.]

---

## Expected output

- Execution contract in `docs/development/implementation-report.md`
- Code and tests with quality pipeline evidence on final SHA
- Specialist reports under `docs/qa/` or paths the factory assigns when audits run