from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification",
    model="joeddav/xlm-roberta-large-xnli",
    tokenizer="joeddav/xlm-roberta-large-xnli",
    framework="pt",
    device=-1,
    use_fast=False
)

SCAM_LABELS = [
    "scam",
    "fraud",
    "phishing",
    "financial scam",
    "safe message"
]

SAFE_LABEL = "safe message"


def ml_score(text: str) -> float:
    """
    Returns probability of scam using zero-shot multilingual model.
    """
    result = classifier(
        text,
        candidate_labels=SCAM_LABELS,
        hypothesis_template="This message is {}."
    )

    labels = result["labels"]
    scores = result["scores"]

    scam_scores = []

    for label, score in zip(labels, scores):
        if label != SAFE_LABEL:
            scam_scores.append(score)

    if not scam_scores:
        return 0.0

    return round(float(max(scam_scores)), 2)
