from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

from app.providers.openai_provider import call_llm_json

PROMPT_PATH = Path(__file__).parent / "prompts" / "feedback.md"


def run_feedback_agent(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Expects in state:
      - transcript (str)
      - analysis (dict|str|None) optional
      - language (str) optional
      - org_id, recording_id optional

    Returns:
      - feedback_json (dict)
      - raw (optional)
    """
    prompt = PROMPT_PATH.read_text(encoding="utf-8")

    system_prompt = (
        prompt
        + """

Return ONLY valid JSON. No markdown, no extra text.

JSON schema (exact top-level keys):
{
  "spin_execution_quality": {
    "situation_questions": {"assessment": "", "examples": [], "notes": ""},
    "problem_questions": {"assessment": "", "examples": [], "notes": ""},
    "implication_questions": {"assessment": "", "examples": [], "notes": ""},
    "need_payoff_questions": {"assessment": "", "examples": [], "notes": ""}
  },
  "value_development": {
    "seriousness": {"assessment": "", "evidence": [], "notes": ""},
    "urgency": {"assessment": "", "evidence": [], "notes": ""},
    "buyer_verbalized_value": {"assessment": "", "evidence": [], "notes": ""}
  },
  "objection_prevention_vs_reaction": {
    "assessment": "",
    "evidence": [],
    "notes": ""
  },
  "commitment_strategy": {
    "pushed_too_early": {"assessment": "", "evidence": [], "notes": ""},
    "realistic_advance": {"assessment": "", "evidence": [], "notes": ""},
    "next_step_clear": {"assessment": "", "evidence": [], "notes": ""}
  },
  "specific_coaching": {
    "missing_questions": [{"question": "", "why": "", "better_version": ""}],
    "example_phrasing": [],
    "keep_doing": [],
    "improve_next_call": []
  }
}

Rules:
- Write in the same language as the transcript.
- Be specific and quote SHORT phrases from the transcript in "evidence"/"examples" when helpful.
- Do not invent.
"""
    )

    user_payload = {
        "transcript": state.get("transcript", ""),
        "analysis": state.get("analysis"),
        "language": state.get("language", "auto"),
        "org_id": state.get("org_id"),
        "recording_id": state.get("recording_id"),
    }

    feedback_json, raw = call_llm_json(
        system_prompt=system_prompt,
        user_payload=user_payload,
    )

    return {
        "feedback_json": feedback_json,
        "raw": raw,
    }
