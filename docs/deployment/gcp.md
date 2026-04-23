---
tags:
  - Deployment
  - GCP
  - Cloud
---

# GCP — Cloud Storage

Deploy MkDocs to **Google Cloud Storage** with global CDN, or use **Firebase Hosting** for a simpler managed experience.

---

## Architecture Options

=== "Cloud Storage + CDN"
    ```mermaid
    graph LR
        GH["GitHub\ngit push"] --> GA["GitHub Actions"]
        GA --> BUILD["mkdocs build\n→ site/"]
        BUILD --> GCS["Cloud Storage\nBucket"]
        GCS --> CDN["Cloud CDN\n(global)"]
        CDN --> USER["fa:fa-user User"]

        style GCS fill:#4285F4,stroke:#4285F4,color:#fff
        style CDN fill:#34A853,stroke:#34A853,color:#fff
    ```

=== "Firebase Hosting"
    ```mermaid
    graph LR
        GH["GitHub\ngit push"] --> GA["GitHub Actions"]
        GA --> BUILD["mkdocs build\n→ site/"]
        BUILD --> FB["Firebase Hosting\n(managed CDN)"]
        FB --> USER["fa:fa-user User"]

        style FB fill:#FFCA28,stroke:#FFCA28,color:#000
    ```

---

## Option A — Cloud Storage + Cloud CDN

### Prerequisites

- GCP project with billing enabled
- `gsutil` or `gcloud` CLI authenticated
- Workload Identity Federation configured (recommended) or service account JSON key

### Create the Bucket

```bash
# Create a public bucket
gcloud storage buckets create gs://YOUR-BUCKET-NAME \
  --project=YOUR-PROJECT-ID \
  --location=US \
  --uniform-bucket-level-access

# Set main page and 404
gcloud storage buckets update gs://YOUR-BUCKET-NAME \
  --web-main-page-suffix=index.html \
  --web-error-page=404.html

# Make bucket publicly readable
gcloud storage buckets add-iam-policy-binding gs://YOUR-BUCKET-NAME \
  --member=allUsers \
  --role=roles/storage.objectViewer
```

### GitHub Actions Workflow

```yaml title=".github/workflows/deploy-gcp.yml"
name: Deploy to GCP Cloud Storage

on:
  push:
    branches: [main]

permissions:
  contents: read
  id-token: write     # Required for Workload Identity Federation

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - uses: actions/setup-python@v5
        with:
          python-version: '3.x'

      - name: Build MkDocs
        run: |
          pip install -r requirements.txt
          mkdocs build

      - name: Authenticate to GCP (OIDC)
        uses: google-github-actions/auth@v2
        with:
          workload_identity_provider: ${{ secrets.GCP_WORKLOAD_IDENTITY_PROVIDER }}
          service_account: ${{ secrets.GCP_SERVICE_ACCOUNT }}

      - name: Upload to Cloud Storage
        uses: google-github-actions/upload-cloud-storage@v2
        with:
          path: site
          destination: ${{ secrets.GCP_BUCKET_NAME }}
          parent: false       # Upload contents of site/, not site/ itself
          predefinedAcl: publicRead

      - name: Invalidate CDN cache
        run: |
          gcloud compute url-maps invalidate-cdn-cache YOUR-URL-MAP \
            --path "/*" \
            --async
```

### Required Secrets (Cloud Storage)

| Secret | Description |
|---|---|
| `GCP_WORKLOAD_IDENTITY_PROVIDER` | Full WIF provider resource name |
| `GCP_SERVICE_ACCOUNT` | Service account email |
| `GCP_BUCKET_NAME` | Bucket name (without `gs://`) |

### Service Account Roles

```bash
gcloud projects add-iam-policy-binding YOUR-PROJECT-ID \
  --member="serviceAccount:YOUR-SA@YOUR-PROJECT.iam.gserviceaccount.com" \
  --role="roles/storage.objectAdmin"
```

---

## Option B — Firebase Hosting

Firebase Hosting is simpler than raw Cloud Storage — it provides managed SSL, global CDN, and preview channels with no extra setup.

### Setup

```bash
# Install Firebase CLI
npm install -g firebase-tools

firebase login
firebase init hosting

# firebase.json will be created — configure it:
```

```json title="firebase.json"
{
  "hosting": {
    "public": "site",
    "ignore": ["firebase.json", "**/.*", "**/node_modules/**"],
    "rewrites": [
      {
        "source": "**",
        "destination": "/index.html"
      }
    ],
    "headers": [
      {
        "source": "**/*.@(css|js)",
        "headers": [{"key": "Cache-Control", "value": "max-age=31536000"}]
      }
    ]
  }
}
```

### GitHub Actions Workflow (Firebase)

```yaml title=".github/workflows/deploy-firebase.yml"
name: Deploy to Firebase Hosting

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - uses: actions/setup-python@v5
        with:
          python-version: '3.x'

      - name: Build MkDocs
        run: |
          pip install -r requirements.txt
          mkdocs build

      - uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Deploy to Firebase
        uses: FirebaseExtended/action-hosting-deploy@v0
        with:
          repoToken: ${{ secrets.GITHUB_TOKEN }}
          firebaseServiceAccount: ${{ secrets.FIREBASE_SERVICE_ACCOUNT }}
          channelId: live
          projectId: YOUR-FIREBASE-PROJECT-ID
```

### Required Secrets (Firebase)

| Secret | How to get it |
|---|---|
| `FIREBASE_SERVICE_ACCOUNT` | `firebase init` creates this, or download from Firebase Console |

---

## Manual Deploy

```bash
# Cloud Storage
pip install -r requirements.txt
mkdocs build
gcloud storage cp -r site/* gs://YOUR-BUCKET-NAME/

# Firebase
pip install -r requirements.txt
mkdocs build
firebase deploy --only hosting
```

---

## Cost Estimate

| Service | Cost |
|---|---|
| Cloud Storage (1 GB + 10 GB transfer) | ~$0.12/month |
| Cloud CDN (10 GB transfer) | ~$0.08/month |
| Firebase Hosting (free tier: 10 GB/month) | **$0** |
| **Firebase total (small site)** | **$0** |
