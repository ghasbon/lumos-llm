# Lumos

**Lumos** is a unified HTTP gateway for AI agent infrastructure components.

It exposes a single entry point (one port) for interacting with and monitoring multiple internal AI services, including embeddings, reranking, code completion, and reasoning systems.

---

## 🚀 Purpose

Modern agent systems are composed of multiple specialized components:

- Embedding models
- Rerankers
- Code autocompletion models
- Light reasoning models (fast inference)
- Deep reasoning models (complex inference / multi-step thinking)

Lumos centralizes access to all of them behind a single HTTP interface.

The goal is not just orchestration, but **observability and performance analysis of agent workflows in real time**.

---

## 🧠 Core Idea

Instead of each component running in isolation, Lumos acts as a **traffic-aware execution layer**:

- All requests pass through a single port
- Requests are routed to the appropriate model or service
- Both request and response are captured
- Latency, payload size, and execution traces are measured

This enables:

- Performance benchmarking per component
- Comparative evaluation (e.g., light vs deep reasoning)
- Full visibility into agent pipelines
- Debugging of multi-stage LLM systems

---

## 📡 Target Architecture

Lumos will eventually provide unified access to:

- 🔎 Embeddings service
- 📊 Reranker service
- 💡 Code autocomplete engine
- ⚡ Light reasoning engine
- 🧠 Deep reasoning engine

Each request is:

1. Received via HTTP
2. Routed internally
3. Logged and traced
4. Measured for latency and throughput
5. Returned with optional metadata

---

## 📈 Observability Goals

Lumos is designed with observability as a first-class feature:

- Request/response logging
- Latency tracking per component
- Tool-level performance comparison
- HTTP-level tracing (OpenTelemetry-ready)
- Future integration with Grafana/Loki

---

## 🧱 Current Status

This project is in early development.

Current state:
- FastAPI server initialized
- Basic health endpoint available (`/health`)
- Logging infrastructure in place

Next steps:
- `/run` execution endpoint
- component routing layer
- instrumentation layer (OpenTelemetry)
- internal service abstraction layer

---

## ⚙️ Running Locally

```bash
uv venv
uv add fastapi uvicorn
uv run uvicorn main:app --reload