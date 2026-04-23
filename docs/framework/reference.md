---
tags:
  - Framework
  - Components
  - Reference
---

# Component Reference

Every MkDocs Material component available in this framework, with copy-paste syntax. This page is itself a live demo — every block below is rendered exactly as it appears in your docs.

---

## Admonitions

Callout boxes for notes, warnings, tips, and more.

### Basic (always expanded)

!!! note "This is a note"
    Use `note` for general information that supplements the main content.

!!! tip "Pro tip"
    Use `tip` for best practices and recommendations.

!!! warning "Watch out"
    Use `warning` for potential pitfalls or important caveats.

!!! danger "Critical"
    Use `danger` for irreversible or destructive actions.

!!! success "All good"
    Use `success` to confirm a positive outcome.

!!! info "FYI"
    Use `info` for contextual background information.

!!! example "Example"
    Use `example` to show a worked example.

!!! quote "Quote"
    Use `quote` for a pull quote or citation.

!!! bug "Known issue"
    Use `bug` to flag a known limitation.

!!! failure "This failed"
    Use `failure` to document a failed approach.

!!! abstract "Summary"
    Use `abstract` for a TL;DR summary block.

!!! question "Is this right?"
    Use `question` for FAQ-style entries.

**Syntax:**
```markdown
!!! tip "Optional custom title"
    Content goes here. Indented with 4 spaces.
```

### Collapsible (closed by default)

??? note "Click to expand"
    This admonition starts collapsed. Use `???` instead of `!!!`.

???+ tip "Expanded by default"
    Use `???+` to start open but still be collapsible.

**Syntax:**
```markdown
??? note "Collapsed by default"
    Content here.

???+ warning "Open by default"
    Content here.
```

---

## Code Blocks

### Basic

```python title="hello.py"
def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("MkDocs"))
```

### Line Numbers

```yaml linenums="1" title="mkdocs.yml"
site_name: My Docs
theme:
  name: material
  palette:
    - scheme: default
      primary: custom
```

### Line Highlighting

```python linenums="1" hl_lines="2 3" title="highlight.py"
def deploy():
    build()      # highlighted
    push()       # highlighted
    notify()
```

### Code Annotations

```yaml title="mkdocs.yml"
plugins:
  - search:
      separator: '[\s\-]+'  # (1)
  - tags  # (2)
```

1. Custom separator for better CJK and camelCase search splitting.
2. Tags plugin — no extra config needed for basic use.

**Syntax:**
```markdown
    ```python
    x = 1  # (1)
    ```

    1. Annotation text appears on click.
```

### Inline Highlighting

Use `#!python print("hello")` for inline highlighted code.

**Syntax:** `` `#!python print("hello")` ``

### Diff View

```diff
- old line that was removed
+ new line that was added
  unchanged line
```

---

## Content Tabs

=== "Python"
    ```python
    pip install mkdocs-material
    ```

=== "conda"
    ```bash
    conda install -c conda-forge mkdocs-material
    ```

=== "Docker"
    ```bash
    docker run --rm -it -v ${PWD}:/docs squidfunk/mkdocs-material
    ```

**Syntax:**
```markdown
=== "Tab One"
    Content for tab one.

=== "Tab Two"
    Content for tab two.
```

!!! tip "Linked tabs"
    Tabs with the same label sync across the whole page (requires `content.tabs.link` in `mkdocs.yml`).

---

## Grid Cards

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } **Fast setup**

    ---
    Clone, install, serve — up in under 2 minutes.

    [:octicons-arrow-right-24: Get started](index.md)

-   :material-palette:{ .lg .middle } **Fully branded**

    ---
    CSS variables map your colours to every Material component.

    [:octicons-arrow-right-24: Brand colours](../showcase/ui-components.md)

-   :material-cloud:{ .lg .middle } **Multi-cloud deploy**

    ---
    GitHub, AWS, Azure, GCP — all pipelines included.

    [:octicons-arrow-right-24: Deployment](../deployment/index.md)

-   :material-feature-search:{ .lg .middle } **Every feature**

    ---
    Admonitions, diagrams, tabs, annotations, tooltips — pre-configured.

    [:octicons-arrow-right-24: Showcase](../showcase/index.md)

</div>

**Syntax:**
```html
<div class="grid cards" markdown>

-   :material-icon:{ .lg .middle } **Card Title**

    ---
    Card description text.

    [:octicons-arrow-right-24: Link text](url)

</div>
```

---

## Buttons

[Primary button](index.md){ .md-button .md-button--primary }
[Secondary button](index.md){ .md-button }

**Syntax:**
```markdown
[Primary](url){ .md-button .md-button--primary }
[Secondary](url){ .md-button }
```

---

## Icons & Emoji

:material-rocket-launch: Material icon — `:material-rocket-launch:`  
:fontawesome-brands-github: FontAwesome — `:fontawesome-brands-github:`  
:octicons-heart-fill-24: Octicons — `:octicons-heart-fill-24:`  
:simple-docker: Simple Icons — `:simple-docker:`  
:wave: Emoji — `:wave:`

Search all icons at [squidfunk.github.io/mkdocs-material/reference/icons-emojis](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/).

---

## Keyboard Keys

Press ++ctrl+c++ to copy. Press ++cmd+shift+p++ to open the command palette.

**Syntax:** `++ctrl+c++`

---

## Task Lists

- [x] Configure `mkdocs.yml`
- [x] Add brand CSS
- [x] Set up GitHub Actions
- [ ] Write content pages
- [ ] Add custom domain

**Syntax:**
```markdown
- [x] Done item
- [ ] Pending item
```

---

## Definition Lists

MkDocs
:   A static site generator geared towards project documentation.

Material for MkDocs
:   The most popular MkDocs theme, providing a Google Material Design UI.

Docs as Code
:   A methodology for writing and managing documentation using the same tools as source code.

**Syntax:**
```markdown
Term
:   Definition text.
```

---

## Footnotes

MkDocs[^1] is built on Python-Markdown[^2] and Jinja2.

[^1]: [mkdocs.org](https://www.mkdocs.org/)
[^2]: [python-markdown.github.io](https://python-markdown.github.io/)

**Syntax:**
```markdown
Text with footnote[^1].

[^1]: Footnote content.
```

---

## Abbreviations & Tooltips

Hover over these terms: CI/CD · IaC · SLO · API · k8s

These tooltips come from `includes/abbreviations.md` and are appended to **every** page automatically via `mkdocs.yml`:

```yaml title="mkdocs.yml"
markdown_extensions:
  - pymdownx.snippets:
      auto_append:
        - includes/abbreviations.md
```

---

## Text Formatting

| Effect | Syntax | Result |
|---|---|---|
| Bold | `**text**` | **bold** |
| Italic | `*text*` | *italic* |
| Strikethrough | `~~text~~` | ~~strikethrough~~ |
| Highlight | `==text==` | ==highlighted== |
| Superscript | `H^2^O` | H^2^O |
| Subscript | `CO~2~` | CO~2~ |
| Underline | `^^text^^` | ^^underlined^^ |
| Keyboard | `++ctrl+s++` | ++ctrl+s++ |

---

## Critic Markup

{==This text was highlighted==}.  
{--This text was deleted--}.  
{++This text was added++}.  
{>>This is a comment<<}

**Syntax:**
```markdown
{==highlight==}  {--delete--}  {++add++}  {>>comment<<}
```

---

## Smart Symbols

(c) (tm) (r) -- --- ... 1/2 1/4 3/4

These are auto-converted by `pymdownx.smartsymbols`.

---

## Tables

| Column A | Column B | Column C |
|:---------|:--------:|---------:|
| Left     | Centre   | Right    |
| `code`   | **bold** | *italic* |

**Syntax:**
```markdown
| Col A | Col B |
|:------|------:|
| left  | right |
```

---

## Front Matter Reference

```yaml
---
title: Custom Page Title          # Overrides H1 in browser tab
description: SEO meta description
tags:
  - Tag1
  - Tag2
hide:
  - navigation                    # Hide left nav on this page
  - toc                           # Hide right TOC on this page
  - footer                        # Hide prev/next footer
search:
  exclude: true                   # Exclude from search index
---
```
