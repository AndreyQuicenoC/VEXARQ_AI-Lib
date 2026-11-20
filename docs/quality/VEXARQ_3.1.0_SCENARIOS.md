# Instruction walk-through — VEXARQ 3.1.0

Status of every row below is WALKTHROUGH-ONLY unless the evidence column says the command ran.

| # | Request | Expected behavior |
| --- | --- | --- |
| 1 | Simple frontend | Factory loads frontend, accessibility, and the quality pipeline. |
| 2 | Backend with a database | Factory loads backend and gates G-10 when migrations exist. |
| 3 | Full-stack | Contract, backend, frontend, integrator, quality pipeline. |
| 4 | User-story batch | Existing batch rules, then the quality pipeline. |
| 5 | Targeted fix, several tries | Fix register appends. The pipeline reruns from G-00. |
| 6–9 | Refactor missing one required document | `BLOCKED — REQUIRED DOCUMENTATION MISSING` and no code edit. |
| 10 | Refactor with all four documents | Baseline, small steps, full rerun, compliance report. |
| 11 | Auth change | CRITICAL or at least security audit at MODERATE. |
| 12 | Slow SQL | Query-performance agent. No invented timings. |
| 13 | Audio | Separate preprocess, transcription, and business logic. |
| 14 | Video | Sampling strategy. No invented latency. |
| 15 | Dashboard | Data-engineering agent. Metric grain required. |
| 16 | Logging | Observability agent. Redaction required. |
| 17 | Commit text | Git agent rejects a vague subject. |
| 18 | Two repositories | One `docs/` per root. |
| 19 | Existing `docs/vexarq/current/` | Legacy path is read when the lifecycle file is absent. |
| 20 | No `docs/` | Create only the directory an artifact needs. |
| 21 | Free-text feature | Execution contract before code. |
| 22 | One-line auth change | Risk dimension can raise the level to CRITICAL. |
| 23 | Override that weakens a control | Warn and require confirmation. |
| 24 | Cost without rates | Ask. Do not invent. |
| 25 | Unverified model price | Mark PROVISIONAL. |
| 26 | Trivial fix | No estimate and no extra diagram. |

The quality-pipeline recovery script is executed separately and is not a walk-through.
