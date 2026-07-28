# AI Blog Writer

A Multi-Agent AI Content Generation Platform

AI Blog Writer is a full-stack Multi-Agent AI platform that automates technical blog generation. The system researches topics, plans article structure, generates long-form technical content, validates content quality, generates metadata, and exports blogs in Markdown format through a LangGraph-based workflow.
## Features

- Multi-Agent AI Workflow using LangGraph
- Automated Topic Research using Tavily Search API
- AI-powered Technical Blog Generation
- Article Planning and Structuring
- Content Validation and Quality Review
- Metadata Generation (Title, Description, Slug)
- Markdown Blog Export
- Local JSON Storage
- Responsive Web Interface
- Modular Architecture
- Easy LLM Provider Integration

## Tech Stack

- Python
- LangGraph
- Google Gemini / Groq
- FastAPI
- React.js
- Next.js
- Tailwind CSS
- Tavily Search API
- HTML
- CSS
- JavaScript
- Git
- GitHub

---

## Project Architecture

```
                 User
                  │
                  ▼
          Tutorial Agent
                  │
                  ▼
          Planning Agent
                  │
                  ▼
          Research Agent
                  │
                  ▼
           Writer Agent
                  │
                  ▼
         Validator Agent
                  │
                  ▼
       Metadata Generation
                  │
                  ▼
    Markdown + JSON Storage
                  │
                  ▼
          Web Interface
```

---

## Folder Structure

```
AI-Blog-Writer/

│
├── blogboard/
│   ├── agents/
│   ├── config/
│   ├── graph/
│   ├── services/
│   ├── tools/
│   ├── web/
│   └── run.py
│
├── pyproject.toml
├── package.json
├── README.md
└── .env.example
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/Vignesh-c18/AI-Blog-Writer.git
```

Move into the project

```bash
cd AI-Blog-Writer
```

Create virtual environment

```bash
uv venv
```

Activate environment

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
uv sync
```

---

## Environment Variables

Create a `.env` file and add your API keys.

```env
GROQ_API_KEY=your_key

TAVILY_API_KEY=your_key
```

or

```env
GEMINI_API_KEY=your_key
```

---

## Run the Project

Start the backend

```bash
python blogboard/run.py
```

Run the frontend

```bash
python -m http.server 8000 --directory blogboard/web
```

Open your browser

```
http://localhost:8000
```

---

## AI Workflow

### Tutorial Agent

- Selects the blog domain
- Initializes the workflow

### Planning Agent

- Creates article outline
- Organizes section flow

### Research Agent

- Searches latest technical information
- Collects relevant references

### Writer Agent

- Generates long-form technical articles
- Produces Markdown content

### Validator Agent

- Reviews article quality
- Checks formatting and readability

### Metadata Generator

- Generates title
- Description
- Slug

### Storage

- Saves Markdown files
- Maintains article metadata in JSON

---

## Future Improvements

- Multi-LLM Support
- SEO Optimization Agent
- Image Generation
- PDF Export
- Authentication
- Analytics Dashboard
- Docker Deployment
---

## Author

N. Vignesh

---

## License

This project is released under the MIT License.
