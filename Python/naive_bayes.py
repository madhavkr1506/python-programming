import pandas as pd 

readFile = pd.read_csv("Titanic_Dataset.csv")
# print(readFile.head())
# print(readFile.info())
readFile.drop(["PassengerId","Name","SibSp","Parch","Ticket","Cabin","Embarked"], axis="columns", inplace=True)

# print(readFile.head())

target = readFile.Survived
features = readFile.drop("Survived",axis="columns")

# print(target.head())
# print(features.head())

dummies = pd.get_dummies(features.Sex)
# print(dummies.head())
dummies = dummies.astype(int)
# print(dummies.head())

features = pd.concat([features, dummies], axis="columns")
# print(features.head())


features.drop("Sex", axis="columns", inplace=True)

# print(features.head())

# print(features.isna().any())

features.Age = features.Age.fillna(features.Age.mean())

# print(features.isna().any())


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.33, random_state=42)

# print(len(x_train))


from sklearn.naive_bayes import GaussianNB
model = GaussianNB()

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_pred, y_test)

import joblib
model_path = "D:\\ML\\GaussianNB.pkl"
joblib.dump(model,model_path)


print(accuracy)