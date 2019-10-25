#!/usr/bin/python
# -*- coding: utf-8 -*
import sys
import re

f = open("/home/hduser/pyfile/stopwords.txt")
stopwords = []
for words in f:
    # print(words)
    word = re.sub("\n","",words)
    stopwords.append(word)

# print(stopwords)
for line in sys.stdin:
    string = re.sub("[+\.\!\/_,$%^*(+\"\']+|[+——!,.?`~@#￥%……&*()[\]{}|:-]+","",line)
    word_string = re.sub(r'\d+','',string)
    ss = word_string.strip().split(' ')
    for word in ss:
        word = word.lower()
        if word in stopwords:
            continue
        print('%s\t%s' % (word,1))
