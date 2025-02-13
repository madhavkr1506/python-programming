from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd 
analyzer = SentimentIntensityAnalyzer()

data = pd.read_csv("C:\\Users\\madha\\Documents\\netflix_titles.csv")

data_document = data["description"].dropna().head()

for doc in data_document:
    scores = analyzer.polarity_scores(doc)
    print(f"Document: {doc}")
    print(f"Scores: {scores}")
    print(f"Sentiment: {"Positive" if scores["compound"] > 0 else "Negative" if scores["compound"] < 0 else "Neutral"}")
    print()
    