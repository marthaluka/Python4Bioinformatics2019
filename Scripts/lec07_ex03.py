#!/usr/bin/python

import sys


def validSequence(infile):
    valid = ['A','C','T','G']
    isValid=True
    for letter in infile:
        if letter not in valid:
            isValid = False
            print("This DNA file contains non-convetional bases")
    return isValid


infile = sys.argv[1] 
validSequence(infile)