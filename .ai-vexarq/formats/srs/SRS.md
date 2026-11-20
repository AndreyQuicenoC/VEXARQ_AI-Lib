# Software requirements specification

## 1. Introduction

### 1.1 Purpose
Who will use this document and what decision it supports.

### 1.2 Scope
Product name, what it does, and what it does not do. Reference the current project document.

### 1.3 Definitions
Terms that change meaning if left unstated. Include the acronym.

### 1.4 References
Current documents and standards used. A standard is cited by its identifier and year.

## 2. Overall description

### 2.1 Perspective
The system in its context: users and external systems.

### 2.2 Functions
A short list. The detail lives in the numbered requirements.

### 2.3 Actors
Name and responsibility. A role is not a persona with a biography.

### 2.4 Constraints
Technical, legal, and operational constraints that are already confirmed.

### 2.5 Assumptions and dependencies
Each assumption says what happens if it is false.

## 3. Functional requirements

One block per requirement:

- Identifier: `RF-01`.
- Statement: a testable condition.
- Source: actor, rule, or current document.
- Verification criterion: how to tell it is satisfied.
- Priority: only when the user or the source set it. Otherwise, pending.

## 4. Business rules

`RN-01`. The rule, the condition, and the requirement it affects. A literal message stays in quotation marks and is not paraphrased.

## 5. External interface requirements

Users, software, and data. Omit a subsection when the product does not have that interface.

## 6. Quality requirements

Only the ISO/IEC 25010:2023 characteristics that apply. Each one has a scenario and a measurement or an acceptance condition.

## 7. Data

Entities or documents the requirements need, without turning this section into the physical model.

## 8. Traceability

| Rule | Requirement | Verification | Story |
| --- | --- | --- | --- |
| RN-01 | RF-01 | criterion | filled in the backlog phase |

## 9. Open questions

What prevents a requirement from being verified. Do not close them with an invention.

## 10. Baseline and brownfield constraints

Current system behavior that this specification must preserve, and constraints of the existing project. Separate confirmed behavior from inference.

## 11. Security requirements

Controls the product needs, mapped to a named OWASP list and year. Each control has a verification criterion. Do not copy findings from another product.

## 12. Usability and accessibility

WCAG 2.2 AA unless the user set another level. Include the acceptance checks for the release gate.

## 13. Privacy, retention, and compliance

Data classes, retention, deletion, and the rule that applies. A missing legal basis stays pending.

## 14. Deployment, operation, and rollback

What must be true to deploy, operate, and roll back. Commands belong to the runbook after they exist in the repository.

## 15. Release acceptance and deferred work

Acceptance criteria for the requested release, and work explicitly left out.

## 16. Approval

Names and dates stay empty until a person signs. The model does not sign.
