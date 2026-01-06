def ml_score(text: str) -> float:
    """
    Language-agnostic heuristic ML stub.
    Works across languages using intent patterns.
    """
    t = text.lower()

    intent_patterns = [
        # winning / reward
        "won", "ganado", "ganhou", "ұтып", "win",

        # urgency
        "urgent", "urgente", "шұғыл", "immediately", "agora",

        # action pressure
        "act now", "confirme", "confirm", "receber", "алу",

        # money
        "money", "dinero", "dinheiro", "доллар", "euro", "$", "€"
    ]

    hits = sum(1 for p in intent_patterns if p in t)

    if hits >= 3:
        return 0.85
    if hits == 2:
        return 0.65
    if hits == 1:
        return 0.4

    return 0.2
