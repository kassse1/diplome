from .language import detect_language
from .rules import rule_based_analysis
from .semantic_ml import semantic_risk_score


def analyze_text(text: str) -> dict:
    lang = detect_language(text)

    # 1️⃣ RULES
    rule_score, signals = rule_based_analysis(text)

    # 🔴 HARD RULE: BANK PHISHING
    if "phishing" in signals:
        return {
            "language": lang,
            "verdict": "scam",
            "is_scam": True,
            "confidence": 0.95,
            "signals": signals,
            "method": "rules (hard) + semantic AI"
        }

    # 2️⃣ SEMANTIC AI (ОСНОВНОЙ ИСТОЧНИК)
    ai_score = semantic_risk_score(text)

    # 3️⃣ AGGREGATION
    risk = max(rule_score, ai_score)

    # 🟡 investment всегда минимум dangerous
    if "investment" in signals and risk < 0.35:
        risk = 0.35

    # 4️⃣ VERDICT
    if risk >= 0.7:
        verdict = "scam"
    elif risk >= 0.3:
        verdict = "dangerous"
    else:
        verdict = "safe"

    return {
        "language": lang,
        "verdict": verdict,
        "is_scam": verdict == "scam",
        "confidence": round(risk, 2),
        "signals": signals,
        "method": "semantic AI + rules"
    }
