import streamlit as st
import requests
import os

UPLOAD_FOLDER = "code"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

st.set_page_config(page_title="Code RAG Assistant", layout="wide")
st.title("💻 Codebase Assistant (RAG)")

# Upload section
st.subheader("📂 Upload your Python code files")
uploaded_files = st.file_uploader("Upload .py files", type=["py"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_path = os.path.join(UPLOAD_FOLDER, file.name)
        with open(file_path, "wb") as f:
            f.write(file.read())
    st.success("✅ Files uploaded! Now run `python embed_code.py`")

# Ask question
st.subheader("🤖 Ask about your code")
query = st.text_input("Enter your question")

if st.button("Ask"):
    if query.strip():
        try:
            response = requests.get("http://127.0.0.1:8000/ask", params={"query": query})
            if response.status_code == 200:
                st.write(response.json()["answer"])
            else:
                st.error(f"Backend Error: {response.status_code}")
        except Exception as e:
            st.error(f"❌ Error: {e}")
    else:
        st.warning("Type a question first!")
