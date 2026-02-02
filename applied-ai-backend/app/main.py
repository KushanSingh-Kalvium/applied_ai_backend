from fastapi import FastAPI
from app.core.config import settings
from app.api.routes import router

app = FastAPI(title=settings.APP_NAME)

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(router)
