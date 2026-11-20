@.ai-vexarq/core/policies.xml
@.ai-vexarq/core/language.xml
@.ai-vexarq/core/documentation-governance.xml
@.ai-vexarq/core/quality-pipeline.xml
@.ai-vexarq/workflows/lifecycle/orchestrator.xml

Run the **continuous VEXARQ cycle**: advance phases until the described scope is implemented, with documentation, code, and tests the product needs.

## Binding contracts

- @.ai-vexarq/workflows/lifecycle/orchestrator.xml
- @.ai-vexarq/core/quality-pipeline.xml for any code change

## Execution instructions

1. Mode: **continuo** — after a phase passes self-check, promote per documentation-governance and continue to the next phase without waiting for a new message, until scope is done or a real blocker stops the cycle.
2. Fill gaps as **STANDARD_ASSUMPTION**; never present them as user-confirmed. A blocker on architecture, data, or security stops the cycle.
3. When implementation is in scope, delegate implementation work through the lifecycle rules (user-story or factory paths), not ad hoc coding.
4. Update `docs/vexarq/status.html` after each phase. Do not push. Do not overwrite user-edited current docs. Do not modify `sources/canon/`.

## Authorization

I authorize promoting each self-checked phase to lifecycle `docs/planning|design|quality|development/` paths (or legacy `docs/vexarq/current/` when the project still uses it) and continuing until the scope below is met.

## Product request

**Goal:** [What "done" looks like for this continuous run.]

**Scope:** [Features, modules, environments.]

**Non-goals:** [What must not be built in this run.]

**Starting point:** [Greenfield, or which phase/document already exists.]

---

## Expected output

- Promoted lifecycle documents on the governance paths
- Implementation and tests where phases require them
- Quality pipeline green on the final code SHA before declaring completion
- Status board and a closure summary of assumptions and pending items