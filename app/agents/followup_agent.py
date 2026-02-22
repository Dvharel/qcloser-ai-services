def run_followup_agent(state):
    # TODO: Replace with follow-up generation prompt + LLM call
    followup = {
        "subject": "Next steps from our conversation",
        "message_to_client": "Hey! Thanks again for your time — here’s what I suggest we do next...",
        "brief_for_rep": "Client key points + objections summary...",
        "next_steps": ["Confirm budget", "Schedule demo", "Send proposal"],
    }

    state["followup"] = followup
    state["raw"] = {"stub": True}
    return state
