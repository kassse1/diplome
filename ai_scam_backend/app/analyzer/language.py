from langdetect import detect, LangDetectException

KZ_CHARS = set("әғқңөұүһі")

def detect_language(text: str) -> str:
    t = text.lower()

    # 🇰🇿 эвристика для казахского
    if any(ch in KZ_CHARS for ch in t):
        return "kk"

    try:
        return detect(text)
    except LangDetectException:
        return "unknown"
