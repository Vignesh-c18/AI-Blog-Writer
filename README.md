# AI Blog Writer

A **Multi-Agent AI Blog Generation Platform** built using **Python, LangGraph, Groq Llama 3.3, FastAPI, and Tavily Search API**.

The application autonomously researches, generates, validates, and stores high-quality technical blog articles using a collaborative AI agent workflow.

---

# ✨ Features

- Multi-Agent workflow using LangGraph
- Autonomous technical tutorial generation
- AI News article generation
- Groq Llama 3.3 integration
- Tavily Search API integration
- AI-powered content validation
- Automatic Markdown generation
- Local JSON & Markdown storage
- FastAPI-ready backend
- Modular project architecture

---

# Architecture

```text
                     User
                       │
           ┌───────────┴───────────┐
           │                       │
     Tutorial Agent          News Agent
           │                       │
           └───────────┬───────────┘
                       │
               Validator Agent
                       │
                Local File Storage
                       │
                      END
```

---

# ⚙️ Workflow

### Tutorial Agent

- Automatically selects or accepts a tutorial topic
- Generates detailed technical articles
- Produces Markdown content

### News Agent

- Collects AI news using Tavily Search
- Generates AI news summaries
- Produces Markdown content

### Validator Agent

- Reviews article quality
- Performs AI-based validation
- Generates metadata
- Saves approved articles

---

# 🛠 Tech Stack

## Backend

- Python
- FastAPI
- LangGraph
- Pydantic

## AI

- Groq (Llama 3.3)
- Google Gemini (optional)
- Prompt Engineering

## Search

- Tavily Search API

## Frontend

- HTML
- CSS
- JavaScript

## Storage

- Local Markdown Files
- Local JSON Metadata

---

# Project Structure

```text
blogboard/
│
├── agents/
│   ├── tutorial_agent/
│   ├── news_agent/
│   └── validator_agent/
│
├── config/
├── graph/
├── services/
├── tools/
├── web/
├── output/
└── run.py
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/Vignesh-c18/AI-Blog-Writer.git
cd AI-Blog-Writer
```

## Create Virtual Environment

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install .
```

## Configure Environment Variables

Create a `.env` file.

Example:

```env
LLM__API_KEY=YOUR_GROQ_API_KEY

CONTENT__TAVILY_API_KEY=YOUR_TAVILY_API_KEY

R2__ACCOUNT_ID=
R2__ACCESS_KEY_ID=
R2__SECRET_ACCESS_KEY=
R2__BUCKET_NAME=
```

---

# Run

```bash
python blogboard/run.py
```

---

# Output

Generated files are stored inside:

```text
output/
└── blogs/
    └── ml/
        ├── article-name.md
        └── articles.json
```

---

# 🎯 Highlights

- Multi-Agent AI Architecture
- LangGraph State Machine
- Autonomous Topic Selection
- AI-powered Validation
- Groq Llama 3.3 Integration
- Tavily Search Integration
- Automatic Markdown Generation
- Local Storage System
- Modular Python Design

---

# Future Improvements

- Planning Agent
- Research Agent
- SEO Optimization
- PDF Export
- Multi-LLM Routing
- User Authentication
- Admin Dashboard
- Docker Deployment

---

# 📸 Screenshots

> Add screenshots here.

Example:

- Home Page
  <img width="1877" height="892" alt="Homepage" src="https://github.com/user-attachments/assets/124071bc-6743-4d09-8373-61c0539661b1" />

- Generated Blog
  <img width="1890" height="865" alt="Article" src="https://github.com/user-attachments/assets/26d85195-6035-46ef-b903-04ea8cb3b832" />

- Terminal Execution
  <img width="773" height="546" alt="Terminal" src="https://github.com/user-attachments/assets/641257f7-0ef1-41ce-9dd8-e23990d3e248" />

- LangGraph Workflow

---

# Author

**N. Vignesh**

GitHub:
https://github.com/Vignesh-c18

---

# 📄 License

This project is licensed under the **MIT License**.
