# AS-IS assessment — VEXARQ 3.0.0

- Id: AS-IS-3.0.0
- Status: CURRENT
- Date: 2026-11-20
- Scope: library repository at `main` `be24084`

## What exists

`.ai-vexarq/` is a portable prompt library. XML prompts, Markdown contracts, one CSV backlog contract, and an HTML tracker. The lifecycle orchestrator has ten phases. The user-story engine has an orchestrator, backend, frontend, and integrator, with V1/V2 and adaptive complexity from TRIVIAL to COMPLEX. Preliminaries live in `docs/vexarq/preliminary/`. The next phase reads `docs/vexarq/current/`. Gates G1–G5 govern promotion and push. Two canon files generate the backlog and the archetype.

## Strengths

Lineage, language policy, canonical generators, and the rule that a test not run is not a pass.

## Gaps

A specialist could finish after a partial test rerun. There is no single gate state machine. Documents are grouped by the `docs/vexarq/` tree, not by lifecycle responsibility. Refactoring does not require the SRS, SAD, backlog, and test document. There is no cost model, no specialist registry, and no fix register. The license is MIT.

## Protected

`sources/canon/backlog-hu-generator.md` and `sources/canon/archetype-prompt.xml`.

## Diagram

`docs/design/diagrams/as-is.mmd`. Syntax was not validated with mermaid-cli in this change.
