#!/usr/bin/python
# -*- coding: utf-8 -*
from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None
count_dict = {}
for line in sys.stdin:
    # print("line:",line)
    line = line.strip()
    try:
        word, count = line.split('\t', 1)
        count = int(count)
    except ValueError:
        continue
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # print('%s\t%s' % (current_word, current_count))
            count_dict[current_word] = current_count
        current_count = count
        current_word = word
if current_word == word:
    count_dict[current_word] = current_count
    # print('%s\t%s' % (current_word, current_count))
dict_sorted = sorted(count_dict.items(), key=lambda x:x[1], reverse=True)
counter = 1
for item in dict_sorted:
    if counter>200:
        break
    counter+=1
    print('%s\t%s' % (item[0],item[1]))