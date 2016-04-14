#!/usr/bin/python

""" 
INPUT: Output from mapper.py
        Format of each line is: word\t1

OUTPUT: E.g.
            brown   1
            dogs    1
            fox     1
            grey    1
            jumped  1
            lazy    1
            over    1
            quick   1
            the     2
"""


import fileinput

count = 0
old_word = None

for line in fileinput.input():

    data = line.strip().split("\t")    

    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue

    current_word, increment = data

    # Refresh for new words
    if old_word and old_word != current_word:
        print old_word, "\t", count
        old_word = current_word
        count = 0

    old_word = current_word
    count += int(increment)

if old_word != None:
    print old_word, "\t", count


