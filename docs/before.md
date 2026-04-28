---
title: Before — Documentation Chaos
hide:
  - toc
---

# Before: Acme Corp Documentation

---

## Acme Corp — `\\acme-corp\shared\documentation\`

!!! warning "17 files · Multiple conflicting versions detected across 3 folders"
    See `README_IMPORTANT_READ_FIRST.pdf` before using anything here.  
    When in doubt — ask. **The filename often lies.**

### 📁 misc

| File | Date | Status |
|---|---|---|
| `README_IMPORTANT_READ_FIRST.pdf` | 2024-09-01 | 📌 PINNED |
| `Meeting_Notes_Arch_Review_Q1_2024.pdf` | 2024-01-15 | FOR REF |
| `Onboarding_Checklist_TODO_INCOMPLETE.pdf` | 2023-01-01 | ❌ INCOMPLETE |

### 📁 architecture

!!! danger "⚠ 4 conflicting versions — unclear which is authoritative"

| File | Date | Status |
|---|---|---|
| `System_Architecture_v1.0.pdf` | 2022-06-14 | ARCHIVED |
| `System_Architecture_v2_DRAFT.pdf` | 2023-02-28 | DRAFT |
| `System_Architecture_v2_FINAL.pdf` | 2023-04-10 | SUPERSEDED |
| `System_Architecture_v3_John_edits_PLEASE_USE_THIS.pdf` | 2024-01-22 | CURRENT (?) |

### 📁 api

!!! warning "⚠ Unclear which version is latest"

| File | Date | Status |
|---|---|---|
| `API_Reference_2022.pdf` | 2022-09-01 | OUTDATED |
| `API_Reference_2024_v2_UPDATED.pdf` | 2024-03-15 | IN REVIEW |
| `API_Reference_LATEST_USE_THIS_ONE!!.pdf` | 2024-08-30 | PROBABLY? |

### 📁 deployment

| File | Date | Status |
|---|---|---|
| `How_to_Deploy_March2024.pdf` | 2024-03-01 | INFORMAL |
| `Deployment_Guide_AWS_v2.pdf` | 2023-05-20 | NEEDS REVIEW |
| `deployment_runbook_FINAL_v3_USE_THIS.pdf` | 2024-06-10 | FINAL (?) |

### 📁 runbooks

!!! danger "⚠ None of these have been fully verified in production"

| File | Date | Status |
|---|---|---|
| `incident-response-DRAFT_do_not_use.pdf` | 2023-11-05 | ❌ DO NOT USE |
| `Runbook_Database_Failover_v1.pdf` | 2023-08-14 | UNVERIFIED |
| `Runbook_Database_Failover_v2_with_Sarahs_comments.pdf` | 2024-01-30 | USE THIS (maybe) |

---

## The problems at a glance

<div class="grid cards" markdown>

-   :material-close-circle:{ style="color:#c0392b" } **No search**

    ---
    Finding anything means scrolling a shared drive or asking a colleague.

-   :material-file-multiple:{ style="color:#c0392b" } **No single source of truth**

    ---
    Multiple versions of the same document, no clear winner.

-   :material-tag-off:{ style="color:#c0392b" } **Status in filenames**

    ---
    `FINAL`, `USE_THIS`, `DRAFT`, `v2_PLEASE_USE_THIS` — in the filename itself.

-   :material-account-question:{ style="color:#c0392b" } **Tribal knowledge**

    ---
    The only reliable way to know which document is correct: ask a person.

</div>

---

## What's missing

| Problem | Impact |
|---|---|
| No search | Engineers ask colleagues instead — interrupting their work |
| No versioning | Can't tell what changed, when, or why |
| No review process | Errors go unnoticed until something breaks in production |
| No ownership | "Last edited by John" — John left 8 months ago |
| Not linked to code | Deployment guide describes infrastructure that no longer exists |

---

[See the After State →](after.md){ .md-button .md-button--primary }
