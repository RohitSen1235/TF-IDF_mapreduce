#!/usr/bin/env python

from sklearn.externals import joblib
import pickle
import sys

# Load the TF-IDF vectorizer
with open('tfidf_vectorizer.pkl', 'rb') as file:
    tfidf_vectorizer = pickle.load(file)

for line in sys.stdin:
    # Split the line into document ID, rating, and content
    parts = line.strip().split('\t')
    document_id = parts[0]
    rating = int(parts[1])
    content = parts[2]

    # Perform TF-IDF transformation on the content
    tfidf_matrix = tfidf_vectorizer.transform([content])

    # Emit the document ID, rating, and TF-IDF matrix as output
    output = f'{document_id}\t{rating}\t{tfidf_matrix.toarray().tolist()}'
    print(output)
