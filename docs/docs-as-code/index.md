# Documentation as Code

> **Docs as Code** means treating your documentation exactly the same way you treat your source code — written in plain text, stored in Git, reviewed in pull requests, and deployed automatically.

---

## The Core Idea

Traditional documentation lives in wikis, Word documents, or shared drives — isolated from the code it describes. **Docs as Code** brings documentation into the same version-controlled, peer-reviewed, CI/CD-driven workflow as your software.

| Traditional Docs | Docs as Code |
|---|---|
| Word / Confluence / Wiki | Markdown files in Git |
| Manual copy/paste updates | Auto-deployed on every `git push` |
| No review process | Pull Request review |
| Version drift | Always in sync with the codebase |
| Silo'd from engineers | Engineers write & own the docs |

---

## The Three Pillars

=== "1. Plain Text (Markdown)"
    Docs are written in **Markdown** — a simple, human-readable format that is:

    - Easy to learn (no special tools needed)
    - Diff-able in Git (`git diff` shows exactly what changed)
    - Portable across any documentation platform
    - Storable alongside source code in the same repo

    ```markdown
    # My Feature

    This feature does X by calling Y.

    !!! tip
        Use flag `--fast` for better performance.
    ```

=== "2. Version Control (Git)"
    Every documentation change is a commit. This means:

    - Full **history** of who changed what and why
    - **Blame** to find who wrote a particular paragraph
    - **Branches** for drafting new docs in parallel with development
    - **Tags** to snapshot docs for a specific release
    - **Rollback** any change instantly

    ```bash
    # See who last changed a paragraph
    git log -p docs/api-reference.md

    # Create a docs branch alongside a feature branch
    git checkout -b feature/new-api
    # ... write code AND docs together ...
    git push origin feature/new-api
    ```

=== "3. CI/CD (GitHub Actions)"
    Every merge to `main` triggers an automated pipeline that:

    1. Installs MkDocs dependencies
    2. Builds the static site
    3. Deploys to GitHub Pages

    Zero manual steps. Zero stale documentation.

---

## Why It Matters

!!! success "Docs stay in sync with code"
    When a developer changes an API, they update the doc in the **same pull request**. Reviewers catch outdated documentation before it ever ships.

!!! success "Review docs like you review code"
    Pull Request comments, inline suggestions, and approval workflows apply to docs just as they do to code.

!!! success "Anyone can contribute"
    Engineers, PMs, and technical writers all work in the same Markdown files with the same Git workflow they already know.

!!! success "Always deployable"
    Because deployment is automated, the published site is always the latest version of `main` — never stale.

---

**[See the full workflow →](workflow.md)**
