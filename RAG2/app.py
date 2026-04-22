from rag.ingest import create_vector_db
from graph.workflow import build_graph


def main():
    print("🔄 Indexing PDF (first run only)...")
    create_vector_db()
    print("✅ System Ready!\n")

    app = build_graph()

    while True:
        query = input("Ask your question (or type 'exit'): ")

        if query.lower() == "exit":
            break

        result = app.invoke({"query": query})

        print("\n💬 Answer:")
        print(result["answer"])
        print("-" * 50)


if __name__ == "__main__":
    main()
