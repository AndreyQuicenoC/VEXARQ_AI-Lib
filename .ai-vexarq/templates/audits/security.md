@.ai-vexarq/core/policies.xml
@.ai-vexarq/core/language.xml
@.ai-vexarq/core/finding-contract.xml
@.ai-vexarq/workflows/agents/security-audit.xml

Run a **read-only security review** unless this request also authorizes remediations.

## Binding contracts

- @.ai-vexarq/workflows/agents/security-audit.xml
- @.ai-vexarq/core/finding-contract.xml (severity, evidence, remediation shape)

## Execution instructions

1. Scope review to the paths and environments named below. No destructive testing unless explicitly authorized.
2. Record findings under `docs/qa/` with IDs, severity, evidence, and recommended fix — not a blanket "secure" claim.
3. If fixes are **not** requested, stop after the report. If fixes are requested, route through factory + quality pipeline in a follow-up.
4. Do not push.

## Request metadata

| Field | Value |
| --- | --- |
| Mode | `[review only \| review and fix]` |
| Environment | `[local \| staging \| production-like — no prod creds in chat]` |

## Scope

**Assets in scope:** [Repos, APIs, auth flows, uploads, admin panels.]

**Threat focus:** [OWASP category, compliance, secrets, supply chain.]

**Out of scope:** [Third-party SaaS you cannot inspect.]

---

## Expected output

- Security findings file under `docs/qa/` per finding-contract
- Summary: highest severity, quick wins, and items needing product decision