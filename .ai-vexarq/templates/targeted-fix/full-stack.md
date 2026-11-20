@.ai-vexarq/core/policies.xml
@.ai-vexarq/core/language.xml
@.ai-vexarq/core/quality-pipeline.xml
@.ai-vexarq/workflows/factory/orchestrator.xml

**Targeted correction** on existing code. This is not a full product lifecycle walk.

## Binding contracts

- @.ai-vexarq/workflows/factory/orchestrator.xml (routing and contract)
- @.ai-vexarq/core/quality-pipeline.xml (mandatory completion)
- Fix register format: `.ai-vexarq/formats/development/FIX_REGISTER.md`

## Execution instructions

1. Reproduce the symptom and record environment (branch, command, data shape — redact secrets).
2. Identify root cause; prefer the smallest fix plus a regression test.
3. Scope: **frontend | backend | full-stack** — state which applies below.
4. After every code change, rerun the quality pipeline from G-00.
5. Append `docs/development/FIX_REGISTER.md` with symptom, cause, fix, tests, and residual risk.
6. Redact secrets, tokens, personal data, and exploit detail in reports.
7. Commit only when the user asks (Git specialist). Do not push unless asked.

## Request metadata

| Field | Value |
| --- | --- |
| Scope | `[frontend \| backend \| full-stack]` |
| Severity | `[blocking \| major \| minor]` |

## Problem description

**Symptom:** [What fails, error message, screenshot reference.]

**Expected behavior:** [Correct outcome.]

**Where to look:** [File, endpoint, route, recent change.]

**Reproduction steps:**

1. [Step]
2. [Step]

---

## Expected output

- Fix with regression test
- FIX_REGISTER entry
- Quality pipeline evidence on final SHA