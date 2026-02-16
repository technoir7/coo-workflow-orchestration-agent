# Tasks

- [x] **Project Initialization**
  - [x] Scaffold file tree structure
  - [x] Define `Organization`, `User`, `IntegrationAccount` models
  - [x] Define `WorkItem` schema and Pydantic validation
  - [x] Create core event taxonomy (`stalled`, `sla_risk`, etc.)

- [x] **Core Logic**
  - [x] Implement Workflow State Machines
  - [x] Build deterministic Policy Engine
  - [x] Create LLM Interface abstraction layer
  - [x] Define internal REST API endpoints

- [ ] **Infrastructure & Deployment**
  - [ ] Set up PostgreSQL and Redis instances (Docker Compose)
  - [ ] Configure Alembic for database migrations
  - [ ] Implement secure environment variable loading (`.env`)

- [ ] **Integration Implementation**
  - [ ] **Linear Connector**: OAuth flow + Webhook ingestion
  - [ ] **Slack Connector**: App installation + Message posting logic

- [ ] **Workflow Orchestration**
  - [ ] Set up Temporal (or internal task queue) worker
  - [ ] Implement `InfoProcessor` for scheduled ingestion
  - [ ] Build `BackgroundWorker` for policy evaluation

- [ ] **Intelligence Layer**
  - [ ] Implement real Gemini LLM service (`app/llm/gemini.py`)
  - [ ] Refine prompts for "Nudge Drafting" and "Meeting Extraction"

- [ ] **Frontend**
  - [ ] Build simple Dashboard for SLA monitoring
  - [ ] Create Approval UI for human-in-the-loop actions

- [ ] **Documentation**
  - [ ] Write `CONTRIBUTING.md`
  - [ ] Document API usage with Swagger/Redoc
