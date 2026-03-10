# 🛡️ AI Compliance & Risk Intelligence Platform

An AI-powered platform that analyzes enterprise documents to detect **compliance risks, policy violations, and regulatory issues** using **Retrieval-Augmented Generation (RAG)** and Large Language Models.

The system helps organizations automatically review internal documents, policies, contracts, and reports to identify potential **legal, regulatory, or security risks**.

---

# 🚀 Overview

Modern organizations handle thousands of documents including policies, contracts, compliance reports, and employee guidelines. Manually reviewing them for regulatory issues is time-consuming and error-prone.

This platform uses **AI + RAG pipelines** to:

- Analyze enterprise documents
- Detect compliance risks
- Generate risk scores
- Provide AI explanations
- Enable interactive chat with documents

AI-based compliance tools are increasingly used in **RegTech (Regulatory Technology)** to help companies detect fraud, regulatory violations, and financial risks using machine learning and data analysis. :contentReference[oaicite:0]{index=0}

---

# ✨ Features

### 📄 Document Upload
Upload enterprise documents such as:

- Compliance policies
- Employee data policies
- Legal contracts
- Internal governance documents

---

### 🔎 AI Document Analysis

The system performs:

- Risk detection
- Compliance scoring
- Policy violation identification
- Key insights extraction

Output includes:

- Compliance score
- Risk summary
- Key findings

---

### 💬 AI Chat with Documents

Ask questions directly about uploaded documents:

Examples:

```
Does this document contain employee data privacy risks?
```

```
What compliance issues exist in this policy?
```

The system retrieves relevant document chunks and generates AI answers.

---

### 📊 Compliance Score Dashboard

Each document receives a **compliance score** based on detected risks.

Example:

| Score | Interpretation |
|------|------|
| 90-100 | Low Risk |
| 70-89 | Moderate Risk |
| < 70 | High Risk |

---

### 📑 Automated Risk Reports

Generate structured compliance reports including:

- Risk summary
- Key issues
- AI explanation
- Recommendations

---

# 🧠 System Architecture

```
User
  │
  ▼
React Frontend (Dashboard)
  │
  ▼
FastAPI Backend
  │
  ▼
RAG Pipeline
 ├── Document Loader
 ├── Text Splitter
 ├── Embeddings
 ├── Vector Store
 └── LLM Query Engine
  │
  ▼
AI Analysis + Risk Scoring
```

---

# 🧰 Tech Stack

| Layer | Technology |
|------|------|
| Frontend | React + Vite |
| Backend | FastAPI |
| AI Pipeline | LangChain |
| Embeddings | OpenAI / Local Models |
| Vector Database | Chroma / FAISS |
| Language Model | LLM (RAG-based) |
| Document Processing | Python |

---

# 📂 Project Structure

```
AI-Compliance-Risk-Intelligence-Platform

backend
│
├── app.py
├── rag_pipeline
│   ├── document_loader.py
│   ├── text_splitter.py
│   ├── embeddings.py
│   └── vector_store.py
│
├── routes
│   ├── upload_routes.py
│   ├── analysis_routes.py
│   ├── chat_routes.py
│   └── report_routes.py
│
├── services
│   ├── document_service.py
│   ├── chat_service.py
│   └── report_service.py
│
└── data
    └── documents

frontend
│
├── src
│   ├── pages
│   │   ├── Dashboard.jsx
│   │   ├── Upload.jsx
│   │   ├── Analyze.jsx
│   │   ├── Chat.jsx
│   │   └── Report.jsx
│   │
│   └── api
│       └── axios.js
│
└── vite.config.js
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```
git clone https://github.com/Viraj1525/AI-Compliance-Risk-Intelligence-Platform.git
cd AI-Compliance-Risk-Intelligence-Platform
```

---

## 2️⃣ Backend Setup

```
cd backend

pip install -r requirements.txt

uvicorn app:app --reload
```

Backend runs on:

```
http://localhost:8000
```

---

## 3️⃣ Frontend Setup

```
cd frontend

npm install

npm run dev
```

Frontend runs on:

```
http://localhost:5173
```

---

# 🧪 Example Workflow

1️⃣ Upload a document  
2️⃣ AI processes document with RAG  
3️⃣ System generates compliance score  
4️⃣ View analysis dashboard  
5️⃣ Ask questions using AI chat  
6️⃣ Generate compliance report  

---

# 🔮 Future Improvements

- Multi-document analysis
- Enterprise authentication
- Real-time compliance monitoring
- Regulatory knowledge base
- AI risk classification models
- Audit-ready compliance reports

---

# 🎯 Use Cases

- Enterprise compliance review
- Legal document analysis
- Data privacy policy verification
- Internal governance monitoring
- Risk management automation

---

# 👨‍💻 Author

**Viraj Agrawal**

AI Developer focused on:

- Generative AI
- Retrieval-Augmented Generation (RAG)
- AI-powered enterprise applications

GitHub  
https://github.com/Viraj1525

---

# ⭐ Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

---

# 📜 License

This project is licensed under the **MIT License**.
