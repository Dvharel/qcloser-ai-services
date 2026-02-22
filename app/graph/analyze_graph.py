from langgraph.graph import StateGraph, END
from .state import AnalyzeState
from app.agents.analysis_agent import run_analysis_agent


def build_analyze_graph():
    g = StateGraph(AnalyzeState)
    g.add_node("analysis_agent", run_analysis_agent)
    g.set_entry_point("analysis_agent")
    g.add_edge("analysis_agent", END)
    return g.compile()
