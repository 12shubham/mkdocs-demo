# Configuration

All MkDocs configuration lives in a single `mkdocs.yml` file at the root of your project.

## File Structure

```
mkdocs-demo/
├── mkdocs.yml          ← All configuration here
├── requirements.txt
├── docs/
│   ├── index.md        ← Home page
│   ├── getting-started/
│   │   ├── installation.md
│   │   └── configuration.md
│   ├── api-reference.md
│   └── changelog.md
└── .github/
    └── workflows/
        └── deploy.yml  ← Auto-deploy to GitHub Pages
```

## Key Config Options

### Site Metadata

```yaml
site_name: My Project Docs
site_url: https://username.github.io/repo-name
site_description: A short description of your project
repo_url: https://github.com/username/repo-name
```

### Navigation

Define the left sidebar structure manually:

```yaml
nav:
  - Home: index.md
  - Getting Started:
    - Installation: getting-started/installation.md
    - Configuration: getting-started/configuration.md
  - API Reference: api-reference.md
```

!!! note "Auto-navigation"
    If you omit `nav:`, MkDocs will auto-generate it from your file structure.

### Theme Options

```yaml
theme:
  name: material
  palette:
    - scheme: default       # light mode
      primary: indigo
    - scheme: slate         # dark mode
      primary: indigo
  features:
    - navigation.tabs       # top-level tabs
    - navigation.top        # back-to-top button
    - search.suggest        # search autocomplete
    - content.code.copy     # copy button on code blocks
```

### Plugins

```yaml
plugins:
  - search                  # built-in full-text search
```

### Markdown Extensions

```yaml
markdown_extensions:
  - admonition              # !!! tip, !!! warning blocks
  - pymdownx.superfences    # code blocks inside admonitions
  - pymdownx.tabbed:        # === "Tab" syntax
      alternate_style: true
  - pymdownx.highlight:     # syntax highlighting
      anchor_linenums: true
  - tables                  # GitHub-flavored tables
```
