# Targeted correction

Load `.ai-vexarq/workflows/factory/orchestrator.xml` and `.ai-vexarq/core/quality-pipeline.xml`.

Scope: frontend, backend, or full-stack.
This is not a lifecycle walk.

1. Reproduce the symptom.
2. Record the root cause.
3. Apply the smallest fix and a regression test.
4. Run the quality pipeline from G-00 after every code change.
5. Append `docs/development/FIX_REGISTER.md` using `.ai-vexarq/formats/development/FIX_REGISTER.md`.
6. Redact secrets, tokens, personal data, and exploit detail.
7. Commit only when asked, through the Git specialist. Do not push.

Request:

[Symptom, expected behavior, and where to look.]
