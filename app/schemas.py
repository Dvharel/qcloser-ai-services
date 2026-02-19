from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any, Literal

class AnalyzeRequest(BaseModel):
    transcript: str
    language: Optional[str] = Field(default="auto", description="he/en/None")
    org_id: Optional[int] = None
    recording_id: Optional[int] = None

class AnalyzeResponse(BaseModel):
    nuggets: List[str] = Field(default_factory=list)
    patterns: List[str] = Field(default_factory=list)
    risks: List[str] = Field(default_factory=list)
    next_questions: List[str] = Field(default_factory=list)
    closing_outlook: Dict[str, Any]
    raw_response: Optional[str] = None

class FollowupRequest(BaseModel):
    analysis: AnalyzeResponse
    channel: Literal["email"] = "whatsapp" # maybe add whatsapp later
    transcript: str
    analysis: str
    language: Optional[str] = None
    channel: str = "whatsapp"   # whatsapp/email

class FollowupResponse(BaseModel):
    followup_message: str
    sales_brief: str
    continuation_plan: str

class FeedbackRequest(BaseModel):
    recording_id: int
    rating: int = Field(ge=1, le=5)
    notes: Optional[str] = None
