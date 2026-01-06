from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models import ScamDetector
from app.schemas import TextRequest

app = FastAPI(
    title="AI Scam Detection API",
    description="Backend for detecting fraudulent messages using NLP",
    version="1.0"
)

# ✅ CORS (ОБЯЗАТЕЛЬНО ДЛЯ FLUTTER WEB)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # для прототипа
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

detector = ScamDetector()


@app.post("/analyze")
def analyze_text(request: TextRequest):
    return detector.analyze(request.text)