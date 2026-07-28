# AI Blog Writer

An intelligent Multi-Agent AI Blog Generation platform that automatically researches trending topics, generates high-quality technical articles, validates content quality, and prepares them for publishing.

Built using Python, LangGraph, Groq/Gemini, and modern AI workflows.

---

## Features

- Multi-Agent AI Architecture
- Automated Topic Research
- AI-Powered Technical Blog Generation
- Content Validation
- Markdown Blog Generation
- Web-Based Blog Interface
- Modular Agent Design
- Easy API Integration

---

## Tech Stack

- Python 3.12+
- LangGraph
- Groq API / Google Gemini
- Tavily Search API
- HTML
- CSS
- JavaScript
- Git
- GitHub

---

## Project Architecture

```
             User Input
                  │
                  ▼
          Research Agent
                  │
                  ▼
          Content Writer
                  │
                  ▼
         Content Validator
                  │
                  ▼
         Blog Generation
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

The application follows a Multi-Agent workflow.

### Research Agent

- Searches latest AI topics
- Collects reliable information

### Writer Agent

- Generates technical articles
- Produces structured blog content

### Validator Agent

- Reviews generated content
- Improves readability and quality

---

## Future Improvements

- SEO Optimization Agent
- Image Generation Support
- PDF Export
- Blog Scheduling
- Multi-Language Support
- Admin Dashboard
- Streamlit Interface

---

## Author

Vignesh

---

## License

This project is released under the MIT License.