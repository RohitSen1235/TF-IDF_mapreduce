#!/usr/bin/env python
import sys

# Mapper
for line in sys.stdin:
    line = line.strip()
    word_doc, tf_idf = line.split('\t')
    word,doc_id = word_doc.split(',')
    print('%s\t%s,%s' % (doc_id, word, tf_idf))
