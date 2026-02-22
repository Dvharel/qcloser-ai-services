def run_feedback_agent(state):
    # TODO: Replace with sales-book feedback rubric + LLM call
    feedback_text = f"[FEEDBACK]\nBased on analysis:\n{state['analysis_text'][:250]}..."

    state["feedback_text"] = feedback_text
    state["raw"] = {"stub": True}
    return state
