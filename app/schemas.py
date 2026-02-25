from pydantic import BaseModel, Field
from typing import Optional, Literal, Dict, Any, List


Language = Literal["auto", "he", "en"]


class AnalyzeRequest(BaseModel):
    recording_id: int
    transcript: str
    language: Language = "auto"
    deal_title: Optional[str] = None


class AnalyzeResponse(BaseModel):
    analysis_json: Dict[str, Any] = Field(
        ..., description="Freeform SPIN analysis wrapped in JSON"
    )
    raw: Optional[Dict[str, Any]] = None


class FeedbackRequest(BaseModel):
    recording_id: int
    transcript: str
    analysis_json: Dict[str, Any]
    deal_title: str
    language: Language = "auto"


class FeedbackResponse(BaseModel):
    feedback_json: Dict[str, Any] = Field(
        ..., description="Freeform SPIN coaching feedback wrapped in JSON"
    )
    raw: Optional[Dict[str, Any]] = None


class FollowupRequest(BaseModel):
    transcript: str
    analysis_json: Dict[str, Any]
    language: Language = "auto"
    deal_title: str
    recording_id: int
    channel: str = "email"
    tone: str = "friendly"


class FollowupResponse(BaseModel):
    followup: Dict[str, Any]
    raw: Optional[Dict[str, Any]] = None
