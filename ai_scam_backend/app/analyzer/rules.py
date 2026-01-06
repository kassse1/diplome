SCAM_PATTERNS = {
    "urgency": [
        "срочно", "немедленно", "прямо сейчас", "последний шанс",
        "urgent", "urgente", "шұғыл"
    ],
    "money": [
        "деньги", "перевод", "оплата", "платёж", "оплатить",
        "тенге", "руб", "доллар", "евро", "$", "€"
    ],
    "profit": [
        "вы выиграли", "выигрыш", "приз", "бонус",
        "гарантированный доход", "без риска",
        "won", "ganado", "ganhou", "ұтып"
    ],
    "pressure": [
        "подтвердите", "верификация", "подтверждение",
        "аккаунт будет заблокирован", "заблокирован",
        "confirm", "verify", "blocked"
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
