#!/usr/bin/env python
import sys

# Reducer
current_doc_id = None
word_tfidf_dict = {}

for line in sys.stdin:
    line = line.strip()
    doc_id, word_tfidf = line.split('\t')
    word, tf_idf = word_tfidf.split(',')

    if current_doc_id == doc_id:
        word_tfidf_dict[word] = tf_idf
    else:
        if current_doc_id is not None:
            # Emit the current doc_id and its corresponding word-tf_idf dictionary
            print('%s\t%s' % (current_doc_id, word_tfidf_dict))

        current_doc_id = doc_id
        word_tfidf_dict = {word: tf_idf}

# Emit the last doc_id and its corresponding word-tf_idf dictionary
if current_doc_id is not None:
    print('%s\t%s' % (current_doc_id, word_tfidf_dict))
