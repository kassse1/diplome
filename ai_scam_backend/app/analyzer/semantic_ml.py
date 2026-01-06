from sentence_transformers import SentenceTransformer, util

# 🌍 multilingual semantic model
model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

SCAM_PROTOTYPES = [
    # 💸 money request
    "Please send money to my account urgently.",
    "Can you transfer money to me as soon as possible?",

    # 🏦 bank phishing
    "Your bank account has been suspended. Verify your identity.",
    "Confirm your bank details to restore access.",

    # 📈 investment scam
    "Guaranteed profit with no risk. Invest now.",
    "Double your money quickly with this investment.",

    # 🎁 prize scam
    "You have won a large sum of money. Claim your prize now.",
]

# 🔒 precompute embeddings once
prototype_embeddings = model.encode(
    SCAM_PROTOTYPES,
    convert_to_tensor=True,
    normalize_embeddings=True
)


def semantic_risk_score(text: str) -> float:
    text_emb = model.encode(
        text,
        convert_to_tensor=True,
        normalize_embeddings=True
    )

    similarities = util.cos_sim(text_emb, prototype_embeddings)[0]
    max_sim = float(similarities.max())

    return round(max_sim, 2)
