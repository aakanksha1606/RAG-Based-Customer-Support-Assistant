import os

# 🔑 Add your OpenAI API key
os.environ["GROQ_API_KEY"] = "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"

# 📂 Paths
PDF_PATH = "data/knowledge.pdf"
DB_PATH = "db/chroma_db"

# ⚙️ RAG Settings
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
TOP_K = 3
