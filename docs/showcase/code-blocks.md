---
tags:
  - Showcase
  - Code
---

# Code Blocks

Every code block feature available in this framework, demonstrated live.

---

## Basic — Language Highlighting

```python
def fibonacci(n: int) -> list[int]:
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]
```

```yaml
site_name: My Docs
theme:
  name: material
  palette:
    primary: custom
```

```bash
mkdocs serve --dev-addr 0.0.0.0:8000
```

---

## With Title

```python title="fibonacci.py"
def fibonacci(n: int) -> list[int]:
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]
```

**Syntax:** ` ```python title="filename.py" `

---

## Line Numbers

```python linenums="1" title="app.py"
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}
```

**Syntax:** ` ```python linenums="1" `

---

## Line Highlighting

```python linenums="1" hl_lines="3 4 5" title="highlighted.py"
class Pipeline:
    def run(self):
        self.build()   # highlighted
        self.test()    # highlighted
        self.deploy()  # highlighted
        self.notify()
```

**Syntax:** ` ```python hl_lines="3 4 5" `

Range syntax is also supported: `hl_lines="3-5"` highlights lines 3 through 5.

---

## Code Annotations

```yaml title="mkdocs.yml"
theme:
  features:
    - content.code.annotate  # (1)
    - content.code.copy      # (2)
    - navigation.instant     # (3)
```

1. Enables `(N)` annotations — click the number to read the note.
2. Adds a copy button to the top-right of every code block.
3. SPA-style page loads — no full reload on navigation.

**Syntax:**
````markdown
```yaml
key: value  # (1)
```

1. The annotation text. Supports **Markdown**.
````

---

## Annotations with Icons

```python title="deploy.py"
import boto3  # (1)!

def deploy(bucket: str, source_dir: str) -> None:
    s3 = boto3.client("s3")  # (2)
    for path in source_dir.iterdir():
        s3.upload_file(str(path), bucket, path.name)
```

1. :simple-amazonaws: The AWS SDK for Python.
2. Creates an S3 client using credentials from the environment or IAM role.

The `!` after `(N)` strips the comment from the rendered code.

---

## Inline Highlighting

Use `#!python range(10)` for inline syntax highlighting.  
Use `#!yaml theme: material` for YAML.  
Use `#!bash mkdocs serve` for bash.

**Syntax:** `` `#!python range(10)` ``

---

## Diff View

```diff
 site_name: My Docs
-theme:
-  name: readthedocs
+theme:
+  name: material
+  palette:
+    primary: custom
 plugins:
   - search
```

**Syntax:** ` ```diff ` with `+` and `-` prefix per line.

---

## Multi-language Tabs with Code

=== "Python"
    ```python title="build.py"
    import subprocess
    subprocess.run(["mkdocs", "build"], check=True)
    ```

=== "Shell"
    ```bash title="build.sh"
    #!/usr/bin/env bash
    set -euo pipefail
    mkdocs build
    ```

=== "Makefile"
    ```makefile title="Makefile"
    .PHONY: build serve deploy

    build:
        mkdocs build

    serve:
        mkdocs serve

    deploy:
        mkdocs gh-deploy --force
    ```

---

## Supported Languages (Sample)

| Language | Identifier |
|---|---|
| Python | `python` |
| JavaScript | `javascript` / `js` |
| TypeScript | `typescript` / `ts` |
| Bash | `bash` / `shell` |
| YAML | `yaml` |
| JSON | `json` |
| Terraform | `hcl` / `terraform` |
| Dockerfile | `dockerfile` |
| SQL | `sql` |
| Markdown | `markdown` / `md` |
| Go | `go` |
| Rust | `rust` |
| Java | `java` |
| C# | `csharp` |
| Diff | `diff` |

Full list: [pygments.org/docs/lexers](https://pygments.org/docs/lexers/)
