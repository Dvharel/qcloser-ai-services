from pathlib import Path
from app.providers.openai_provider import chat_completion

PROMPT_PATH = Path(__file__).parent / "prompts" / "analyze.md"


def _load_prompt() -> str:
    return PROMPT_PATH.read_text(encoding="utf-8")


def run_analysis_agent(*, transcript: str, language: str) -> dict:
    system_prompt = _load_prompt()

    # Optional: help the model keep language consistent
    user_prompt = f"""Transcript language: {language}
Transcript:
{transcript}
"""

    analysis_text = chat_completion(
        system=system_prompt,
        user=user_prompt,
    )

    return {
        "analysis_json": {"analysis_text": analysis_text},
        "raw": None,
    }
