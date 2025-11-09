from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.document_loaders import DirectoryLoader, TextLoader
from dotenv import load_dotenv
import os

load_dotenv()

# Load code files
loader = DirectoryLoader("./code_files", glob="**/*.py", loader_cls=TextLoader)
docs = loader.load()

# Create embeddings
embeddings = OpenAIEmbeddings()

# Store in ChromaDB
db = Chroma.from_documents(documents=docs, embedding=embeddings, persist_directory="./chroma_db")
db.persist()

print("✅ Code indexed successfully with LangChain!")
