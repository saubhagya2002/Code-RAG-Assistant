# 💻 Code RAG Assistant

An AI-powered code understanding and debugging assistant built using **Retrieval-Augmented Generation (RAG)** with **LangChain**, **FastAPI**, **Streamlit**, and **ChromaDB**.

---

## 🚀 Overview

Code RAG Assistant allows developers to **query their project’s source code in natural language**.  
It parses and embeds Python/JavaScript files into vector space, enabling the assistant to retrieve the most relevant code snippets and provide context-aware explanations using OpenAI’s language models.

---

## ✨ Features

- 🔍 **Retrieval-Augmented Generation (RAG)** pipeline for accurate, context-based responses  
- ⚙️ **Automated code parsing** for Python and JavaScript files  
- 🧠 **LangChain + OpenAI** for semantic code understanding and explanation  
- 💾 **ChromaDB vector store** for efficient similarity search  
- ⚡ **FastAPI backend** for retrieval and inference  
- 🖥️ **Streamlit UI** for interactive file upload and natural language querying  

---

## 🏗️ Architecture

[User Query]
↓
[Streamlit Frontend]
↓ (sends query)
[FastAPI Backend]
↓
[LangChain RAG Pipeline]
↓
[ChromaDB Vector Store + OpenAI Model]
↓
[Generated Response]

---

## 🧩 Tech Stack

| Component        | Technology |
|------------------|-------------|
| **Frontend**     | Streamlit |
| **Backend**      | FastAPI |
| **RAG Framework**| LangChain |
| **Vector Store** | ChromaDB |
| **LLM**          | OpenAI GPT-4 |
| **Embeddings**   | OpenAI text-embedding-3-small |
| **Language**     | Python |

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/code-rag-assistant.git
cd code-rag-assistant
python -m venv .venv
.\.venv\Scripts\activate    # On Windows
# source .venv/bin/activate  # On Mac/Linux
pip install -r requirements.txt
OPENAI_API_KEY=your_openai_api_key_here
python embed_code.py
uvicorn backend.app:app --reload --port 8000
streamlit run frontend.py
code-rag-assistant/
│
├── backend/
│   ├── app.py              # FastAPI backend
│
├── frontend.py             # Streamlit UI
├── embed_code.py           # Code parser and embedder
├── requirements.txt
├── .env
└── README.md
Question: How is the API key loaded?

Answer:
The API key is loaded using the `dotenv` package in `backend/app.py`.
This ensures secure environment variable management for OpenAI API access.
