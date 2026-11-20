@.ai-vexarq/core/policies.xml
@.ai-vexarq/core/language.xml
@.ai-vexarq/core/documentation-governance.xml
@.ai-vexarq/core/quality-pipeline.xml
@.ai-vexarq/workflows/refactoring/orchestrator.xml
@.ai-vexarq/workflows/user-story-implementation/backend.xml

Backend-only refactor. Same documentation gate and completion rules as the full-stack template.

## Execution instructions

1. Run the **documentation gate** from @.ai-vexarq/workflows/refactoring/orchestrator.xml before any edit.
2. Layer: **backend** — do not change frontend unless this request explicitly includes UI fixes for broken integration.
3. Follow backend agent standards: @.ai-vexarq/workflows/user-story-implementation/backend.xml
4. Quality pipeline after every code change; refactoring reports under `docs/development/`.

## Request metadata

| Field | Value |
| --- | --- |
| Layer | backend |
| Module | `[service, package, or bounded context]` |

## Refactor intent

**Goals:** [e.g. extract service, clarify repository layer, remove duplicate validation.]

**APIs / contracts frozen:** [Endpoints, events, DB schema invariants.]

**Substitutes (optional):** [Named docs only.]

---

## Expected output

- BLOCKED guide or backend refactor with tests and `REFACTORING_*.md` reports