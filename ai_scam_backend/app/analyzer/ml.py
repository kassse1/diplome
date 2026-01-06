def ml_score(text: str) -> float:
    suspicious_phrases = [
        "you won", "free money", "act now",
        "account suspended", "verify your account"
    ]

    text_l = text.lower()
    if any(p in text_l for p in suspicious_phrases):
        return 0.7

    return 0.3
