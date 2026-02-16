# COO Workflow Orchestration Agent (CWA)

> **Status**: Pre-Alpha / Scaffolding Phase
> **Version**: 0.1.0

The **COO Workflow Orchestration Agent (CWA)** is a bounded, semi-autonomous "control tower" designed to orchestrate complex operations workflows with deterministic precision. Unlike generic "AI Agents" that rely on probabilistic reasoning for critical actions, CWA operates on strict architectural invariants, ensuring that every action is audited, policy-driven, and subject to human approval when necessary.

It serves as a central nervous system for operations teams, ingesting tasks from disparate sources (Linear, Slack, Email), normalizing them into a unified `WorkItem` schema, and executing policy-based workflows to drive them to completion.

---

## 🎯 Functionality: How It Works

CWA is designed to automate the repetitive, high-stakes coordination work that bogs down COO and Operations teams. It follows a strict "Observe-Orient-Decide-Act" loop:

1.  **Ingest & Normalize**: The agent listens to various inputs (Linear tickets, Slack messages, Emails) and converts them into a standardized `WorkItem`. This creates a single source of truth for all operational tasks.
2.  **Evaluate Policies**: A deterministic policy engine checks every `WorkItem` against defined rules (e.g., "If a P1 ticket hasn't been updated in 4 hours, trigger an escalation").
3.  **Propose Action Drafts**: When a policy is triggered, the agent *proposes* an action (an `ActionDraft`). It does **not** act immediately.
4.  **Enforce Approval Gates**: Depending on the criticality of the action, it may require human approval.
5.  **Execute & Audit**: Once approved (or if auto-approval is safe), the agent executes the side-effect (e.g., sending a Slack ping) and logs an immutable `AuditLog`.

---

## ✨ Key Features

### 🛡️ Deterministic Policy Engine
The core of CWA is **logic, not vibes**. Policies are defined in code/configuration, not natural language prompts.
*   **Precise Triggers**: Rules are evaluated mathematically (e.g., `days_since_update > 3`).
*   **No Hallucinations**: Decisions are made by explicit logic branches, ensuring consistent behavior every time.

### 🔄 Supported Workflows
CWA comes with pre-built state machines for common operations scenarios:
*   **Stall Detection & Nudging**: Automatically identifies work items that haven't moved and drafts polite "nudge" messages to owners.
*   **SLA Monitoring**: Tracks deadlines and proactively escalates "at-risk" items before they breach SLA.
*   **Weekly Reporting**: Aggregates completed work and blockers into a draft status report for leadership review.
*   **Meeting Task Extraction**: Parses meeting notes to extract action items, validates them, and creates proper tickets.

### 🔒 Bounded Autonomy
The agent operates within strict "bounds" defined by state machines.
*   **Explicit States**: A workflow can only move between valid states (e.g., `DRAFTING` -> `AWAITING_APPROVAL` -> `SENT`).
*   **Impossible Transitions**: A "Pending" item cannot jump to "Resolved" without passing through the necessary checks.

### 👤 Human-in-the-Loop by Design
*   **Action Drafts**: The agent proposes actions for you to review. You are the editor; the agent is the drafter.
*   **Granular Permissions**: Configure which actions require explicit approval and which can run autonomously.

---

## 🚀 Benefits

### Why use CWA over a generic AI Agent?

| Feature | Generic "AI Agent" | COO Workflow Agent (CWA) |
| :--- | :--- | :--- |
| **Decision Logic** | Probabilistic (LLM decides) | **Deterministic (Policy Engine)** |
| **Reliability** | Prone to hallucinations | **100% Predictable Behavior** |
| **Security** | Risk of prompt injection | **Bounded State Machines** |
| **Audit Trail** | Opaque "reasoning" | **Immutable Audit Logs** |
| **Role** | "Magic Box" | **Force Multiplier** |

*   **Trust & Safety**: You can trust CWA with sensitive operations because it *cannot* do anything outside its programmed policies.
*   **Scalability**: Handle 100x more volume without adding headcount. The agent handles the tracking, reminding, and reporting, freeing humans to solve the actual problems.
*   **Ops Excellence**: Enforce standard operating procedures (SOPs) automatically. If it's policy, it happens—every time.

---

## 🏗 System Architecture

CWA is built on a **Policy-Driven, Event-Sourced** architecture. It separates the *decision* to act from the *execution* of the action, with a strict audit trail in between.

### Core Components

1.  **Ingestion Layer**:
    *   Connectors for Linear, Slack, and other external systems.
    *   Normalizes incoming data into a canonical `WorkItem`.
    *   **Invariant**: Source of Truth. The Agent never "invents" work; it only reflects the state of external systems.

2.  **Policy Engine** (`app/policies/`):
    *   Deterministic rule evaluation.
    *   Evaluates `WorkItems` against active `Policies` to propose `ActionDrafts`.

3.  **Execution Layer** (`app/workflows/`):
    *   **Action Drafts**: Proposed actions (e.g., "Send Slack Message") that wait for approval.
    *   **Action Execution**: The actual side-effect (API call), performed only after approval logic is satisfied.

4.  **Intelligence Layer** (`app/llm/`):
    *   Uses LLMs (Gemini) for *content generation* (drafting messages, extracting tasks from meeting notes) but **never** for *control flow decisions*.
    *   Result: High-quality text output with zero risk of "rogue" agent behavior.

### Architectural Invariants

The system is rigorously tested against these non-negotiable constraints (see `tests/test_invariants.py`):
*   **Idempotency**: Retrying a workflow step **never** results in duplicate side-effects (e.g., sending the same Slack message twice).
*   **Auditability**: Every `ActionExecution` must have a linked `AuditLog` trace.
*   **Approval Gates**: High-stakes actions (like Escalations) **cannot** execute without an `APPROVED` `ActionDraft`.

---

## 📦 Data Models

Key entities in the system:

*   **`Organization`**: Supports multi-tenancy.
*   **`User`**: System users with granular roles (Admin, Approver, Viewer).
*   **`WorkItem`**: The atomic unit of work. Contains normalized metadata (`status`, `priority`, `due_date`) and raw source data.
*   **`Policy`**: Configuration for automation rules (`trigger_event`, `rules`, `actions`).
*   **`AuditLog`**: Immutable record of system activities.

---

## 🚀 Getting Started

### Prerequisites

*   Python 3.10+
*   PostgreSQL 14+
*   Docker & Docker Compose (optional, for infra)

### Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/your-org/coo-workflow-agent.git
    cd coo-workflow-agent
    ```

2.  **Set up the environment**:
    Create a `.env` file based on the configuration requirements (see `app/config.py`).
    ```bash
    cp .env.example .env
    # Edit .env with your DATABASE_URL, OPENAI_API_KEY, etc.
    ```

3.  **Install dependencies**:
    *Note: `requirements.txt` or `pyproject.toml` is currently pending. Please install standard FastAPI/SQLAlchemy deps manually if needed.*
    ```bash
    pip install fastapi uvicorn sqlalchemy pydantic psycopg2-binary
    ```

4.  **Run Migrations**:
    ```bash
    alembic upgrade head
    ```

### Running the Application

Start the development server:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.
Interactive API docs: `http://127.0.0.1:8000/docs`.

---

## 🧪 Development

### Directory Structure

```text
app/
├── api/            # REST API endpoints (FastAPI routers)
├── models/         # SQLAlchemy ORM models
├── schemas/        # Pydantic data schemas (Request/Response)
├── policies/       # Deterministic policy logic
├── workflows/      # State machines and execution logic
├── connectors/     # Integrations (Linear, Slack)
├── llm/            # LLM interface and prompts
└── main.py         # Application entrypoint

tests/
├── test_invariants.py  # Architectural constraint verification
```

### Running Tests

Run the implementation and invariant tests:

```bash
pytest
```

---

## 🤝 Contributing

1.  Fork the repository.
2.  Create a feature branch.
3.  Ensure `pytest` passes (especially `test_invariants.py`).
4.  Submit a Pull Request.

---

*Generated by Antigravity*
