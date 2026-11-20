@.ai-vexarq/core/policies.xml
@.ai-vexarq/core/language.xml
@.ai-vexarq/core/documentation-governance.xml
@.ai-vexarq/workflows/lifecycle/orchestrator.xml

Execute **one VEXARQ lifecycle phase** only. Do not open the next phase in this turn.

## Binding contracts

- @.ai-vexarq/workflows/lifecycle/orchestrator.xml
- Format for this phase under `.ai-vexarq/formats/` (agent discovers the file for the phase id)

## Execution instructions

1. Use **only** current or legacy current documents as input (no invented requirements).
2. Mode: **validar**.
3. Write output to `docs/vexarq/preliminary/<phase>/` using the phase format contract.
4. Run phase self-checks from the lifecycle orchestrator. If a mandatory input is missing, stop with a clear list: what is missing, expected path, format file, and how to obtain it (previous phase or template).
5. Do not promote in **validar** unless this request explicitly asks to promote.
6. Do not push.

## Request metadata

| Field | Value |
| --- | --- |
| Phase | `[acercamiento \| srs \| base-de-datos \| backlog \| extendido \| sad \| arquetipo \| implementacion \| entrega \| recomendaciones]` |
| Language | Follow the language of this request unless named otherwise |

## Additional context

[Decisions already made, links, files to treat as source of truth, or substitutes named in this request.]

---

## Expected output

- Phase preliminary document(s) with gaps labeled STANDARD_ASSUMPTION or BLOCKED as appropriate
- Short summary: inputs used, open questions, promotion readiness