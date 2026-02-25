from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

from app.providers.openai_provider import call_llm_json  # rename if yours differs

PROMPT_PATH = Path(__file__).parent / "prompts" / "followup.md"


def run_followup_agent(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    LangGraph node.

    Expects in state:
      - transcript (str)
      - analysis (dict | str | None)   # in your MVP you said analysis_json is freeform text soon
      - feedback (dict | str | None)  # followup after feedback, so include it
      - language (str: 'he'/'en'/'auto')
      - channel (str: 'whatsapp'/'email'/...)
      - tone (str: e.g. 'friendly')
      - org_id (int)
      - recording_id (int)

    Returns:
      - followup_json (dict)  # must contain: message, subject, brief_for_rep, next_steps
      - raw (optional)
    """

    system_prompt = PROMPT_PATH.read_text(encoding="utf-8")

    user_payload = {
        "transcript": state.get("transcript", ""),
        "analysis": state.get("analysis"),  # could be text or dict
        "feedback": state.get("feedback"),  # could be text or dict
        "language": state.get("language", "auto"),
        "channel": state.get("channel", "whatsapp"),
        "tone": state.get("tone", "friendly"),
        "org_id": state.get("org_id"),
        "recording_id": state.get("recording_id"),
    }

    followup_json, raw = call_llm_json(
        system_prompt=system_prompt,
        user_payload=user_payload,
    )

    # Optional safety: ensure required keys exist (prevents silent bad outputs)
    for k in ("message", "subject", "brief_for_rep", "next_steps"):
        followup_json.setdefault(k, "" if k != "next_steps" else [])

    return {
        "followup": followup_json,
        "raw": raw,  # optional
    }
