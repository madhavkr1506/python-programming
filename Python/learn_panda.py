import pandas as pd


# A Series is like a single column of data
# data = pd.Series([10,11,17,19])
# print(data)


# A DataFrame is like a full table

# data = {"Name" : ['Madhav',"Krishna","Ram"], 
# "City" : ["Patna",'Delhi',"Mumbai"],
# "Mobile" : [9693744950, 9693744951, 9693744953]
# }

# data = pd.DataFrame(data)
# print(data)

data = pd.read_csv("C:\\Users\\madha\\Documents\\netflix_titles.csv")
# print(data)


# print(data.head())

# print(data.head())

# print(data.info())


# print(data.describe())

# print(data.columns)

# print(data["type"])


# filtered_data = data[data["type"] == "Movie"]

# data["new_column"] = "Hi"

# data["new_column"] = data["new_column"] + " Madhav"

# data = data.drop("new_column", axis=1)

# data = data.groupby("type")["release_year"].mean()

# print(data)

# import matplotlib.pyplot as plt

# data["release_year"].plot(kind = "bar")
# plt.show()



