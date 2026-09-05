#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: index.py
# SPECIFICATION: builds an inverted index using normalization and lemmatization
# FOR: CS 4250 - Assignment #1
# TIME SPENT: how long it took you to complete the assignment
#-------------------------------------------------------------------------

# Importing Python libraries
import pandas as pd

# Reading the document collection
data = pd.read_csv("collection.csv")

# Defining the dictionary used for lemmatization
# --> add your Python code here
lemmas = {
    "homes": "home",
    "sales": "sale",
    "increases": "increase",
    "increasing": "increase",
    "rising": "rise"
}

# Creating the data structure that will store the inverted index
invertedIndex = {}

# Processing each document in the collection
for i, row in data.iterrows():

    docID = row["Document"]
    text = row["Text"]

    # Applying surface-level normalization
    # --> add your Python code here
    text = text.lower().replace(".", "")

    # Tokenizing the document
    # --> add your Python code here
    tokens = text.split()

    # Applying lemmatization
    # --> add your Python code here
    tokens = [lemmas.get(token, token) for token in tokens]

    # Building the inverted index
    # --> add your Python code here
    for term in tokens:
        if term not in invertedIndex:
            invertedIndex[term] = []

        if docID not in invertedIndex[term]:
            invertedIndex[term].append(docID)

# Printing the inverted index with terms ordered alphabetically
# Expected format:
# term1 : ['Doc1', 'Doc2']
# term2 : ['Doc3']
# --> add your Python code here
for term in sorted(invertedIndex):
    print(term, ":", invertedIndex[term])
