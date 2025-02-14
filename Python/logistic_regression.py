import pandas as pd
import re

read_data = pd.read_csv("D:\\Python\\sentiment_analysis.csv")

# print(read_data.head())

def cleanText(text):
    clean_text = re.sub("[^a-zA-Z\\s]","",text)
    return clean_text.lower()



read_data["clean_description"] = read_data["description"].apply(cleanText)

# print(read_data.head())

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(max_features=1000)

features = vectorizer.fit_transform(read_data["clean_description"]).toarray()
target = read_data["sentiment"]

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)

print(f"accuracy : {accuracy * 100 : .2f}%")

new_review = ["Movies was good, but i am not that much satified and i am also not regretting."]

new_review_clean = cleanText(new_review[0])

new_review_vec = vectorizer.transform([new_review_clean]).toarray()


prediction = model.predict(new_review_vec)
print(prediction[0])




