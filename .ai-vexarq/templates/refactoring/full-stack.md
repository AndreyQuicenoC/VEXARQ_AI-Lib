@.ai-vexarq/core/policies.xml
@.ai-vexarq/core/language.xml
@.ai-vexarq/core/documentation-governance.xml
@.ai-vexarq/core/quality-pipeline.xml
@.ai-vexarq/workflows/refactoring/orchestrator.xml

Refactor existing code **without changing agreed behavior**, unless this request explicitly allows contract changes.

## Binding contracts

- Documentation gate and BLOCKED message shape: @.ai-vexarq/workflows/refactoring/orchestrator.xml
- Specialists when needed:
  - @.ai-vexarq/workflows/user-story-implementation/backend.xml
  - @.ai-vexarq/workflows/user-story-implementation/frontend.xml
  - @.ai-vexarq/workflows/user-story-implementation/integrator.xml

## Execution instructions

1. **Gate first:** locate SRS, SAD, backlog, and test strategy. If any is missing, output the full **BLOCKED — REQUIRED DOCUMENTATION MISSING** message (all sections in the orchestrator). Do not edit code.
2. Record baseline: run quality pipeline and note failing tests before structural changes.
3. Layer for this request: **full-stack** (shared contract → backend → frontend → integrator when UI exists).
4. Plan small, behavior-preserving steps; add characterization tests where coverage is weak.
5. After each code change, rerun quality pipeline from G-00.
6. Write `docs/development/REFACTORING_ASSESSMENT.md` and `docs/development/REFACTORING_COMPLIANCE_REPORT.md` using `.ai-vexarq/formats/development/REFACTORING.md`.
7. A substitute document counts only if **named in this request**. Do not push unless asked.

## Request metadata

| Field | Value |
| --- | --- |
| Layer | full-stack |
| Module / area | `[e.g. auth, billing API, checkout UI]` |
| Substitutes (optional) | `[path or title, if any]` |

## Refactor intent

**Goals:** [e.g. reduce coupling, split module, rename for clarity, performance without behavior change.]

**Behavior that must stay the same:** [User-visible flows, API contracts, SLA, or link to SRS section.]

**Known debt:** [Hot spots, hacks, missing tests.]

**Non-goals:** [Rewrites, version bumps, feature work.]

---

## Expected output

- If blocked: structured missing-doc guide per orchestrator (no code diff)
- If allowed: incremental commits-ready changes, tests, refactoring reports, QPC green on final SHA