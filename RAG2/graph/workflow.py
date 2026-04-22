from langgraph.graph import StateGraph
from graph.nodes import State, detect_intent, rag_node, human_node


def route(state: State):
    return state["intent"]


def build_graph():
    graph = StateGraph(State)

    graph.add_node("intent", detect_intent)
    graph.add_node("rag", rag_node)
    graph.add_node("human", human_node)

    graph.set_entry_point("intent")

    graph.add_conditional_edges(
        "intent",
        route,
        {
            "rag": "rag",
            "escalate": "human"
        }
    )

    graph.set_finish_point("rag")
    graph.set_finish_point("human")

    return graph.compile()
