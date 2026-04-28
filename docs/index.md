---
hide:
  - toc
  - navigation.footer
---

<div class="hero-strip" markdown>

# Did you know there's a more efficient way to manage and share project documentation?

Replace scattered Word docs, outdated SharePoint pages, and version confusion with a
**single searchable portal** — reviewed like code, deployed in under 60 seconds, and always current.

[See the Live Demo](#live-demo){ .md-button .md-button--primary }
[Get Started](framework/index.md){ .md-button }

</div>

---

## The Problem

<div class="grid cards" markdown>

-   :material-close-circle:{ .lg .middle style="color:#c0392b" } **Scattered Word docs or PDFs**

    ---
    Files emailed around, saved to desktops, duplicated across shared drives.  
    No one knows which copy is authoritative.

-   :material-clock-alert:{ .lg .middle style="color:#c0392b" } **Outdated SharePoint pages**

    ---
    Last updated two years ago. Half the links are broken.  
    Engineers stop trusting it and ask colleagues instead.

-   :material-file-multiple:{ .lg .middle style="color:#c0392b" } **Version confusion**

    ---
    Four copies of the architecture doc.  
    One named `System_Architecture_v3_John_edits_PLEASE_USE_THIS.pdf`.

-   :material-account-question:{ .lg .middle style="color:#c0392b" } **Tribal knowledge**

    ---
    "Just ask Sarah" — if she's not in a meeting.  
    Runbooks that have never been tested in production.

</div>

> *"I can never find anything. Where do we even keep our docs?"*  
> — Engineering Lead, Architecture Review Q1 2024

---

## The Solution

<div class="grid cards" markdown>

-   :material-language-markdown:{ .lg .middle style="color:#1E6B8C" } **Markdown as Code**

    ---
    Write docs alongside source code with **built-in version control**.  
    Any editor, any OS, zero vendor lock-in.

-   :material-pipe:{ .lg .middle style="color:#1E6B8C" } **Automated Pipelines**

    ---
    GitHub Actions **automatically builds and publishes** on every commit.  
    From merge to live site in under 60 seconds.

-   :material-book-open-page-variant:{ .lg .middle style="color:#1E6B8C" } **MkDocs Portal**

    ---
    A clean, **searchable documentation portal** with full-text search,
    tag taxonomy, and structured navigation — out of the box.

-   :material-source-pull:{ .lg .middle style="color:#1E6B8C" } **PR-Reviewed**

    ---
    Documentation changes go through the same **pull request workflow** as code.  
    Quality enforced by default — no more stale or unreviewed docs.

</div>

---

## End-to-End Pipeline

```mermaid
graph LR
    A["✏️ Write Markdown"] --> B["git push"]
    B --> C["Open Pull Request"]
    C --> D["Review & Merge"]
    D --> E["CI/CD Builds"]
    E --> F["🌐 Live in <60s"]

    style A fill:#2D2926,stroke:#2D2926,color:#fff
    style B fill:#2D2926,stroke:#2D2926,color:#fff
    style C fill:#1E6B8C,stroke:#1E6B8C,color:#fff
    style D fill:#1E6B8C,stroke:#1E6B8C,color:#fff
    style E fill:#FD5108,stroke:#FD5108,color:#fff
    style F fill:#1a6e43,stroke:#1a6e43,color:#fff
```

---

## Why It Matters

<div class="grid cards" markdown>

-   :material-check-circle:{ .lg .middle style="color:#1a6e43" } **Always up-to-date**

    ---
    No more "which version is correct?" — docs are tied to every code release automatically.

-   :material-check-circle:{ .lg .middle style="color:#1a6e43" } **Easy to maintain and collaborate on**

    ---
    Same PR workflow as code review. Engineers already know how to contribute.

-   :material-check-circle:{ .lg .middle style="color:#1a6e43" } **Professional, searchable portal**

    ---
    Full-text search, tag taxonomy, structured navigation — all included.  
    No Ctrl+F through PDFs.

-   :material-check-circle:{ .lg .middle style="color:#1a6e43" } **Platform flexibility**

    ---
    Deploy to Azure, AWS, GCP, or GitHub Pages.  
    Switch targets with a single config change.

</div>

---

## Deployment Options

<div class="grid cards" markdown>

-   :material-microsoft-azure:{ .lg .middle style="color:#0078D4" } **Azure**

    ---
    [Azure Static Web Apps](deployment/azure.md) — global CDN, free tier, custom domains, automatic HTTPS.

-   :material-aws:{ .lg .middle style="color:#FF9900" } **AWS**

    ---
    [S3 + CloudFront](deployment/aws.md) — enterprise scale, fine-grained IAM, geographic restrictions.

-   :material-google-cloud:{ .lg .middle style="color:#4285F4" } **GCP**

    ---
    [Cloud Storage](deployment/gcp.md) — scalable static hosting backed by Google's global network.

-   :material-github:{ .lg .middle } **GitHub Pages**

    ---
    [GitHub Pages](deployment/github.md) — zero config, built-in free hosting, deploys with one command.

</div>

---

## Live Demo { #live-demo }

See the difference between before and after docs-as-code — both states are live.

=== ":material-close-circle:{ style='color:#c0392b' } Before"

    **[Open the Before State →](before.md){ .md-button }**

    | Folder | Problem |
    |---|---|
    | `architecture/` | 4 versions — `PLEASE_USE_THIS`, `DRAFT`, `FINAL`, `ARCHIVED` |
    | `api/` | `USE_THIS_ONE!!` — but 3 files, no clear winner |
    | `deployment/` | `FINAL_v3_USE_THIS` and `INFORMAL` and `NEEDS REVIEW` |
    | `runbooks/` | None verified. One says `DO NOT USE`. |

    No search. Status lives in the filename. The only way to know which is correct: ask someone.

=== ":material-check-circle:{ style='color:#1a6e43' } After — This Site"

    **You're looking at it.**

    | What changed | How |
    |---|---|
    | Single source of truth | Git — one version, full history |
    | Always current | Auto-deploys on every push to `main` |
    | Searchable | Press ++slash++ to try it |
    | Reviewed | Every change goes through a pull request |
    | Navigable | Structure lives in `mkdocs.yml`, not filenames |

    [Explore the Framework →](framework/index.md){ .md-button .md-button--primary }
    [Deployment Guides →](deployment/index.md){ .md-button }

---

## Get Started

Everything you need to adopt this as a reusable service — from spinning up a new site to going live.

=== ":material-rocket-launch: Quick Start"

    ```bash title="Clone and run locally"
    git clone https://github.com/12shubham/mkdocs-demo my-docs
    cd my-docs
    pip install -r requirements.txt
    mkdocs serve
    # → http://127.0.0.1:8000  (hot-reloads on every save)
    ```

    ```bash title="Build for production"
    mkdocs build
    # Outputs to site/ — ready to deploy to any static host
    ```

=== ":material-file-plus: Create a Page"

    ```bash title="Create the file"
    mkdir -p docs/my-section
    touch docs/my-section/my-page.md
    ```

    ```yaml title="Add front matter"
    ---
    title: My Page Title
    description: Brief description for search and social cards.
    tags:
      - MyTag
    ---

    # My Page Title

    Content goes here.
    ```

    ```yaml title="Register in mkdocs.yml nav"
    nav:
      - My Section:
          - Overview:  my-section/index.md
          - My Page:   my-section/my-page.md
    ```

    [Full Page Creation Guide →](framework/create-page.md){ .md-button }

=== ":material-cog: Manage the Site"

    | File | What it controls |
    |---|---|
    | `mkdocs.yml` | Site name, nav, theme, plugins — everything |
    | `docs/assets/extra.css` | Brand colours mapped to Material CSS variables |
    | `docs/javascripts/mermaid-config.js` | Mermaid diagram palette |
    | `includes/abbreviations.md` | Hover tooltips on every page |
    | `requirements.txt` | Pinned Python packages — identical builds everywhere |

    [Framework Reference →](framework/reference.md){ .md-button }

=== ":material-cloud-upload: Deploy"

    Push to `main` — GitHub Actions handles the rest automatically.

    | Target | Guide |
    |---|---|
    | :material-github: GitHub Pages | [deployment/github.md](deployment/github.md) |
    | :material-microsoft-azure: Azure Static Web Apps | [deployment/azure.md](deployment/azure.md) |
    | :material-aws: AWS S3 + CloudFront | [deployment/aws.md](deployment/aws.md) |
    | :material-google-cloud: GCP Cloud Storage | [deployment/gcp.md](deployment/gcp.md) |

    !!! tip "Security best practice"
        Use **OIDC federation** (GitHub → Azure/AWS/GCP) instead of long-lived secrets.
        No credentials stored in GitHub — the cloud provider issues short-lived tokens per run.

