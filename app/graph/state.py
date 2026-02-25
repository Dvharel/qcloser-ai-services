from typing import TypedDict, Optional, Dict, Any


class AnalyzeState(TypedDict):
    recording_id: int
    transcript: str
    language: str
    deal_title: Optional[str]
    analysis_json: Optional[Dict[str, Any]]
    raw: Optional[Dict[str, Any]]


class FeedbackState(TypedDict):
    recording_id: int
    transcript: str
    analysis_json: Optional[Dict[str, Any]]
    language: str
    feedback_json: Optional[str]
    raw: Optional[Dict[str, Any]]


class FollowupState(TypedDict):
    recording_id: int
    transcript: str
    analysis_json: Optional[Dict[str, Any]]
    feedback_json: str
    language: str
    channel: str
    tone: str
    followup: Optional[Dict[str, Any]]
    raw: Optional[Dict[str, Any]]
