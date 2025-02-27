import pandas as pd 

from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


readFile = pd.read_csv("D:\\ML\\Titanic_Dataset.csv")
# print(readFile.head())

readFile.drop(["Name", "PassengerId", "SibSp", "Parch", "Ticket", "Cabin", "Embarked"], axis="columns", inplace=True)

# print(readFile.head())

target = readFile.Survived
# print(target.head())

features = readFile.drop("Survived", axis="columns", inplace=False)
# print(features.head())

dummy = pd.get_dummies(features.Sex)
dummy = dummy.astype(int)

# print(dummy.head())

features = pd.concat([features, dummy], axis="columns")

# print(features.head())

features.drop("Sex",axis="columns" ,inplace=True)

# print(features.head())

# naColumn = features.isna().any()
# print(naColumn)

features.Age = features.Age.fillna(features.Age.mean())
# naColumn = features.isna().any()
# print(naColumn)

x_train, x_test, y_train, y_test = train_test_split(features, target, test_size = 0.20, random_state=0)

model = tree.DecisionTreeClassifier()

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

accuracy = accuracy_score(y_pred, y_test)

print(f"model accuracy: {accuracy * 100: .2f}")




