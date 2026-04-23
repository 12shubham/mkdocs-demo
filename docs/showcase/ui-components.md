---
tags:
  - Showcase
  - UI
  - Components
---

# UI Components

All interactive and visual UI components available in this framework.

---

## Grid Cards

Standard card grid — 4-column on desktop, stacks on mobile.

<div class="grid cards" markdown>

-   :material-rocket-launch:{ .lg .middle } **Deploy anywhere**

    ---
    GitHub Pages, AWS, Azure, GCP — all CI/CD configs included.

    [:octicons-arrow-right-24: Deployment guides](../deployment/index.md)

-   :material-palette:{ .lg .middle } **Full brand control**

    ---
    CSS variables, dark/light mode, custom fonts — one file to change.

-   :material-magnify:{ .lg .middle } **Instant search**

    ---
    Full-text search with autocomplete and search term highlighting.

-   :material-chart-timeline:{ .lg .middle } **Rich diagrams**

    ---
    Mermaid flowcharts, Gantt, sequence, ER, timelines — all rendered in-browser.

    [:octicons-arrow-right-24: Diagram showcase](diagrams.md)

</div>

**Syntax:**
```html
<div class="grid cards" markdown>

-   :material-icon:{ .lg .middle } **Card Title**

    ---
    Description text.

    [:octicons-arrow-right-24: Link](url)

</div>
```

---

## Two-Column Grid

<div class="grid" markdown>

:material-check-circle:{ .lg } **Left column content**

Some text that sits in the left half of a two-column layout.

:material-check-circle:{ .lg } **Right column content**

Some text that sits in the right half of a two-column layout.

</div>

---

## Buttons

[Primary button](index.md){ .md-button .md-button--primary }
[Secondary button](index.md){ .md-button }
[:material-github: GitHub](https://github.com/12shubham/mkdocs-demo){ .md-button }

**Syntax:**
```markdown
[Primary](url){ .md-button .md-button--primary }
[Secondary](url){ .md-button }
[:material-github: With icon](url){ .md-button }
```

---

## Content Tabs

=== ":material-language-python: Python"
    ```python
    import mkdocs
    ```

=== ":fontawesome-brands-js: JavaScript"
    ```javascript
    const mkdocs = require('mkdocs');
    ```

=== ":simple-docker: Docker"
    ```dockerfile
    FROM squidfunk/mkdocs-material
    COPY . /docs
    ```

!!! tip "Linked tabs"
    All tab groups with matching labels sync across the page — enabled via `content.tabs.link` in `mkdocs.yml`.

---

## Icons

=== "Material Design"
    :material-home: `:material-home:`  
    :material-rocket-launch: `:material-rocket-launch:`  
    :material-cloud-upload: `:material-cloud-upload:`  
    :material-shield-check: `:material-shield-check:`  
    :material-cog: `:material-cog:`  
    :material-chart-line: `:material-chart-line:`

=== "FontAwesome"
    :fontawesome-brands-github: `:fontawesome-brands-github:`  
    :fontawesome-brands-aws: `:fontawesome-brands-aws:`  
    :fontawesome-brands-docker: `:fontawesome-brands-docker:`  
    :fontawesome-brands-python: `:fontawesome-brands-python:`  
    :fontawesome-solid-terminal: `:fontawesome-solid-terminal:`

=== "Octicons"
    :octicons-repo-24: `:octicons-repo-24:`  
    :octicons-git-pull-request-24: `:octicons-git-pull-request-24:`  
    :octicons-check-circle-fill-24: `:octicons-check-circle-fill-24:`  
    :octicons-arrow-right-24: `:octicons-arrow-right-24:`

=== "Simple Icons"
    :simple-docker: `:simple-docker:`  
    :simple-kubernetes: `:simple-kubernetes:`  
    :simple-terraform: `:simple-terraform:`  
    :simple-amazonaws: `:simple-amazonaws:`  
    :simple-microsoftazure: `:simple-microsoftazure:`

Search all icons: [squidfunk.github.io/mkdocs-material/reference/icons-emojis](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/)

---

## Emoji

:wave: :rocket: :fire: :white_check_mark: :x: :bulb: :warning: :lock: :key: :tada:

**Syntax:** `:emoji_name:` — same as GitHub emoji syntax.

---

## Task Lists

- [x] Configure brand colours in `extra.css`
- [x] Set up GitHub Actions pipeline
- [x] Enable all markdown extensions
- [ ] Add custom domain
- [ ] Enable social preview cards (Insiders)
- [ ] Add math equations page

```markdown
- [x] Completed task
- [ ] Pending task
```

---

## Keyboard Keys

| Shortcut | Key Syntax |
|---|---|
| Copy | ++ctrl+c++ | `++ctrl+c++` |
| Save | ++ctrl+s++ | `++ctrl+s++` |
| Search | ++slash++ | `++slash++` |
| Command palette | ++cmd+shift+p++ | `++cmd+shift+p++` |
| Escape | ++escape++ | `++escape++` |
| Enter | ++enter++ | `++enter++` |

---

## Definition Lists

MkDocs
:   A static site generator designed for project documentation, configured via a single YAML file.

Material for MkDocs
:   The most popular MkDocs theme — provides Google Material Design UI with dark mode, search, and 50+ features.

Docs as Code
:   Writing and managing documentation with the same tools used for source code: Git, PRs, CI/CD.

---

## Footnotes

Static sites[^1] are faster, cheaper, and more secure[^2] than server-rendered docs.

[^1]: No server-side processing means no attack surface beyond the CDN.
[^2]: Benchmark data from [web.dev](https://web.dev) shows sub-100ms TTFB for CDN-hosted static sites.

---

## Text Formatting

| Effect | Syntax | Result |
|---|---|---|
| Bold | `**text**` | **text** |
| Italic | `*text*` | *text* |
| Strikethrough | `~~text~~` | ~~text~~ |
| Highlight | `==text==` | ==text== |
| Superscript | `E=mc^2^` | E=mc^2^ |
| Subscript | `H~2~O` | H~2~O |
| Underline | `^^text^^` | ^^text^^ |
| Bold + italic | `***text***` | ***text*** |

---

## Critic Markup (Track Changes)

Useful for doc reviews and changelogs:

- {==This was added in v2.0==}.
- {--This line was removed--}.
- {++This replacement text was added++}.
- {>>Reviewer comment: needs a code example<<}

```markdown
{==highlight==}  {--delete--}  {++add++}  {>>comment<<}
```

---

## Smart Symbols

| Input | Output |
|---|---|
| `(c)` | (c) |
| `(tm)` | (tm) |
| `(r)` | (r) |
| `--` | -- |
| `---` | --- |
| `...` | ... |
| `1/2` | 1/2 |
| `1/4` | 1/4 |
| `3/4` | 3/4 |

---

## Abbreviations (Global Tooltips)

Hover over these terms to see tooltips — defined once in `includes/abbreviations.md`, applied to every page automatically:

CI/CD pipelines use IaC tools like Terraform to deploy k8s workloads. The SLO is measured via the API and reported by the SRE team.

---

## Tables with Alignment

| Left-aligned | Centred | Right-aligned |
|:-------------|:-------:|--------------:|
| Item 1       | Medium  |         $1.00 |
| Item 2       | High    |        $42.50 |
| `code`       | **bold**|      *italic* |

```markdown
| Left   | Centre |  Right |
|:-------|:------:|-------:|
| text   | text   |   text |
```

---

## Brand Colour Reference

<div class="grid" markdown>

<span class="swatch" style="background:#FD5108"></span> **Orange 500** `#FD5108` — Primary

<span class="swatch" style="background:#FE7C39"></span> **Orange 400** `#FE7C39` — Hover state

<span class="swatch" style="background:#FFAA72"></span> **Orange 300** `#FFAA72` — Data viz

<span class="swatch" style="background:#FFCDA8"></span> **Orange 200** `#FFCDA8` — Backgrounds

<span class="swatch" style="background:#FFE8D4"></span> **Orange 100** `#FFE8D4` — Tints

<span class="swatch" style="background:#FFF5ED; border:1px solid #DFE3E6"></span> **Orange 50** `#FFF5ED` — Subtle bg

<span class="swatch" style="background:#A1A8B3"></span> **Grey 500** `#A1A8B3` — Text/icons

<span class="swatch" style="background:#DFE3E6"></span> **Grey 200** `#DFE3E6` — Borders

<span class="swatch" style="background:#F5F7F8; border:1px solid #DFE3E6"></span> **Grey 50** `#F5F7F8` — Page bg

<span class="swatch" style="background:#000000"></span> **Black** `#000000` — Body text

</div>
