# VEXARQ paste templates — author contract

Use this when you create or edit templates under `templates/`. Consumer projects paste a template into the agent; the `@` lines are **binding loads**.

## 1. Header (mandatory)

List global contracts first, then the workflow entry, then optional specialists:

```text
@.ai-vexarq/core/policies.xml
@.ai-vexarq/core/language.xml
@.ai-vexarq/workflows/<entry>.xml
```

Add `@.ai-vexarq/core/quality-pipeline.xml` when the task can change code.

Add specialist prompts only in **Execution instructions** when the orchestrator may delegate (same style as user-story `backend.xml`).

Do not write `Load ...` prose instead of `@` paths.

## 2. Body sections (recommended order)

| Section | Purpose |
| --- | --- |
| Title (`#`) | Task name |
| Purpose | One short paragraph |
| Binding contracts | Repeat workflow + formats the agent must obey |
| Execution instructions | Numbered steps; name agents; say what must not happen |
| Request context | Fields with `[example]` placeholders the user overwrites |
| Expected output | Paths, evidence, and completion rule (QPC) |
| Separator `---` | Everything below is user-owned content |

## 3. Language

The template text is English. Generated product text follows `language.xml` from the user's request.

## 4. Completion

Code-changing tasks are done only when `core/quality-pipeline.xml` has no unresolved mandatory gate.

## 5. Missing inputs

Workflows such as refactoring must output `BLOCKED — REQUIRED DOCUMENTATION MISSING` with the table defined in `workflows/refactoring/orchestrator.xml`, not a one-line error.