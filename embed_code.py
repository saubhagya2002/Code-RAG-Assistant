import chromadb, os

chroma = chromadb.PersistentClient(path="./code_db")

try:
    collection = chroma.get_collection("codebase")
except:
    collection = chroma.create_collection("codebase")

# Folder that contains your project code
code_folder = "./my_code"

for root, dirs, files in os.walk(code_folder):
    for file in files:
        if file.endswith(".py"):
            file_path = os.path.join(root, file)

            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            collection.add(
                documents=[content],
                metadatas=[{"file": file_path}],
                ids=[file_path]
            )

print("✅ Code successfully embedded in ChromaDB")
