# # import nltk

# # nltk.data.path.append("D:/Python/nltk_data")

# # print(nltk.data.path)

# from nltk import word_tokenize, sent_tokenize

# sent = "Madhav is a good boy. Madhav has krishna as his best friends."

# print(word_tokenize(sent))
# print(sent_tokenize(sent))


import nltk

# Overwrite default paths
# nltk.data.path = ["D:/Python/nltk_data"]

# Verify path
print(nltk.data.path)  # Output should show only ['D:/Python/nltk_data']
