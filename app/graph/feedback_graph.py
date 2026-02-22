from langgraph.graph import StateGraph, END
from .state import FeedbackState
from app.agents.feedback_agent import run_feedback_agent


def build_feedback_graph():
    g = StateGraph(FeedbackState)
    g.add_node("feedback_agent", run_feedback_agent)
    g.set_entry_point("feedback_agent")
    g.add_edge("feedback_agent", END)
    return g.compile()
