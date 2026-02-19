from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class AnalyzeRequest(BaseModel):
    transcript: str
    language: Optional[str] = Field(default=None, description="he/en/None")
    org_id: Optional[int] = None
    recording_id: Optional[int] = None

class AnalyzeResponse(BaseModel):
    nuggets: List[str]
    patterns: List[str]
    risks: List[str]
    next_questions: List[str]
    closing_outlook: Dict[str, Any]

class FollowupRequest(BaseModel):
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
    rating: int  # 1-5
    notes: Optional[str] = None
