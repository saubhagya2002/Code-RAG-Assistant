from fastapi import FastAPI, Query
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

# Load vector DB
embeddings = OpenAIEmbeddings()
db = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)

llm = ChatOpenAI(model="gpt-4")
retriever = db.as_retriever()

qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

@app.get("/")
def root():
    return {"message": "LangChain RAG backend running ✅"}

@app.get("/ask")
def ask(query: str = Query(...)):
    result = qa_chain.run(query)
    return {"answer": result}
