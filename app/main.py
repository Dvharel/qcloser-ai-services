import os
from fastapi import FastAPI, Header, HTTPException
from starlette import status

from app.schemas import (
    AnalyzeRequest,
    AnalyzeResponse,
    FeedbackRequest,
    FeedbackResponse,
    FollowupRequest,
    FollowupResponse,
)

from app.graph.analyze_graph import build_analyze_graph
from app.graph.feedback_graph import build_feedback_graph
from app.graph.followup_graph import build_followup_graph

app = FastAPI(title="QCloser AI Service", version="0.1")

AI_SERVICE_TOKEN = os.getenv("AI_SERVICE_TOKEN")


def verify_token(x_ai_token: str | None):
    if not AI_SERVICE_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="AI_SERVICE_TOKEN is not configured on the AI service server.",
        )
    if x_ai_token != AI_SERVICE_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing X-AI-Token header.",
        )


_analyze_graph = build_analyze_graph()
_feedback_graph = build_feedback_graph()
_followup_graph = build_followup_graph()


@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(
    req: AnalyzeRequest,
    x_ai_token: str | None = Header(default=None, alias="X-AI-Token"),
):
    verify_token(x_ai_token)

    state = {
        "recording_id": req.recording_id,
        "transcript": req.transcript,
        "language": req.language,
        "deal_title": req.deal_title,
        "analysis_text": None,
        "raw": None,
    }
    out = _analyze_graph.invoke(state)
    return AnalyzeResponse(analysis_text=out["analysis_text"], raw=out.get("raw"))


@app.post("/feedback", response_model=FeedbackResponse)
def feedback(
    req: FeedbackRequest,
    x_ai_token: str | None = Header(default=None, alias="X-AI-Token"),
):
    verify_token(x_ai_token)

    state = {
        "recording_id": req.recording_id,
        "transcript": req.transcript,
        "analysis_text": req.analysis_text,
        "language": req.language,
        "feedback_text": None,
        "raw": None,
    }
    out = _feedback_graph.invoke(state)
    return FeedbackResponse(feedback_text=out["feedback_text"], raw=out.get("raw"))


@app.post("/followup", response_model=FollowupResponse)
def followup(
    req: FollowupRequest,
    x_ai_token: str | None = Header(default=None, alias="X-AI-Token"),
):
    verify_token(x_ai_token)

    state = {
        "recording_id": req.recording_id,
        "transcript": req.transcript,
        "analysis_text": req.analysis_text,
        "language": req.language,
        "channel": req.channel,
        "tone": req.tone,
        "followup": None,
        "raw": None,
    }
    out = _followup_graph.invoke(state)
    return FollowupResponse(followup=out["followup"], raw=out.get("raw"))
