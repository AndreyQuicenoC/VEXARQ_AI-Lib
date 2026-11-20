@.ai-vexarq/core/policies.xml
@.ai-vexarq/core/language.xml
@.ai-vexarq/core/documentation-governance.xml
@.ai-vexarq/core/quality-pipeline.xml
@.ai-vexarq/workflows/user-story-implementation/orchestrator.xml

Implement the following User Story using the user-story-implementation multi-agent workflow.

## Execution instructions
1. **Orchestrator** analyzes and classifies the user story, generates the shared contract and execution_plan
2. According to the plan, run ONLY the necessary agents:
   - Backend: @.ai-vexarq/workflows/user-story-implementation/backend.xml
   - Frontend: @.ai-vexarq/workflows/user-story-implementation/frontend.xml
   - Integrator: @.ai-vexarq/workflows/user-story-implementation/integrator.xml
3. Update development docs per @.ai-vexarq/core/documentation-governance.xml (`docs/development/`; legacy `docs/*.md` if the project still uses it)
4. Implement real code; after each change rerun @.ai-vexarq/core/quality-pipeline.xml from G-00
5. Do not declare completion without pipeline evidence on the final SHA
6. Do not stop at analysis alone; produce verifiable changes

---

## User Story

**ID:** HU-XXX

**As** [actor]  
**I want** [action]  
**So that** [benefit]

### Acceptance criteria
1. [Verifiable criterion]
2. [Verifiable criterion]
3. ...

---

## Project context

**Path:** .

**Additional constraints:** None

**Requested scope:** auto (let the Orchestrator classify)

---

## Expected output

- Documentation updated in `docs/development/` (user-stories, code-structure, implementation-report, integration-report) or legacy `docs/` paths when applicable
- Code implemented and working
- Tests executed and passing
- Traceability user story → code → tests → evidence
