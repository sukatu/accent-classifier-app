from transformers import pipeline

accent_classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

labels = ["British English", "American English", "Australian English", "Indian English", "Nigerian English"]

def classify_accent(transcript):
    result = accent_classifier(transcript, candidate_labels=labels)
    top_label = result["labels"][0]
    score = round(result["scores"][0] * 100, 2)
    summary = f"The model is {score}% confident the speaker has a {top_label} accent."
    return top_label, score, summary
