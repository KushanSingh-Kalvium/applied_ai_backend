from transformers import pipeline

MODEL_NAME = "distilbert-base-uncased-finetuned-sst-2-english"

_sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model=MODEL_NAME
)

def analyze_sentiment(text: str) -> tuple[str, float]:
    result = _sentiment_pipeline(text)[0]
    return result["label"].lower(), float(result["score"])
