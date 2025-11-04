# Code RAG Assistant 🤖

A project that lets you upload source code and chat with your codebase using RAG + LLM.

## 🚀 How to Run

### Backend
cd backend
pip install -r requirements.txt
uvicorn app:app --reload --port 8000

shell
Copy code

### Frontend
cd frontend
pip install -r requirements.txt
streamlit run streamlit_app.py

diff
Copy code

### ✅ Features
- Upload code files
- AI searches & reads code
- Ask questions like:
  - "Where is DB code?"
  - "Explain validate_user function"

### 🧠 Built With
- FASTAPI
- Streamlit
- OpenAI API
- ChromaDB (vector DB)
