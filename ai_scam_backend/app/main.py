from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.analyzer.hybrid import analyze_text

# ✅ СНАЧАЛА создаём приложение
app = FastAPI(title="AI Scam Detector")

# ✅ ПОТОМ добавляем CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ====== SCHEMAS ======

class AnalyzeRequest(BaseModel):
    text: str

# ====== ROUTES ======

@app.post("/analyze")
def analyze(req: AnalyzeRequest):
    return analyze_text(req.text)
