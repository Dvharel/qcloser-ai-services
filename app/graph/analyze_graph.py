from langgraph.graph import StateGraph, END
from .state import AnalyzeState
from app.agents.analysis_agent import run_analysis_agent


def _node_analyze(state: AnalyzeState):
    out = run_analysis_agent(transcript=state["transcript"], language=state["language"])
    return out


def build_analyze_graph():
    g = StateGraph(AnalyzeState)
    g.add_node("analyze", _node_analyze)
    g.set_entry_point("analyze")
    return g.compile()
