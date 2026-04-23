---
tags:
  - Showcase
  - Admonitions
---

# Admonitions

Admonitions are styled callout blocks for drawing attention to important information. This page is a live demo of every available type.

---

## All Twelve Types

!!! note "Note"
    General information that supplements the main content. Use for context, background, or related details.

!!! abstract "Abstract / Summary"
    A TL;DR summary block. Use at the top of long pages to give readers a quick overview.

!!! info "Info"
    Factual background information. Use when you want to add context without it being a warning.

!!! tip "Tip"
    A best practice or pro tip. This type uses the **brand orange** in this framework.

!!! success "Success"
    Confirms a positive outcome, completed step, or recommended approach.

!!! question "Question"
    FAQ-style entries. Use when anticipating a common reader question.

!!! warning "Warning"
    A potential pitfall or important caveat. Read before proceeding.

!!! failure "Failure"
    Documents a failed approach or known anti-pattern.

!!! danger "Danger"
    Reserved for irreversible or destructive actions. Use sparingly.

!!! bug "Bug"
    Flags a known issue, limitation, or workaround.

!!! example "Example"
    A worked example. Appears on showcase and tutorial pages.

!!! quote "Quote"
    A pull quote or citation from an external source.

---

## Collapsible Admonitions

Use `???` for collapsed by default, `???+` for expanded by default.

??? note "Collapsed by default — click to expand"
    This content is hidden until the user clicks the block. Great for optional detail that would otherwise clutter the page.

???+ tip "Expanded by default — click to collapse"
    This starts open but can be collapsed. Use for important information that shouldn't be hidden, but readers may want to tuck away.

??? danger "Irreversible action details"
    This section describes a destructive operation. Starting it collapsed signals to readers that they should think carefully before reading and acting.

---

## Admonitions Without Titles

!!! warning ""
    Omit the title string to render an admonition without a title bar.

---

## Admonitions in Tabs

=== "Note"
    !!! note
        This is a note inside a tab.

=== "Warning"
    !!! warning
        This is a warning inside a tab.

=== "Success"
    !!! success
        This is a success block inside a tab.

---

## Nested Admonitions

!!! info "Outer block"
    Some introductory text.

    !!! tip "Inner block"
        Admonitions can be nested inside each other.

---

## Syntax Reference

```markdown
# Always expanded
!!! type "Optional custom title"
    Content indented with 4 spaces.

# Custom title omitted
!!! warning ""
    No title bar.

# Collapsed by default
??? type "Title"
    Hidden content.

# Expanded by default (but collapsible)
???+ type "Title"
    Visible content.
```

**Available types:**

| Type | Aliases |
|---|---|
| `note` | `seealso` |
| `abstract` | `summary`, `tldr` |
| `info` | `todo` |
| `tip` | `hint`, `important` |
| `success` | `check`, `done` |
| `question` | `help`, `faq` |
| `warning` | `caution`, `attention` |
| `failure` | `fail`, `missing` |
| `danger` | `error` |
| `bug` | — |
| `example` | — |
| `quote` | `cite` |
