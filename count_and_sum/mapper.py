#!/usr/bin/python

""" 
INPUT: Transactions of products in multiple stores and location; these can also be passed to STDIN
        Format of each line is: date\ttime\tstore location\titem description\tcost\tmethod of payment

OUTPUT: E.g. 
            Las Vegas       208.97
            Miami   84.11
            Tucson  489.93
            San Francisco   388.3
            Dallas  145.63
            Tampa   353.23
            Washington      481.31
            San Jose        492.8
            Newark  410.37
            Memphis 354.44
            Jersey City     369.07
            Plano   4.65
            Buffalo 337.35
            Louisville      213.64
            Miami   154.64
            ...
"""


import string
import fileinput

for line in fileinput.input():
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, location, item, cost, payment = data
        print "{0}\t{1}".format(location, cost)
