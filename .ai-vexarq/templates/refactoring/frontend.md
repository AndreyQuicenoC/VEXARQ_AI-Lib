@.ai-vexarq/core/policies.xml
@.ai-vexarq/core/language.xml
@.ai-vexarq/core/documentation-governance.xml
@.ai-vexarq/core/quality-pipeline.xml
@.ai-vexarq/workflows/refactoring/orchestrator.xml
@.ai-vexarq/workflows/user-story-implementation/frontend.xml

Frontend-only refactor. Same documentation gate and completion rules as the full-stack template.

## Execution instructions

1. Run the **documentation gate** from @.ai-vexarq/workflows/refactoring/orchestrator.xml before any edit.
2. Layer: **frontend** — do not change backend contracts unless this request explicitly authorizes API changes in the SRS.
3. Follow frontend agent standards: @.ai-vexarq/workflows/user-story-implementation/frontend.xml
4. Quality pipeline after every code change; refactoring reports under `docs/development/`.

## Request metadata

| Field | Value |
| --- | --- |
| Layer | frontend |
| Module | `[app area, feature folder, design system]` |

## Refactor intent

**Goals:** [e.g. split components, state cleanup, a11y fixes without UX change.]

**UX / behavior frozen:** [Screens, flows, acceptance from SRS or backlog.]

**Substitutes (optional):** [Named docs only.]

---

## Expected output

- BLOCKED guide or frontend refactor with tests and `REFACTORING_*.md` reports