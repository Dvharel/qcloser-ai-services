import os
import json
from typing import Any, Dict, Tuple, Optional
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class OpenAIProviderError(RuntimeError):
    pass


def chat_completion(*, system: str, user: str, model: str = None) -> str:
    """
    Returns the assistant text.
    """
    model = model or os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    if not client.api_key:
        raise OpenAIProviderError("OPENAI_API_KEY is missing")

    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        temperature=0.3,
    )

    content = resp.choices[0].message.content
    return (content or "").strip()


def call_llm_json(
    *,
    system_prompt: str,
    user_payload: Dict[str, Any],
    model: Optional[str] = None,
    temperature: float = 0.2,
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """
    Calls the LLM and returns parsed JSON dict + raw response.
    Uses OpenAI response_format=json_object for reliability.
    """
    model = model or os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    if not client.api_key:
        raise OpenAIProviderError("OPENAI_API_KEY is missing")

    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": json.dumps(user_payload, ensure_ascii=False)},
        ],
        temperature=temperature,
        response_format={"type": "json_object"},
    )

    content = (resp.choices[0].message.content or "").strip()
    try:
        return json.loads(content), resp.model_dump()
    except json.JSONDecodeError as e:

        raise OpenAIProviderError(
            f"Model did not return valid JSON: {e}\nContent:\n{content}"
        )
