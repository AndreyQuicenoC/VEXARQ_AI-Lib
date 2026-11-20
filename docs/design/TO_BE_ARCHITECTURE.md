# TO-BE architecture — VEXARQ 3.1.0

- Id: TO-BE-3.1.0
- Status: CURRENT
- Date: 2026-11-20
- Depends on: AS-IS-3.0.0

## Decision

Option A. Drafts stay in `docs/vexarq/preliminary/`. A promoted document is written to its lifecycle directory. `docs/vexarq/current/INDEX.md` points at it. If the new file is missing, readers use the 3.0.0 path. Migration of a consumer project uses `git mv` and asks first.

## Flow

The factory orchestrator classifies the request and delegates to the lifecycle orchestrator, the user-story engine, the refactoring engine, or a descriptive execution contract. Specialists are loaded from `workflows/agents/registry.xml`. The quality pipeline is the only done decision.

## Rejected agents

Supply-chain checks stay in the security audit. API conformance stays with the integrator. A separate architecture-compliance agent would duplicate the refactoring gate.

## Diagram

`docs/design/diagrams/to-be.mmd`. Syntax was not validated with mermaid-cli in this change.

## Roadmap

Dependency-aware incremental gate reruns are not part of 3.1.0.
