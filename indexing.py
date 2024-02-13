#-------------------------------------------------------------------------
# AUTHOR: Thoa Nguyen
# FILENAME: Assignment 1 question 8
# SPECIFICATION: read the file collection.csv and output the tf-idf document-term matrix
# FOR: CS 4250- Assignment #1
# TIME SPENT: 3.5hr
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard arrays

#Importing some Python libraries
import csv
import math

documents = []

#Reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
         if i > 0:  # skipping the header
            documents.append (row[0])

#Conducting stopword removal. Hint: use a set to define your stopwords.

documents = [doc.split(" ") for doc in documents]
stopWords = {'I', 'and', 'She', 'They', 'her', 'their'}
#Remove stopwords
for i, doc in enumerate(documents):
    n_doc = [word for word in doc if word not in stopWords]
    documents[i] = n_doc

#Conducting stemming. Hint: use a dictionary to map word variations to their stem.
#--> add your Python code here
steeming = {
  "loves": "love",
  "dogs": "dog",
  "cats": "cat",
}
for doc in documents:
  for i, word in enumerate(doc):
    doc[i] = steeming.get(word, word)
#Identifying the index terms.
#--> add your Python code here
terms = list(set(word for doc in documents for word in doc))

# TF-IDF calculations
def tf(word, doc):
    return doc.count(word) / len(doc)

def df(word):
    return sum(1 for doc in documents if word in doc)

def idf(word):
    return math.log(len(documents) / df(word), 10)

def tf_idf(word, doc):
    return tf(word, doc) * idf(word)

#Building the document-term matrix by using the tf-idf weights.
#--> add your Python code here
docTermMatrix = []

for i, doc in enumerate(documents):
    current_doc = [round(tf_idf(term, doc), 4) for term in terms]
    docTermMatrix.append(current_doc)

# Printing the document-term matrix
tcolumns = "        "

for term in terms:
    tcolumns += f"| {term}    " if len(str(term)) < 4 else f"| {term}   "

print(tcolumns)

for i, DWeights in enumerate(docTermMatrix):
    scores = f"Doc {i + 1}:"
    scores += "\t|" + "\t|".join(map(lambda x: f"{x:.3f}", DWeights))
    print(scores)

print()
