from transformers import pipeline

# Load sentiment model once
sentiment_model = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base-emotion")

def analyze_sentiment(text):
    try:
        result = sentiment_model(text[:512])[0]  # truncate long texts
        label = result["label"]
        return label
    except Exception as e:
        print(f"Sentiment analysis failed: {e}")
        return "neutral"

#extend utils/sentiment_labels.py to remap into custom buckets:
# example { "joy": "enthusiastic", "sadness": "bored", "anger": "tacky" }.