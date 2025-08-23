import pandas as pd 
from datetime import datetime

# read_data = pd.read_csv("D:\\Python\\Student Depression Dataset.csv")

# print(read_data.head())
# print(read_data.count)

# rm_id_data = read_data.drop(columns=["id","Age"])

# select_number_type = rm_id_data.select_dtypes(include=["number"])
# select_target = rm_id_data["Profession"]
# select_number_type["Profession"] = select_target

# print(select_number_type.head())

# select_number_type.to_csv("clean_data.csv",index=False)

clean_read_data = pd.read_csv("D:\\Python\\clean_data.csv")
# print(clean_read_data.describe())

# print(clean_read_data.info())

from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


features = clean_read_data.iloc[:,:-1].dropna()
target = clean_read_data.iloc[:,-1].dropna()


# print(target.shape)

# print(features.shape)

# vectorizer = CountVectorizer(max_features=1000)

# features = vectorizer.fit_transform(features)
x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=1000)

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

accuracy = accuracy_score(y_pred, y_test)

print(f"model accuracy: {accuracy * 100 :.2f}%")