from typing import TypedDict
from langchain_groq import ChatGroq

from rag.retrieve import get_relevant_docs, load_db

# 🔹 Load DB once
db = load_db()

# 🔹 Groq LLM (replace OpenAI)
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

# 🔹 Graph State
class State(TypedDict):
    query: str
    intent: str
    context: str
    answer: str


# 🔍 Intent Detection
def detect_intent(state: State):
    query = state["query"].lower()

    if any(word in query for word in ["refund", "complaint", "human", "agent"]):
        return {"intent": "escalate"}
    
    return {"intent": "rag"}


# 📚 RAG Node
def rag_node(state: State):
    docs = get_relevant_docs(state["query"], db)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are a customer support assistant.

Answer ONLY using the context below.

Context:
{context}

Question:
{state['query']}
"""

    response = llm.invoke(prompt)

    return {
        "context": context,
        "answer": response.content
    }


# 👤 Human Escalation Node
def human_node(state: State):
    return {
        "answer": "⚠️ This query requires human assistance. Escalating to support team."
    }
