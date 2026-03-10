# AI Compliance and Risk Intelligence Platform

An AI-assisted platform for analyzing enterprise PDF documents for compliance and security risks.

The app combines:
- A FastAPI backend for document ingestion, retrieval, risk analysis, chat, and report generation
- A React + Vite frontend dashboard for upload, analysis, chat, and reporting
- A local RAG pipeline using sentence-transformer embeddings and FAISS

## Current capabilities

- Upload PDF documents (`/upload-document`)
- Build and persist local vector index (`embeddings/faiss_index.bin` + `embeddings/chunks.pkl`)
- Run compliance/risk analysis (`/analyze-risk`)
- Ask contextual questions over uploaded docs (`/chat`)
- Generate PDF compliance reports (`/generate-report`)
- List and delete indexed documents (`GET/DELETE /documents`)

## Tech stack

- Backend: Python, FastAPI, Uvicorn
- AI/RAG: LangChain utilities, sentence-transformers, FAISS
- LLM provider: Groq (with heuristic fallback when API key/client is unavailable)
- Frontend: React 19, Vite 7, Axios, Tailwind 4

## Project structure

```text
AI-Compliance-Risk-Intelligence-Platform/
|-- backend/
|   |-- app.py
|   |-- routes/
|   |-- services/
|   |-- rag_pipeline/
|   |-- risk_engine/
|   |-- config/
|   `-- data/documents/
|-- frontend/
|   |-- src/
|   `-- package.json
|-- requirements.txt
`-- README.md
```

## Prerequisites

- Python 3.10+
- Node.js 18+
- npm

## Environment setup

1. Create a `.env` file in the repository root:

```env
GROQ_API_KEY=your_groq_api_key
```

2. Install backend dependencies:

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
```

3. Install frontend dependencies:

```bash
cd frontend
npm install
```

## Run locally

Open two terminals from the repo root.

1. Start backend:

```bash
cd backend
..\\.venv\\Scripts\\python -m uvicorn app:app --host 127.0.0.1 --port 8000 --reload
```

2. Start frontend:

```bash
cd frontend
npm run dev -- --host 127.0.0.1 --port 5173
```

3. Open:

- Frontend: `http://127.0.0.1:5173`
- Backend docs: `http://127.0.0.1:8000/docs`
- Health check: `http://127.0.0.1:8000/health`

Note: the frontend uses a Vite proxy (`/api -> http://127.0.0.1:8000`).

## API endpoints

- `GET /` - root status
- `GET /health` - health check
- `POST /upload-document` - upload a PDF and index it
- `POST /analyze-risk` - run risk/compliance analysis
- `POST /chat` - ask questions against indexed document context
- `POST /generate-report` - create report PDF (`reports/compliance_report.pdf`)
- `GET /documents` - list indexed documents
- `DELETE /documents/{document_name}` - remove a document from index and storage

## Example requests

Upload a document:

```bash
curl -X POST "http://127.0.0.1:8000/upload-document" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@backend/data/documents/sample.pdf"
```

Analyze risk:

```bash
curl -X POST "http://127.0.0.1:8000/analyze-risk" \
  -H "Content-Type: application/json" \
  -d '{"query":"Analyze this document for GDPR and security risks"}'
```

Chat with documents:

```bash
curl -X POST "http://127.0.0.1:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"question":"What are the high-risk findings?","history":[]}'
```

Generate report:

```bash
curl -X POST "http://127.0.0.1:8000/generate-report" \
  -H "Content-Type: application/json" \
  -d '{"query":"Create an executive compliance summary"}'
```

## Notes

- Only PDF uploads are supported.
- FAISS index and chunk metadata are persisted under `backend/embeddings/`.
- Generated reports are stored in `backend/reports/` and served through `/reports`.
- The code includes non-essential legacy dependencies in `requirements.txt` that can be trimmed later.

## License

MIT
