---
title: After — Docs as Code
hide:
  - toc
---

# After: What the Same Documentation Looks Like

> *"I found it in 3 seconds. The search even highlighted the exact paragraph."*  
> — Same Engineering Lead, Architecture Review Q1 2025

---

## What changed

<div class="grid cards" markdown>

-   :material-magnify:{ style="color:#1E6B8C" } **Full-text search**

    ---
    Every word across every page is indexed. Results appear in milliseconds with highlighted context.

-   :material-source-branch:{ style="color:#1E6B8C" } **One version per topic**

    ---
    One file per topic. Git history shows exactly who changed what, and why, forever.

-   :material-tag:{ style="color:#1A6E43" } **Semantic file names**

    ---
    `architecture/overview.md` — no `FINAL`, `v3_John_edits`, or `USE_THIS_ONE!!` required.

-   :material-account-check:{ style="color:#1A6E43" } **Clear ownership**

    ---
    Every change has an author, a reviewer, and a PR. No more asking if "John's version" is safe.

</div>

---

## Acme Corp — `docs/` (this site)

!!! success "14 pages · One version per topic · Authorship tracked by Git · Reviewed via PR"
    Every page went through a pull request before it was published.  
    **The URL is the single source of truth. No PDFs. No shared drives.**

### 📁 `docs/` (root)

| Page | Replaces | Status |
|---|---|---|
| [`index.md`](index.md) | `README_IMPORTANT_READ_FIRST.pdf` | ✅ Live |

### 📁 `docs/architecture/`

!!! check "Single authoritative page — 4 conflicting PDFs collapsed into one"
    Change history visible in Git. Previous versions are commits, not filenames.

| Page | Replaces | Status |
|---|---|---|
| `architecture/overview.md` | `System_Architecture_v1.0.pdf` | ✅ Live |
| | `System_Architecture_v2_DRAFT.pdf` | ↳ merged |
| | `System_Architecture_v2_FINAL.pdf` | ↳ merged |
| | `System_Architecture_v3_John_edits_PLEASE_USE_THIS.pdf` | ↳ merged |

### 📁 `docs/api/`

!!! check "Three API docs collapsed into one — version tracked by git tag, not filename"

| Page | Replaces | Status |
|---|---|---|
| `api/reference.md` | `API_Reference_2022.pdf` | ✅ Live |
| | `API_Reference_2024_v2_UPDATED.pdf` | ↳ merged |
| | `API_Reference_LATEST_USE_THIS_ONE!!.pdf` | ↳ merged |

### 📁 `docs/deployment/`

| Page | Replaces | Status |
|---|---|---|
| [`deployment/index.md`](deployment/index.md) | `How_to_Deploy_March2024.pdf` | ✅ Live |
| [`deployment/aws.md`](deployment/aws.md) | `Deployment_Guide_AWS_v2.pdf` | ✅ Live |
| `deployment/runbook.md` | `deployment_runbook_FINAL_v3_USE_THIS.pdf` | ✅ Live |

### 📁 `docs/runbooks/`

!!! check "Both runbooks reviewed and approved — no more 'do not use' warnings"

| Page | Replaces | Status |
|---|---|---|
| `runbooks/incident-response.md` | `incident-response-DRAFT_do_not_use.pdf` | ✅ Live |
| `runbooks/database-failover.md` | `Runbook_Database_Failover_v1.pdf` + `_v2_with_Sarahs_comments` | ✅ Live |

### 📁 `docs/misc/`

| Page | Replaces | Status |
|---|---|---|
| `misc/onboarding.md` | `Onboarding_Checklist_TODO_INCOMPLETE.pdf` | ✅ Live |
| `misc/meeting-notes.md` | `Meeting_Notes_Arch_Review_Q1_2024.pdf` | ✅ Archived |

---

## What's fixed

| Problem (Before) | Solution (After) |
|---|---|
| No search | Full-text search across every page |
| No single source of truth | One `.md` file per topic, reviewed via PR |
| No review process | Nothing goes live without a pull request |
| No ownership | Every commit has an author and a message |
| Not linked to code | Docs live in the same repo as the code |
| Version in filename | Version history is Git — dates, diffs, blame |

---

## How it looks

The file tree that replaced 17 PDFs across 5 chaotic folders:

```text
docs/
├── index.md                     ← site home, replaces README_IMPORTANT_READ_FIRST.pdf
├── architecture/
│   └── overview.md              ← replaces 4 conflicting version PDFs
├── api/
│   └── reference.md             ← replaces 3 conflicting API PDFs
├── deployment/
│   ├── index.md                 ← overview
│   ├── aws.md                   ← replaces Deployment_Guide_AWS_v2.pdf
│   └── runbook.md               ← replaces deployment_runbook_FINAL_v3_USE_THIS.pdf
├── runbooks/
│   ├── incident-response.md     ← replaces DRAFT_do_not_use.pdf (reviewed & approved)
│   └── database-failover.md    ← replaces v1 + v2_with_Sarahs_comments
└── misc/
    ├── onboarding.md            ← replaces Onboarding_Checklist_TODO_INCOMPLETE.pdf
    └── meeting-notes.md         ← replaces Meeting_Notes_Arch_Review_Q1_2024.pdf
```

17 PDFs → 14 pages. 5 messy folders → clean semantic tree. Zero ambiguity.

---

<div style="text-align:center; margin-top: 2rem;">

[Set this up for your team →](../framework/index.md){ .md-button .md-button--primary }
[See how it's built →](../framework/create-page.md){ .md-button }

</div>
