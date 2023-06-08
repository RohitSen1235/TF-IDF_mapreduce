#!/usr/bin/env python

from string import punctuation
import sys
import os
# from nltk.corpus import stopwords

def mapper():
    # Retrieve NLTK stopwords for English
    # stopwords = set(stopwords.words('english'))
    stopwords = {
        'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for',
        'from', 'has', 'he', 'in', 'is', 'it', 'its', 'of', 'on',
        'that', 'the', 'to', 'was', 'were', 'will', 'with',
        'about', 'after', 'all', 'also', 'an', 'another', 'any',
        'because', 'been', 'before', 'being', 'between', 'both',
        'but', 'came', 'can', 'come', 'could', 'did', 'do', 'does',
        'each', 'else', 'for', 'get', 'got', 'has', 'had', 'he',
        'have', 'her', 'here', 'him', 'himself', 'his', 'how',
        'if', 'in', 'into', 'is', 'it', 'like', 'make', 'many',
        'me', 'might', 'more', 'most', 'much', 'must', 'my',
        'never', 'now', 'of', 'on', 'only', 'or', 'other', 'our',
        'out', 'over', 're', 'said', 'same', 'see', 'should',
        'since', 'so', 'some', 'still', 'such', 'take', 'than',
        'that', 'the', 'their', 'them', 'then', 'there', 'these',
        'they', 'this', 'those', 'through', 'to', 'too', 'under',
        'up', 'use', 'very', 'want', 'was', 'way', 'we', 'well',
        'were', 'what', 'when', 'where', 'which', 'while', 'who',
        'will', 'with', 'would', 'you', 'your'
    }


    # TF-IDF computation: Phase One
    # Mapper output: <<word, document_name>   1>

    # Get the input file name from the environment variable
    input_file = os.getenv('map_input_file')

    # Extract the doc_id from the input file name
    # doc_id = input_file.split('_')[0]
    doc_id = input_file.split("/")[-1]

    for line in sys.stdin:
        line = line.translate(str.maketrans('', '', punctuation)).strip('\t')
        line_contents = line.split(" ")
        for word in line_contents:
            word = word.rstrip().lower()  # Convert word to lowercase
            # Skip processing if the word is a stopword or digit
            if word not in stopwords and not word.isdigit():
                key = word + "," + doc_id
                print('%s\t%s' % (key, 1))

if __name__ == "__main__":
    mapper()
