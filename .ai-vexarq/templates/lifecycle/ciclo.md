@.ai-vexarq/core/policies.xml
@.ai-vexarq/core/language.xml
@.ai-vexarq/core/documentation-governance.xml
@.ai-vexarq/workflows/lifecycle/orchestrator.xml

Run or continue the **VEXARQ product lifecycle** for the project described below.

## Binding contracts

- Governance and placement: @.ai-vexarq/core/documentation-governance.xml
- Phase order and gates: @.ai-vexarq/workflows/lifecycle/orchestrator.xml

## Execution instructions

1. Detect the user's language and write artifacts in that language unless they name another.
2. Read `docs/vexarq/status.html` and lifecycle folders under `docs/planning/`, `docs/design/`, `docs/quality/`, and legacy `docs/vexarq/current/`.
3. If no cycle exists, start at **acercamiento** (discovery). Otherwise continue from the phase the status board indicates.
4. Mode for this request: **validar** — one phase at a time unless this template is overridden.
5. Produce the phase preliminary under `docs/vexarq/preliminary/`; promote only when gates pass per documentation-governance.
6. When the phase ends, update `docs/vexarq/status.html` and write the phase request report.
7. Do not push. Do not replace a current document the user has already edited. Do not modify `sources/canon/`.

## Request metadata

| Field | Value |
| --- | --- |
| Profile | `[classify if not set: greenfield \| brownfield \| migration]` |
| Roots | `[backend path] [frontend path]` |
| Out of scope | `[e.g. payments, mobile app]` |

## Product request

**Summary:** [One paragraph: problem, users, and success in the user's words.]

**Must-have capabilities:** [Bullet list.]

**Constraints:** [Stack, deadlines, compliance, integrations.]

**Existing assets:** [Repos, databases, APIs, or "none".]

---

## Expected output

- Phase artifact in preliminary (and promoted when self-check passes)
- Updated `docs/vexarq/status.html` (phase, state, links)
- Request report for this turn with blockers, assumptions, and next phase