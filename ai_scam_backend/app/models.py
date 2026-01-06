from transformers import pipeline

class ScamDetector:
    def __init__(self):
        self.model = pipeline(
            "text-classification",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )

        # 🔍 Триггерные паттерны (explainability)
        self.triggers = {
            "urgent": ["urgent", "immediately", "срочно", "немедленно"],
            "reward": ["win", "won", "prize", "вы выиграли", "бонус"],
            "action": ["click", "link", "перейдите", "нажмите"],
        }

    def analyze(self, text: str) -> dict:
        result = self.model(text)[0]
        risk_score = round(result["score"] * 100, 2)

        reasons = self._explain(text)

        return {
            "label": result["label"],
            "risk_score": risk_score,
            "verdict": "HIGH RISK" if risk_score > 70 else "LOW RISK",
            "reasons": reasons
        }

    def _explain(self, text: str):
        text_lower = text.lower()
        reasons = []

        if any(word in text_lower for word in self.triggers["urgent"]):
            reasons.append("Urgent language detected")

        if any(word in text_lower for word in self.triggers["reward"]):
            reasons.append("Promise of reward detected")

        if any(word in text_lower for word in self.triggers["action"]):
            reasons.append("Call-to-action phrase detected")

        if not reasons:
            reasons.append("No explicit scam patterns detected")

        return reasons