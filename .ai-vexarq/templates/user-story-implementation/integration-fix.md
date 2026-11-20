@.ai-vexarq/core/policies.xml
@.ai-vexarq/core/language.xml
@.ai-vexarq/core/quality-pipeline.xml
@.ai-vexarq/workflows/user-story-implementation/integrator.xml

Validate and correct the integration of HU-XXX.

## Context

**User story:** HU-XXX — [Title]  
**Problem detected:** [Description of the integration problem]

## References

Read the prior analysis: `docs/development/implementation-report.md` (or legacy `docs/implementation-report.md`) section HU-XXX

## Task

1. Validate the E2E flow according to the shared contract
2. Detect Backend ↔ Frontend incompatibilities
3. Correct minimally if necessary
4. Run integration/E2E tests
5. Update implementation-report and integration-report under `docs/development/`; rerun quality-pipeline after fixes

## Expected output

- E2E flow verified
- Acceptance criteria validated with evidence
- Tests executed
- Final status: COMPLETED or COMPLETED_WITH_PENDING
