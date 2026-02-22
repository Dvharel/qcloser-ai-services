from langgraph.graph import StateGraph, END
from .state import FollowupState
from app.agents.followup_agent import run_followup_agent


def build_followup_graph():
    g = StateGraph(FollowupState)
    g.add_node("followup_agent", run_followup_agent)
    g.set_entry_point("followup_agent")
    g.add_edge("followup_agent", END)
    return g.compile()
