from pydantic import BaseModel, Field
from typing import Optional, Literal, Dict, Any, List


Language = Literal["auto", "he", "en"]


class AnalyzeRequest(BaseModel):
    recording_id: int
    transcript: str
    language: Language = "auto"
    deal_title: Optional[str] = None


class AnalyzeResponse(BaseModel):
    analysis_text: str
    raw: Optional[Dict[str, Any]] = None


class FeedbackRequest(BaseModel):
    recording_id: int
    transcript: str
    analysis_text: str
    language: Language = "auto"


class FeedbackResponse(BaseModel):
    feedback_text: str
    raw: Optional[Dict[str, Any]] = None


class FollowupRequest(BaseModel):
    recording_id: int
    transcript: str
    analysis_text: str
    language: Language = "auto"
    channel: str = "whatsapp"
    tone: str = "friendly"


class FollowupResponse(BaseModel):
    followup: Dict[str, Any] = Field(
        ...,
        description="JSON with keys: subject, message_to_client, brief_for_rep, next_steps",
    )
    raw: Optional[Dict[str, Any]] = None
