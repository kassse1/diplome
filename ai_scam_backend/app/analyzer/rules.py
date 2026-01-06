SCAM_PATTERNS = {
    "urgency": [
        "urgent", "immediately", "act now", "last chance",
        "срочно", "немедленно", "прямо сейчас", "последний шанс",
        "urgente", "шұғыл"
    ],

    "money": [
        "money", "payment", "transfer", "send",
        "деньги", "перевод", "оплата", "платёж",
        "тенге", "руб", "доллар", "евро", "$", "€"
    ],

    "profit": [
        "you won", "won money", "free money",
        "вы выиграли", "выигрыш", "приз", "бонус",
        "ganado", "ganhou", "ұтып"
    ],

    "pressure": [
        "verify", "confirm", "blocked", "suspended",
        "подтвердите", "верификация", "заблокирован",
        "confirmar", "bloqueado"
    ],
"investment": [
    # EN
    "invest",
    "investment",
    "double your money",
    "guaranteed profit",
    "no risk",
    "high return",

    # RU
    "инвест",
    "инвестици",
    "гарантирован",
    "доход",
    "без риска",

    # ES
    "invertir",
    "inversión",
    "ganancias garantizadas",
    "sin riesgo",
    "duplica tu dinero",

    # PT
    "investir",
    "investimento",
    "lucro garantido",
    "sem risco",
    "dobrar seu dinheiro",

    # KZ
    "инвестиция",
    "табыс",
    "пайда",
    "тәуекелсіз",
],

    "phishing": [
    # EN
    "verify your identity",
    "verify your account",
    "account has been suspended",
    "account suspended",
    "restore access",
    "security alert",
    "bank account",

    # RU
    "служба поддержки банка",
    "подтвердите данные",
    "подтвердите личность",
    "аккаунт заблокирован",
    "блокировка счёта",
    "служба безопасности",

    # ES
    "verifique su identidad",
    "cuenta suspendida",
    "cuenta bancaria",
    "restaurar el acceso",
    "alerta de seguridad",

    # PT
    "verifique sua identidade",
    "conta suspensa",
    "conta bancária",
    "restaurar acesso",
    "alerta de segurança",

    # KZ
    "банк қызметі",
    "шотыңыз бұғатталды",
    "деректерді растаңыз",
    "қауіпсіздік қызметі",
],

    "links": [
        "http://", "https://", "www."
    ],
}


def rule_based_analysis(text: str):
    text_l = text.lower()
    score = 0.0
    signals = []

    for category, patterns in SCAM_PATTERNS.items():
        if any(p in text_l for p in patterns):
            signals.append(category)

    # 🔴 HARD RULE: BANK PHISHING = SCAM
    if "phishing" in signals:
        return 1.0, signals

    # 🔴 HARD RULE: PROFIT + PRESSURE
    if "profit" in signals and ("urgency" in signals or "money" in signals):
        return 1.0, signals

    # soft scoring
    score = 0.25 * len(signals)

    return min(score, 0.9), signals
