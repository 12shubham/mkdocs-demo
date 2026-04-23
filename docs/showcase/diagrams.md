---
tags:
  - Showcase
  - Diagrams
  - Mermaid
---

# Diagrams

All Mermaid diagram types rendered live with this framework's brand colours.

---

## Flowchart — Left to Right

```mermaid
graph LR
    A["Start"] --> B{"Decision?"}
    B -->|Yes| C["Action A"]
    B -->|No| D["Action B"]
    C --> E["End"]
    D --> E
```

---

## Flowchart — Top to Bottom

```mermaid
graph TD
    REPO["GitHub Repository"]
    CI["GitHub Actions\nCI Pipeline"]
    BUILD["mkdocs build"]
    TEST["Link Check\n& Lint"]
    DEPLOY["mkdocs gh-deploy"]
    LIVE["🌐 GitHub Pages"]

    REPO -->|"git push"| CI
    CI --> BUILD
    BUILD --> TEST
    TEST -->|Pass| DEPLOY
    TEST -->|Fail| REPO
    DEPLOY --> LIVE
```

---

## Sequence Diagram

```mermaid
sequenceDiagram
    actor Dev as Developer
    participant GH as GitHub
    participant GHA as GitHub Actions
    participant Pages as GitHub Pages

    Dev->>GH: git push main
    GH->>GHA: Trigger workflow
    GHA->>GHA: pip install -r requirements.txt
    GHA->>GHA: mkdocs build
    GHA->>GH: Push to gh-pages branch
    GH->>Pages: Deploy static site
    Pages-->>Dev: ✅ Live in ~60s
```

---

## Class Diagram

```mermaid
classDiagram
    class MkDocsSite {
        +String site_name
        +String site_url
        +Theme theme
        +List~Plugin~ plugins
        +build()
        +serve()
        +deploy()
    }

    class Theme {
        +String name
        +Palette palette
        +List~String~ features
    }

    class Plugin {
        +String name
        +configure()
    }

    class SearchPlugin {
        +String separator
    }

    class TagsPlugin {
        +String tags_file
    }

    MkDocsSite "1" --> "1" Theme
    MkDocsSite "1" --> "N" Plugin
    Plugin <|-- SearchPlugin
    Plugin <|-- TagsPlugin
```

---

## State Diagram

```mermaid
stateDiagram-v2
    [*] --> Draft
    Draft --> Review : Open PR
    Review --> Approved : LGTM
    Review --> Draft : Changes requested
    Approved --> Published : Merged to main
    Published --> Draft : Edit needed
    Published --> [*] : Deprecated
```

---

## ER Diagram

```mermaid
erDiagram
    DOCUMENT {
        string id PK
        string title
        string path
        datetime created_at
        datetime updated_at
        string author_id FK
    }

    AUTHOR {
        string id PK
        string name
        string email
    }

    TAG {
        string id PK
        string name
        string slug
    }

    DOCUMENT_TAG {
        string document_id FK
        string tag_id FK
    }

    AUTHOR ||--o{ DOCUMENT : writes
    DOCUMENT ||--o{ DOCUMENT_TAG : has
    TAG ||--o{ DOCUMENT_TAG : applied_to
```

---

## Gantt Chart

```mermaid
gantt
    title Documentation Sprint — April 2026
    dateFormat  YYYY-MM-DD
    section Framework
        Create mkdocs.yml config  :done,    f1, 2026-04-20, 1d
        Brand CSS & JS            :done,    f2, 2026-04-21, 1d
        Framework docs            :done,    f3, 2026-04-22, 1d
    section Content
        DevOps home page          :done,    c1, 2026-04-22, 1d
        Deployment guides         :done,    c2, 2026-04-23, 1d
        Feature showcase          :active,  c3, 2026-04-23, 1d
    section Deploy
        GitHub Pages live         :done,    d1, 2026-04-23, 1d
        AWS guide                 :         d2, 2026-04-24, 2d
        Azure guide               :         d3, 2026-04-24, 2d
```

---

## Pie Chart

```mermaid
pie title Documentation Coverage by Section
    "Framework Docs"    : 25
    "Deployment Guides" : 30
    "Feature Showcase"  : 30
    "API Reference"     : 15
```

---

## Timeline

```mermaid
timeline
    title MkDocs Material — Major Releases
    2016 : MkDocs Material 0.1
         : Initial release
    2019 : Version 4.0
         : Dark mode
         : Improved search
    2021 : Version 7.0
         : Tabs, navigation overhaul
    2022 : Version 8.0
         : Blog plugin
         : Social cards
    2023 : Version 9.0
         : Tags plugin
         : Instant navigation
    2026 : This Framework
         : Full feature showcase
         : Multi-cloud deploy
```

---

## Quadrant Chart

```mermaid
quadrantChart
    title Documentation Priority Matrix
    x-axis Low Effort --> High Effort
    y-axis Low Impact --> High Impact
    quadrant-1 Do First
    quadrant-2 Plan
    quadrant-3 Skip
    quadrant-4 Delegate
    Home Page: [0.2, 0.9]
    API Reference: [0.7, 0.85]
    Getting Started: [0.3, 0.8]
    Changelog: [0.15, 0.4]
    Runbooks: [0.6, 0.7]
    ADRs: [0.5, 0.5]
    Style Guide: [0.4, 0.3]
    Meeting Notes: [0.2, 0.1]
```

---

## Git Graph

```mermaid
gitGraph
    commit id: "Initial commit"
    commit id: "Add mkdocs.yml"

    branch feature/new-page
    checkout feature/new-page
    commit id: "Add API reference"
    commit id: "Fix broken links"

    checkout main
    merge feature/new-page id: "Merge PR #12"

    branch fix/typo
    checkout fix/typo
    commit id: "Fix typo in readme"

    checkout main
    merge fix/typo id: "Merge PR #13"
    commit id: "Deploy v1.1"
```

---

## Syntax Reference

````markdown
```mermaid
graph LR
    A --> B
```
````

All diagram types: `graph`, `sequenceDiagram`, `classDiagram`, `stateDiagram-v2`, `erDiagram`, `gantt`, `pie`, `timeline`, `quadrantChart`, `gitGraph`, `xychart-beta`, `block-beta`.

Full reference: [mermaid.js.org/syntax](https://mermaid.js.org/syntax/flowchart.html)
