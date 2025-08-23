# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd 

# analyzer = SentimentIntensityAnalyzer()

# read_data = pd.read_csv("C:\\Users\\madha\\Documents\\netflix_titles.csv")

# print(read_data.head())


# movie_description = read_data["description"]
# print(movie_description.head())

# movie_description.to_csv("movie_description.csv", index=False)


# read_movie_description = pd.read_csv("D:\\Python\\movie_description.csv")

# print(read_movie_description.head())

# movie_description_column = read_movie_description["description"].dropna().head()


# def getSentiment(description):
#     scores = analyzer.polarity_scores(description)
#     return "positive" if scores["compound"] > 0 else "negative" if scores["compound"] < 0 else "neutral"


# read_movie_description["sentiment"] = read_movie_description["description"].apply(getSentiment)

# read_movie_description.to_csv("sentiment_analysis.csv", index=False)
    

