from .language import detect_language
from .rules import rule_based_analysis
from .ml import ml_score

def analyze_text(text: str) -> dict:
    lang = detect_language(text)

    rule_score, signals = rule_based_analysis(text)
    ml_result = ml_score(text)

    # 🚨 жёсткое правило
    if "urgency" in signals and "money" in signals:
        final_score = max(ml_result, 0.7)
    else:
        final_score = rule_score * 0.4 + ml_result * 0.6

    return {
        "language": lang,
        "is_scam": final_score >= 0.5,
        "confidence": round(final_score, 2),
        "signals": signals,
        "method": "hybrid (rules + ml)"
    }

