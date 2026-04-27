"""
Generate a realistic 'before' state: scattered PDFs with version chaos.
Run: python3 generate_pdfs.py
"""
import textwrap
from fpdf import FPDF
import os

# ── helpers ──────────────────────────────────────────────────────────────────

ORANGE = (253, 81, 8)
GREY   = (100, 100, 100)
LIGHT  = (245, 245, 245)

def safe(text: str) -> str:
    """Strip characters outside latin-1 range."""
    return text.encode("latin-1", errors="replace").decode("latin-1")


def make_pdf(path: str, title: str, version: str, author: str,
             date: str, status: str, body_lines: list[str],
             warning: str = None):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_margins(20, 20, 20)

    # Header bar
    pdf.set_fill_color(*ORANGE)
    pdf.rect(0, 0, 210, 18, style="F")
    pdf.set_font("Helvetica", "B", 14)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(10, 4)
    pdf.cell(0, 10, safe("Acme Corp - Internal Documentation"), align="L")

    pdf.ln(20)

    # Title
    pdf.set_font("Helvetica", "B", 20)
    pdf.set_text_color(30, 30, 30)
    pdf.multi_cell(0, 10, safe(title))
    pdf.ln(2)

    # Meta table
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(*GREY)
    meta = [
        ("Version", version),
        ("Author",  author),
        ("Date",    date),
        ("Status",  status),
    ]
    for k, v in meta:
        pdf.set_font("Helvetica", "B", 9)
        pdf.cell(28, 6, safe(f"{k}:"), border=0)
        pdf.set_font("Helvetica", "", 9)
        pdf.cell(0, 6, safe(v), border=0, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)

    # Warning banner
    if warning:
        pdf.set_fill_color(255, 243, 205)
        pdf.set_text_color(133, 77, 14)
        pdf.set_font("Helvetica", "B", 9)
        pdf.multi_cell(0, 7, safe(f"  WARNING: {warning}"), border=1, fill=True)
        pdf.ln(4)

    # Divider
    pdf.set_draw_color(*ORANGE)
    pdf.set_line_width(0.6)
    pdf.line(20, pdf.get_y(), 190, pdf.get_y())
    pdf.ln(5)

    # Body
    pdf.set_text_color(40, 40, 40)
    for line_num, line in enumerate(body_lines):
        try:
            if line.startswith("## "):
                pdf.set_font("Helvetica", "B", 12)
                pdf.set_text_color(*ORANGE)
                pdf.ln(4)
                pdf.multi_cell(0, 8, safe(line[3:]), new_x="LMARGIN", new_y="NEXT")
                pdf.set_text_color(40, 40, 40)
                pdf.ln(1)
            elif line.startswith("### "):
                pdf.set_font("Helvetica", "B", 10)
                pdf.multi_cell(0, 7, safe(line[4:]), new_x="LMARGIN", new_y="NEXT")
            elif line.startswith("- "):
                pdf.set_font("Helvetica", "", 10)
                for i, chunk in enumerate(textwrap.wrap(safe(line[2:]), width=85) or [" "]):
                    if i == 0:
                        pdf.cell(6, 6, "+", new_x="RIGHT", new_y="TOP")
                    else:
                        pdf.cell(6, 6, " ", new_x="RIGHT", new_y="TOP")
                    pdf.multi_cell(0, 6, chunk, new_x="LMARGIN", new_y="NEXT")
            elif line == "":
                pdf.ln(3)
            else:
                pdf.set_font("Helvetica", "", 10)
                for chunk in textwrap.wrap(safe(line), width=88) or [" "]:
                    pdf.multi_cell(0, 6, chunk, new_x="LMARGIN", new_y="NEXT")
        except Exception as e:
            print(f"  WARN line {line_num}: {repr(line[:60])} => {e}")
            pdf.set_x(20)  # reset cursor and continue

    # Footer
    pdf.set_y(-15)
    pdf.set_font("Helvetica", "I", 8)
    pdf.set_text_color(*GREY)
    pdf.cell(0, 5,
             safe(f"CONFIDENTIAL - INTERNAL USE ONLY  |  {title}  |  {version}  |  {date}"),
             align="C")

    pdf.output(path)
    print(f"  created: {path}")


# ── document definitions ──────────────────────────────────────────────────────

docs = [

    # ── Architecture ──────────────────────────────────────────────────────────
    dict(
        path="architecture/System_Architecture_v1.0.pdf",
        title="System Architecture",
        version="v1.0",
        author="James Turner",
        date="2022-06-14",
        status="ARCHIVED",
        warning="This document is OUTDATED. See v3 for current architecture.",
        body_lines=[
            "## Overview",
            "Initial draft of the monolith architecture for the Acme platform.",
            "All services run on a single EC2 instance behind an ALB.",
            "",
            "## Components",
            "- Frontend: React SPA served by Nginx",
            "- Backend: Django monolith",
            "- Database: PostgreSQL on RDS (single-AZ)",
            "- Cache: None (planned for v2)",
            "",
            "## Known Issues",
            "- No disaster recovery plan documented",
            "- Scaling strategy TBD",
            "- Secrets stored in .env files (see TODO list)",
        ],
    ),
    dict(
        path="architecture/System_Architecture_v2_DRAFT.pdf",
        title="System Architecture - Microservices Migration",
        version="v2.0-DRAFT",
        author="James Turner",
        date="2023-02-28",
        status="DRAFT - NOT APPROVED",
        warning="DRAFT - Do not distribute. Pending review from Platform team.",
        body_lines=[
            "## Overview",
            "Proposed migration from monolith to microservices.",
            "This document was shared for initial review. Several sections are incomplete.",
            "",
            "## Proposed Components",
            "- API Gateway: Kong (TBC - might switch to AWS API GW)",
            "- Auth Service: Keycloak",
            "- Product Service: FastAPI",
            "- Order Service: Node.js [DRAFT]",
            "- Database: Per-service databases (PostgreSQL / MongoDB)",
            "",
            "## Open Questions",
            "- Service mesh: Istio vs Linkerd (not decided)",
            "- CI/CD tooling: Jenkins vs GitHub Actions (not decided)",
            "- Observability stack: TBD",
            "",
            "### TODO",
            "- Add network diagram (James to provide by end of sprint)",
            "- Security review required before approval",
        ],
    ),
    dict(
        path="architecture/System_Architecture_v2_FINAL.pdf",
        title="System Architecture - Microservices Migration",
        version="v2.0-FINAL",
        author="James Turner",
        date="2023-04-10",
        status="APPROVED",
        warning="Superseded by v3. Check with Platform team before referencing this.",
        body_lines=[
            "## Overview",
            "Approved microservices architecture after review by Platform and Security teams.",
            "",
            "## Components",
            "- API Gateway: AWS API Gateway",
            "- Auth Service: Keycloak on EKS",
            "- Product Service: FastAPI on EKS",
            "- Order Service: Node.js on EKS",
            "- Databases: PostgreSQL (RDS) per service",
            "- Cache: Redis (ElastiCache)",
            "",
            "## Deployment",
            "Services deployed to EKS via Helm charts. See Deployment_Guide_AWS_v2.pdf.",
            "",
            "## Review Sign-off",
            "- Platform: Sarah Kim (2023-04-09)",
            "- Security: Mike O'Brien (2023-04-10)",
        ],
    ),
    dict(
        path="architecture/System_Architecture_v3_John_edits_PLEASE_USE_THIS.pdf",
        title="System Architecture v3 - Current State",
        version="v3.0",
        author="John Patel (edits by Sarah Kim)",
        date="2024-01-22",
        status="CURRENT - USE THIS VERSION",
        body_lines=[
            "## Overview",
            "Current production architecture as of January 2024.",
            "NOTE: John added comments in red on pages 4-6. Sarah incorporated most of them.",
            "Diagram in section 3 still needs updating after the Redis cluster change in Dec.",
            "",
            "## Components",
            "- API Gateway: AWS API Gateway + Lambda authoriser",
            "- Auth Service: Keycloak on EKS (v21)",
            "- Product Service: FastAPI on EKS (Python 3.11)",
            "- Order Service: Node.js 20 on EKS",
            "- Notification Service: NEW - added Dec 2023 (see Sarah's notes)",
            "- Databases: PostgreSQL 15 (RDS Multi-AZ)",
            "- Cache: Redis 7 (ElastiCache cluster - 3 nodes)",
            "",
            "## Changes from v2",
            "- Added Notification Service (async, SQS-backed)",
            "- Redis upgraded to cluster mode",
            "- Moved secrets to AWS Secrets Manager",
            "",
            "## Diagram",
            "See attached Visio file (Architecture_v3_diagram_FINAL2.vsdx).",
            "WARNING: diagram may be out of date - check with John.",
        ],
    ),

    # ── API Reference ─────────────────────────────────────────────────────────
    dict(
        path="api/API_Reference_2022.pdf",
        title="REST API Reference",
        version="v1 (2022)",
        author="Dev Team",
        date="2022-09-01",
        status="OUTDATED",
        warning="This API version is deprecated. Endpoints may no longer exist.",
        body_lines=[
            "## Base URL",
            "https://api.acme.com/v1",
            "",
            "## Authentication",
            "API Key in header: X-API-Key: <your_key>",
            "",
            "## Endpoints",
            "### GET /products",
            "Returns a list of all products.",
            "",
            "### POST /orders",
            "Creates a new order. Payload schema TBD - ask Dev team.",
            "",
            "### DELETE /orders/{id}",
            "Cancels an order. Note: doesn't work in staging (known bug).",
            "",
            "## Rate Limits",
            "100 req/min per API key. (May have changed - confirm with backend team.)",
        ],
    ),
    dict(
        path="api/API_Reference_2024_v2_UPDATED.pdf",
        title="REST API Reference",
        version="v2 (2024 update)",
        author="Priya Mehta",
        date="2024-03-15",
        status="IN REVIEW",
        warning="Under review by Priya. Some v2 endpoints not yet documented. Ask her directly.",
        body_lines=[
            "## Base URL",
            "https://api.acme.com/v2",
            "",
            "## Authentication",
            "Bearer token (OAuth 2.0 / Keycloak). See Auth Service docs.",
            "",
            "## Endpoints",
            "### GET /products",
            "Returns paginated product list.",
            "Query params: page, size, category",
            "",
            "### POST /orders",
            "Creates an order. Returns order ID and estimated delivery.",
            "",
            "### GET /orders/{id}/status",
            "Polls order status. NEW in v2.",
            "",
            "### POST /notifications/subscribe",
            "Subscribe to webhook events. NEW in v2. (not fully documented yet)",
            "",
            "## Breaking Changes from v1",
            "- Auth changed from API Key to OAuth 2.0",
            "- All timestamps now UTC ISO 8601",
            "- /orders response schema changed (see Priya's Confluence page)",
        ],
    ),
    dict(
        path="api/API_Reference_LATEST_USE_THIS_ONE!!.pdf",
        title="REST API Reference - LATEST",
        version="v2.1",
        author="Priya Mehta + Dev Team",
        date="2024-08-30",
        status="THIS IS THE ONE - probably",
        warning="Priya says this is latest but the /notifications endpoint changed again in Sept. Ask her.",
        body_lines=[
            "## Base URL",
            "https://api.acme.com/v2",
            "",
            "## Endpoints (complete list)",
            "### Products",
            "- GET  /products             - list (paginated)",
            "- GET  /products/{id}        - single product",
            "- POST /products             - create (admin only)",
            "",
            "### Orders",
            "- POST /orders               - create order",
            "- GET  /orders/{id}          - get order",
            "- GET  /orders/{id}/status   - poll status",
            "- DELETE /orders/{id}        - cancel",
            "",
            "### Notifications",
            "- POST /notifications/subscribe    - webhook subscription",
            "- DELETE /notifications/{id}       - unsubscribe",
            "(schema changed Sept 2024 - TBC)",
            "",
            "## Known Gaps",
            "- Error codes not documented",
            "- Rate limits not confirmed post-Redis change",
            "- SDK docs still in Confluence (link broken as of Oct 2024)",
        ],
    ),

    # ── Deployment ────────────────────────────────────────────────────────────
    dict(
        path="deployment/How_to_Deploy_March2024.pdf",
        title="How to Deploy - Step by Step",
        version="unknown",
        author="Carlos R.",
        date="2024-03-01",
        status="INFORMAL",
        warning="Written by Carlos quickly before his holiday. Not reviewed. May be incomplete.",
        body_lines=[
            "## Steps (as I remember them)",
            "1. SSH into the bastion host (ask DevOps for IP, it changes)",
            "2. Run the deploy script: ./scripts/deploy.sh prod",
            "   - If it fails, try running it again (known flakiness)",
            "3. Check CloudWatch logs for errors",
            "4. Ping #dev-alerts Slack channel to confirm",
            "",
            "## Common Issues",
            "- 'Permission denied' - you probably need to re-assume the IAM role",
            "- Script hangs at step 3 - kill and retry, usually fine",
            "- Database migration fails - DO NOT retry, call Carlos",
            "",
            "## Rollback",
            "There is a rollback script somewhere. Ask DevOps.",
        ],
    ),
    dict(
        path="deployment/Deployment_Guide_AWS_v2.pdf",
        title="AWS Deployment Guide",
        version="v2",
        author="DevOps Team",
        date="2023-05-20",
        status="REVIEW NEEDED",
        warning="Written for v2 architecture. May not match current EKS setup. Verify before use.",
        body_lines=[
            "## Prerequisites",
            "- AWS CLI configured with appropriate IAM role",
            "- kubectl configured for the prod EKS cluster",
            "- Helm 3.x installed",
            "- Docker image built and pushed to ECR",
            "",
            "## Deploy Steps",
            "1. Authenticate: aws ecr get-login-password | docker login",
            "2. Update Helm values: edit helm/values-prod.yaml",
            "3. Run: helm upgrade --install acme ./helm/acme -f helm/values-prod.yaml",
            "4. Monitor rollout: kubectl rollout status deployment/acme-api",
            "",
            "## Secrets",
            "Secrets are in AWS Secrets Manager. Retrieve with:",
            "aws secretsmanager get-secret-value --secret-id acme/prod",
            "",
            "## Rollback",
            "helm rollback acme [revision]",
            "Check revision history: helm history acme",
        ],
    ),
    dict(
        path="deployment/deployment_runbook_FINAL_v3_USE_THIS.pdf",
        title="Deployment Runbook - Production",
        version="v3-FINAL",
        author="Sarah Kim",
        date="2024-06-10",
        status="FINAL (allegedly)",
        warning="Sarah marked this FINAL but DevOps made 3 changes in July not reflected here.",
        body_lines=[
            "## Pre-Deployment Checklist",
            "- All PRs merged and CI green",
            "- Staging deployment verified by QA",
            "- Change request raised in ServiceNow (CAB approval for prod)",
            "- On-call engineer notified",
            "- Maintenance window communicated to customers",
            "",
            "## Deployment Process",
            "1. Merge release branch to main",
            "2. GitHub Actions pipeline triggers automatically",
            "3. Monitor pipeline in GitHub Actions UI",
            "4. Verify health checks pass on all services",
            "5. Smoke test: run ./scripts/smoke-test.sh prod",
            "",
            "## Rollback Criteria",
            "Roll back immediately if:",
            "- Error rate > 1% for 5 minutes",
            "- P99 latency > 2s for 5 minutes",
            "- Any data corruption detected",
            "",
            "## Post-Deployment",
            "- Close ServiceNow change request",
            "- Post update in #releases Slack channel",
            "- Update the 'last deployed' cell in the Deployment Tracker spreadsheet",
            "  (link in Confluence - if you can find it)",
        ],
    ),

    # ── Runbooks ──────────────────────────────────────────────────────────────
    dict(
        path="runbooks/incident-response-DRAFT_do_not_use.pdf",
        title="Incident Response Runbook",
        version="DRAFT",
        author="Mike O'Brien",
        date="2023-11-05",
        status="DRAFT - NOT APPROVED",
        warning="DO NOT USE IN PRODUCTION INCIDENTS. This is an unapproved draft.",
        body_lines=[
            "## Severity Levels",
            "- SEV1: Complete outage. Page on-call immediately.",
            "- SEV2: Partial degradation. Notify on-call within 15 min.",
            "- SEV3: Minor issue. Handle during business hours.",
            "",
            "## Response Steps",
            "### SEV1",
            "1. Page on-call via PagerDuty (rotation TBD - not set up yet)",
            "2. Create incident channel in Slack: #inc-YYYYMMDD-brief-description",
            "3. Start an incident doc (template TBD)",
            "4. Identify and mitigate - see service-specific runbooks",
            "   (NOTE: service runbooks don't exist yet)",
            "",
            "## Contacts",
            "- On-call rota: check the spreadsheet (ask Sarah for link)",
            "- Escalation: CTO is David Chen (mobile in password manager)",
        ],
    ),
    dict(
        path="runbooks/Runbook_Database_Failover_v1.pdf",
        title="Database Failover Runbook",
        version="v1",
        author="Carlos R.",
        date="2023-08-14",
        status="UNVERIFIED",
        warning="Never been tested in production. Treat as a guide only.",
        body_lines=[
            "## When to Use",
            "If the primary RDS instance is unreachable or returning errors for > 5 minutes.",
            "",
            "## Steps",
            "1. Confirm primary is down: check RDS console / CloudWatch",
            "2. Trigger manual failover in RDS console (Multi-AZ failover)",
            "   OR run: aws rds failover-db-cluster --db-cluster-identifier acme-prod",
            "3. Monitor DNS propagation (can take 60-120s)",
            "4. Verify application reconnects - check app logs",
            "5. Notify team in #incidents",
            "",
            "## Expected Downtime",
            "60-120 seconds for automatic failover.",
            "",
            "## Post-Failover",
            "- Raise incident report",
            "- Review RDS events for root cause",
            "- Consider promoting read replica if failover doesn't work",
        ],
    ),
    dict(
        path="runbooks/Runbook_Database_Failover_v2_with_Sarahs_comments.pdf",
        title="Database Failover Runbook",
        version="v2 (Sarah comments)",
        author="Carlos R. + Sarah Kim",
        date="2024-01-30",
        status="SUPERSEDES v1 - use this",
        body_lines=[
            "## Changes from v1",
            "Sarah's comments incorporated - added Redis failover section.",
            "",
            "## When to Use",
            "If primary RDS or Redis cluster is unavailable for > 5 minutes.",
            "",
            "## RDS Failover",
            "Same as v1 steps 1-5.",
            "",
            "## Redis Cluster Failover (NEW)",
            "1. Check ElastiCache console for node failures",
            "2. Redis Cluster mode: automatic failover is enabled",
            "3. If full cluster failure: recreate from snapshot",
            "   aws elasticache create-replication-group ...",
            "   (full command TBD - ask Carlos)",
            "",
            "## NOTE",
            "Sarah flagged: the Redis cluster was reconfigured in Dec 2023.",
            "These steps may no longer match. Verify with DevOps before using.",
        ],
    ),

    # ── Misc ──────────────────────────────────────────────────────────────────
    dict(
        path="misc/Meeting_Notes_Arch_Review_Q1_2024.pdf",
        title="Architecture Review - Meeting Notes Q1 2024",
        version="N/A",
        author="James Turner (scribe)",
        date="2024-01-15",
        status="FOR REFERENCE",
        body_lines=[
            "## Attendees",
            "James Turner, Sarah Kim, Priya Mehta, Carlos R., Mike O'Brien, David Chen (CTO)",
            "",
            "## Key Decisions",
            "- Proceed with microservices v3 architecture (David approved)",
            "- Redis to be upgraded to cluster mode by end of January",
            "- API v2 to be released Q2 2024",
            "- Runbooks to be 'written up properly at some point' (action: Mike)",
            "",
            "## Action Items",
            "- James: update Architecture doc to v3 by Jan 31",
            "- Carlos: test DB failover runbook in staging (still outstanding as of March)",
            "- Priya: finish API v2 docs (in progress)",
            "- Mike: create incident response runbook (still DRAFT)",
            "- All: agree on a docs solution - Confluence vs something else",
            "  Decision deferred again. Will revisit in Q2.",
            "",
            "## Quote of the Meeting",
            "'I can never find anything. Where do we even keep our docs?' - David Chen",
        ],
    ),
    dict(
        path="misc/Onboarding_Checklist_TODO_INCOMPLETE.pdf",
        title="New Engineer Onboarding Checklist",
        version="unknown",
        author="HR + DevOps (unclear)",
        date="2023-01-01",
        status="INCOMPLETE - DO NOT SEND TO NEW HIRES",
        warning="Half of the links in this document are broken. Do not use until updated.",
        body_lines=[
            "## Access Requests",
            "- [ ] GitHub org invite (ask James)",
            "- [ ] AWS console access (raise ticket with IT - takes 3-5 days)",
            "- [ ] Jira access (link: [BROKEN])",
            "- [ ] Confluence access (link: [BROKEN])",
            "- [ ] PagerDuty (ask Mike - if he remembers)",
            "",
            "## Tools to Install",
            "- Docker Desktop",
            "- kubectl (version TBD - ask DevOps)",
            "- AWS CLI v2",
            "- See the dev setup doc... somewhere on Confluence",
            "",
            "## Reading List",
            "- System Architecture doc (check which version is current)",
            "- API Reference (check which version is current)",
            "- Deployment Guide (check which version is current)",
            "- Runbooks (most are DRAFT)",
            "",
            "## Who Does What",
            "See the org chart PDF... which may also be out of date.",
        ],
    ),
    dict(
        path="misc/README_IMPORTANT_READ_FIRST.pdf",
        title="IMPORTANT - Read Before Using Any Docs",
        version="N/A",
        author="Sarah Kim",
        date="2024-09-01",
        status="PINNED",
        body_lines=[
            "If you are reading this, you are trying to find documentation.",
            "Please read the following before using anything in this folder.",
            "",
            "## The Problem",
            "Our docs are scattered across:",
            "- This shared drive (you're here now)",
            "- Confluence (space: ACME-INTERNAL - half the pages are stale)",
            "- GitHub repo wikis (3 different repos, none complete)",
            "- Email threads (seriously)",
            "- Slack messages",
            "- People's heads",
            "",
            "## Which Version to Use",
            "When in doubt: ask. The filename often lies.",
            "Files with 'FINAL' in the name are rarely final.",
            "Files with 'USE_THIS_ONE' may not be the one to use.",
            "",
            "## The Plan",
            "We have been 'about to fix this' since Q3 2022.",
            "As of September 2024, a proposal is on the table to move",
            "everything to a docs-as-code solution. Watch this space.",
            "",
            "## In the Meantime",
            "- For architecture: ask James (but he's usually in meetings)",
            "- For API docs: ask Priya",
            "- For deployment: ask Carlos or Sarah",
            "- For runbooks: there are no good runbooks. Sorry.",
        ],
    ),
]

# ── generate all PDFs ─────────────────────────────────────────────────────────
print(f"\nGenerating {len(docs)} PDFs...\n")
for d in docs:
    make_pdf(**d)

print(f"\nDone. {len(docs)} PDFs written to subdirectories of before/\n")
