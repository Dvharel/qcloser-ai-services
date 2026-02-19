import os
from fastapi import FastAPI, Header, HTTPException, Request
from .schemas import (
    AnalyzeRequest,
    AnalyzeResponse,
    FollowupRequest,
    FollowupResponse,
    FeedbackRequest,
)
from starlette import status

app = FastAPI(title="Q-Closer AI Service")

AI_SERVICE_TOKEN = os.getenv("AI_SERVICE_TOKEN", "")


def verify_token(x_ai_token: str | None):
    if not AI_SERVICE_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="AI_SERVICE_TOKEN is not configured on the server.",
        )

    if x_ai_token != AI_SERVICE_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing X-AI-TOKEN header.",
        )


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(
    req: AnalyzeRequest,
    request: Request,
    x_ai_token: str | None = Header(default=None, alias="X-AI-Token"),
):

    print("DEBUG headers:", dict(request.headers))
    print("DEBUG x_ai_token:", x_ai_token)
    print("DEBUG X-AI-Token:", request.headers.get("x-ai-token"))
    verify_token(x_ai_token)

    # MVP: implement provider call here (OpenAI later) or stub
    # For now return deterministic structure so Django integration works.
    return AnalyzeResponse(
        nuggets=["Nugget 1", "Nugget 2"],
        patterns=["Example pattern"],
        risks=["Risk 1"],
        next_questions=["Question 1"],
        closing_outlook={"score": 0.7, "reason": "Good fit"},
    )


@app.post("/generate_followup", response_model=FollowupResponse)
def generate_followup(
    req: FollowupRequest, x_ai_token: str | None = Header(default=None)
):
    verify_token(x_ai_token)

    return FollowupResponse(
        followup_message="היי! תודה על השיחה...",
        sales_brief="Brief: customer wants...",
        continuation_plan="Next: schedule demo...",
    )


@app.post("/feedback")
def feedback(req: FeedbackRequest, x_ai_token: str | None = Header(default=None)):
    verify_token(x_ai_token)
    # MVP: just ack. Later: store in DB or analytics.
    return {"status": "received"}
