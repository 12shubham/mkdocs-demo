---
tags:
  - Framework
  - Getting Started
---

# Creating New Pages

Step-by-step guide for adding a page to this framework in under 2 minutes.

---

## Step 1 — Create the Markdown file

```bash
# Create a single page
touch docs/my-page.md

# Or create a page inside a section
mkdir -p docs/my-section
touch docs/my-section/my-page.md
touch docs/my-section/index.md     # Section landing page (optional)
```

---

## Step 2 — Add front matter

Every page should start with a YAML front matter block:

```yaml title="docs/my-section/my-page.md"
---
title: My Page Title          # Browser tab title (optional — defaults to H1)
description: >-               # Search & social card description
  A short description of what this page covers.
tags:
  - MyTag
  - AnotherTag
---

# My Page Title

Content goes here.
```

---

## Step 3 — Register in the nav

Open `mkdocs.yml` and add your page to the `nav:` section:

```yaml title="mkdocs.yml"
nav:
  - Home: index.md
  - My Section:                           # (1)
      - Overview: my-section/index.md     # (2)
      - My Page: my-section/my-page.md
```

1. The section title is a plain string — it doesn't need a file unless you want `navigation.indexes` to link it.
2. `index.md` becomes the landing page when you click the section header in the tab bar (requires `navigation.indexes` feature).

!!! tip "Order matters"
    Pages appear in the sidebar in the order they are listed in `nav:`.

---

## Step 4 — Preview instantly

```bash
mkdocs serve
```

Open **[http://127.0.0.1:8000](http://127.0.0.1:8000)** — the browser hot-reloads on every file save. No need to restart the server.

---

## Page Templates

Copy-paste any of these starter templates for common page types.

=== "Standard Page"
    ```markdown
    ---
    tags: [MyTag]
    ---

    # Page Title

    Brief intro — one or two sentences.

    ---

    ## Section One

    Content here.

    ## Section Two

    Content here.
    ```

=== "Reference / API Page"
    ```markdown
    ---
    tags: [Reference]
    ---

    # API Reference: MyEndpoint

    !!! info "Base URL"
        `https://api.example.com/v2`

    ## `GET /resource`

    Returns a list of resources.

    **Query Parameters**

    | Parameter | Type   | Required | Description     |
    |-----------|--------|----------|-----------------|
    | `page`    | int    | No       | Page number     |
    | `limit`   | int    | No       | Results per page |

    **Example**

    \`\`\`bash
    curl -X GET "https://api.example.com/v2/resource" \
      -H "Authorization: Bearer <token>"
    \`\`\`
    ```

=== "How-To / Runbook"
    ```markdown
    ---
    tags: [Runbook, Operations]
    ---

    # How to: Deploy to Production

    !!! warning "Prerequisites"
        - [ ] Access to production cluster
        - [ ] Deployment approved in Jira

    ## Steps

    1. **Check cluster health**

        \`\`\`bash
        kubectl get nodes
        \`\`\`

    2. **Apply manifests**

        \`\`\`bash
        kubectl apply -f k8s/production/
        \`\`\`

    3. **Verify rollout**

        \`\`\`bash
        kubectl rollout status deployment/my-app
        \`\`\`

    !!! success "Done"
        Monitor the deployment at [Grafana Dashboard](#).
    ```

=== "ADR (Architecture Decision)"
    ```markdown
    ---
    tags: [ADR, Architecture]
    ---

    # ADR-001: Use MkDocs for Documentation

    **Status:** Accepted  
    **Date:** 2026-04-23  
    **Deciders:** Engineering Team

    ## Context

    We need a documentation system that engineers will actually use.

    ## Decision

    Use MkDocs with Material theme, managed as code in the same repo.

    ## Consequences

    - ✅ Docs reviewed in PRs alongside code
    - ✅ Auto-deployed on merge
    - ❌ Engineers need to learn basic Markdown
    ```

=== "Changelog Page"
    ```markdown
    ---
    tags: [Changelog, Releases]
    hide: [toc]
    ---

    # Changelog

    ## [2.0.0] — 2026-04-23

    ### Added
    - New feature X
    - New feature Y

    ### Changed
    - Updated Z behaviour

    ### Fixed
    - Resolved bug W
    ```

---

## Folder Conventions

| Pattern | Use for |
|---|---|
| `docs/index.md` | Site home page |
| `docs/<section>/index.md` | Section landing page (links from nav tab) |
| `docs/<section>/<topic>.md` | Individual topic pages |
| `includes/abbreviations.md` | Global abbreviations |
| `docs/assets/` | CSS, images, custom files |
| `docs/javascripts/` | Custom JavaScript |

---

## Adding Images

```bash
# Place images in docs/assets/ or alongside the page
cp my-diagram.png docs/assets/my-diagram.png
```

```markdown
<!-- In your Markdown page -->
![Alt text](../assets/my-diagram.png){ width="600" }

<!-- With a caption using HTML -->
<figure markdown>
  ![Alt text](../assets/my-diagram.png){ width="600" }
  <figcaption>Figure 1 — System architecture</figcaption>
</figure>
```

---

## Excluding a Page from Search

```yaml
---
search:
  exclude: true
---
```

---

[← Framework Overview](index.md){ .md-button }
[All Components →](components.md){ .md-button .md-button--primary }
