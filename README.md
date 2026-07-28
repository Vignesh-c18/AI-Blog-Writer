# AI Blog Writer

A Multi-Agent AI Blog Generation Platform built using Python, LangGraph, Google Gemini/Groq, FastAPI, and Tavily Search API.

## Overview

AI Blog Writer is an AI-powered content generation platform that automates the creation of high-quality technical tutorials and AI news articles.

The application uses a LangGraph-based multi-agent workflow where specialized agents collaborate to generate, validate, and store publish-ready Markdown blog posts.

The system supports both autonomous topic generation and user-provided topics while ensuring high-quality content through an AI validation loop.

---

## Features

- Multi-Agent Workflow using LangGraph
- Tutorial Blog Generation
- AI News Blog Generation
- Google Gemini & Groq LLM Support
- Tavily Search API Integration
- AI-powered Content Validation
- Automatic Markdown Export
- Local JSON Storage
- FastAPI Backend
- Responsive Web Interface
- Modular Agent Architecture

---

## Architecture

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
               Markdown Storage
                      │
                     END
```

---

## Workflow

### Tutorial Agent

- Selects or accepts a tutorial topic
- Generates comprehensive technical tutorial articles
- Supports autonomous topic generation
- Produces Markdown blog content

### News Agent

- Fetches the latest AI news
- Uses Tavily Search API for research
- Generates AI news articles
- Produces Markdown blog content

### Validator Agent

- Reviews generated content
- Checks quality and completeness
- Requests revisions when required
- Approves final content for publishing

### Storage

- Saves Markdown blog files
- Stores article metadata locally
- Maintains blog history

---

## Tech Stack

### Backend

- Python
- FastAPI
- LangGraph

### AI

- Google Gemini
- Groq
- Prompt Engineering

### Search

- Tavily Search API

### Frontend

- HTML
- CSS
- JavaScript

### Storage

- Local JSON Storage
- Markdown Files

---

## Project Structure

```text
blogboard/
│
├── agents/
│   ├── tutorial_agent/
│   ├── news_agent/
│   └── validator_agent/
│
├── graph/
│
├── services/
│
├── web/
│
├── output/
│
└── config/
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/your-username/AI-Blog-Writer.git
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file and add:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
GROQ_API_KEY=YOUR_GROQ_API_KEY
TAVILY_API_KEY=YOUR_TAVILY_API_KEY
```

### Run the application

```bash
python main.py
```

or

```bash
uvicorn app:app --reload
```

(depending on your project entry point)

---

## Output

The generated blogs are stored as:

- Markdown (.md)
- Local JSON metadata

---

## Highlights

- Multi-Agent architecture using LangGraph
- Automated technical tutorial generation
- AI news generation with live web research
- AI-powered validation loop
- Modular and extensible design
- Markdown export
- Local article storage

---

## Future Improvements

- Planning Agent
- Research Agent
- Writer Agent
- Metadata Agent
- Multi-LLM Support
- SEO Optimization
- PDF Export
- Cloud Storage Integration
- User Authentication

---

## Author

N. Vignesh

---

## License

This project is released under the MIT License.
