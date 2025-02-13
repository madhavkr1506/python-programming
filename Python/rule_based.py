import re
import pandas as pd

def cleanText(text):
    clean_text = re.sub(r"[^a-zA-Z\s]","", text)
    return clean_text.split()


# text = "Madhav is a good boy, and he has some coding ability."
# clean_text = cleanText(text)
# print(clean_text)

positive_words = ["love", "awesome", "great", "amazing", "happy", "good", "fantastic"]
negative_words = ["hate", "awful", "bad", "terrible", "sad", "hard", "worst"]

def analyzeSentiment(text):
    clean_text = cleanText(text)

    positive_sum = 0
    negative_sum = 0

    positive_sum += sum(1 for word in clean_text if word in positive_words)
    negative_sum += sum(i for word in clean_text if word in negative_words)

    if(positive_sum > negative_sum):
        return "Positive sentiment"
    elif(positive_sum < negative_sum):
        return "Negative sentiment"
    else:
        return "Neutral sentiment"

data = pd.read_csv("C:\\Users\\madha\\Documents\\netflix_titles.csv")

description_column = data["description"].dropna().head()

for i in range(len(description_column)):
    print(f"description: {description_column.iloc[i]}")
    print(f"sentiment analysis: {analyzeSentiment(description_column.iloc[i])}")




