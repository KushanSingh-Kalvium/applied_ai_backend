from fastapi import APIRouter, Depends, Request
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.models import Analysis
from app.services.inference import analyze_sentiment

router = APIRouter()

class AnalyzeRequest(BaseModel):
    text: str


class AnalyzeResponse(BaseModel):
    sentiment: str
    confidence: float

@router.post("/analyze", response_model=AnalyzeResponse)
def analyze_text(payload: AnalyzeRequest, db: Session = Depends(get_db)):
    sentiment, confidence = analyze_sentiment(payload.text)

    confidence=round(confidence, 2)

    record = Analysis(
        input_text=payload.text,
        sentiment=sentiment,
        confidence=confidence,
        model_name="distilbert-base-uncased-finetuned-sst-2-english"
    )

    db.add(record)
    db.commit()

    return {
        "sentiment": sentiment,
        "confidence": confidence
    }
