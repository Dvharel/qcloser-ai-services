def run_analysis_agent(state):
    transcript = state["transcript"]
    lang = state["language"]
    deal_title = state.get("deal_title")

    # TODO: Replace with sales-book prompt + LLM call
    # For now: deterministic output so pipeline works
    analysis_text = f"[ANALYSIS][{lang}] Deal={deal_title or 'N/A'}\nSummary:\n{transcript[:400]}..."

    state["analysis_text"] = analysis_text
    state["raw"] = {"stub": True}
    return state
