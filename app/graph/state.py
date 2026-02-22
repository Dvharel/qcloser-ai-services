from typing import TypedDict, Optional, Dict, Any


class AnalyzeState(TypedDict):
    recording_id: int
    transcript: str
    language: str
    deal_title: Optional[str]
    analysis_text: Optional[str]
    raw: Optional[Dict[str, Any]]


class FeedbackState(TypedDict):
    recording_id: int
    transcript: str
    analysis_text: str
    language: str
    feedback_text: Optional[str]
    raw: Optional[Dict[str, Any]]


class FollowupState(TypedDict):
    recording_id: int
    transcript: str
    analysis_text: str
    feedback_text: str
    language: str
    channel: str
    tone: str
    followup: Optional[Dict[str, Any]]
    raw: Optional[Dict[str, Any]]
