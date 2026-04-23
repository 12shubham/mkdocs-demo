# Installation

Get up and running with MkDocs and the Material theme in minutes.

## Prerequisites

- Python **3.8+**
- `pip` package manager
- `git`

Check your versions:

```bash
python --version   # Python 3.8+
pip --version
git --version
```

## Install Dependencies

=== "pip (recommended)"
    ```bash
    pip install mkdocs-material
    ```

=== "pip with requirements.txt"
    ```bash
    pip install -r requirements.txt
    ```

=== "conda"
    ```bash
    conda install -c conda-forge mkdocs-material
    ```

## Clone This Repo

```bash
git clone https://github.com/12shubham/mkdocs-demo.git
cd mkdocs-demo
pip install -r requirements.txt
```

## Run Locally

```bash
mkdocs serve
```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.  
The site **hot-reloads** — edit any `.md` file and the browser refreshes instantly.

!!! tip "Live Edit During the Demo"
    Run `mkdocs serve` in one terminal, open the browser, then edit `docs/index.md` — your team will see changes appear instantly without refreshing.

## Deploy to GitHub Pages

```bash
git add .
git commit -m "my change"
git push origin main
```

GitHub Actions will automatically build and deploy to:  
**[https://12shubham.github.io/mkdocs-demo](https://12shubham.github.io/mkdocs-demo)**

**[Next: Configuration →](configuration.md)**
