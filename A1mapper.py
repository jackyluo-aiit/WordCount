#!/usr/bin/python
# -*- coding: utf-8 -*
import sys
import re

# print(stopwords)
for line in sys.stdin:
    string = re.sub("[+\.\!\/_,$%^*(+\"\']+|[+——!,.?`~@#￥%……&*()[\]{}|:-]+","",line)
    word_string = re.sub(r'\d+','',string)
    ss = word_string.strip().split(' ')
    for word in ss:
        word = word.lower()
        print('%s\t%s' % (word,1))
