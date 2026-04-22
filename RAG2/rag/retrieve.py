from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from utils.config import DB_PATH, TOP_K


# 🔹 Load vector database
def load_db():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return Chroma(
        persist_directory=DB_PATH,
        embedding_function=embeddings
    )


# 🔹 Retrieve relevant documents
def get_relevant_docs(query, db):
    retriever = db.as_retriever(search_kwargs={"k": TOP_K})
    docs = retriever.invoke(query)
    return docs
