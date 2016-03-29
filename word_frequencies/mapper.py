#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab
""" 
INPUT: File(s) containing words to count; these cn also be passed to STDIN

OUTPUT: E.g.  [('the', 1), ('quick', 1), ('brown', 1), ('fox', 1), ('jumped', 1),
              ('over', 1), ('the', 1), ('lazy', 1), ('grey', 1), ('dogs', 1)]
"""


import string
import fileinput

def remove_punctuation(s):
    return s.translate(string.maketrans("",""), string.punctuation)


words = []
for line in fileinput.input():
    for word in remove_punctuation(line.strip().lower()).split():
        print "{0}\t1".format(word)
