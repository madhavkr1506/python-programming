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

# data = pd.read_csv("C:\\Users\\madha\\Documents\\netflix_titles.csv")
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


# Use read_csv() with parameters like chunksize for large files.

# data = pd.read_csv("C:\\Users\\madha\\Documents\\netflix_titles.csv", chunksize=1000)
# for chunk in data :
    # print(chunk.head())


# df = pd.DataFrame({
#     'City': ['New York', 'New York', 'London', 'London'],
#     'Year': [2020, 2021, 2020, 2021],
#     'Population': [8.3, 8.4, 9.3, 9.4]
# })

# df = df.set_index(["City","Year"])

# Ab hum City aur Year columns ko index bana rahe hain.

# Index ka kaam hota hai ki DataFrame me rows ko uniquely identify kar sakein.
# set_index(['City', 'Year']) ka matlab hai:
# City aur Year ko ek hierarchical index bana diya.
# Pehle level pe City hoga, aur uske andar Year.

# Ab hum df.loc[] ka use karke rows ko access karte hain.
# print(df.loc["New York"])


df = pd.DataFrame({
    'Team': ['A', 'A', 'B', 'B'],
    'Score': [10, 20, 15, 25],
    'Penalties': [1, 2, 0, 1]
})

df = df.groupby("Team")
df = df.agg({"Score" : ["mean","max"], "Penalties" : "sum"})
print(df)


