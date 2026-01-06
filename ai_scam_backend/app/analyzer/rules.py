SCAM_PATTERNS = {
    "urgency": [
        "urgent", "immediately", "act now", "last chance",
        "срочно", "немедленно", "последний шанс",
        "қазір", "шұғыл",
        "ahora", "urgente",
        "imediatamente"
    ],
    "money": [
        "money", "payment", "transfer", "send",
        "деньги", "перевод", "оплата",
        "tenge", "тенге", "dollar", "usd", "$", "€"
    ],
    "pressure": [
        "verify", "verification", "blocked", "suspended",
        "подтвердите", "заблокирован", "верификация",
        "confirmar", "bloqueado"
    ],
    "profit": [
        "guaranteed profit", "no risk", "easy money",
        "гарантированный доход", "без риска"
    ],
    "links": [
        "http://", "https://", "www."
    ]
}

def rule_based_analysis(text: str):
    text_l = text.lower()
    score = 0
    signals = []

    for category, patterns in SCAM_PATTERNS.items():
        if any(p in text_l for p in patterns):
            score += 0.25
            signals.append(category)

    return min(score, 1.0), signals
