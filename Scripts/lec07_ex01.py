#!/usr/bin/python

import sys

def readAndWrite(infile, outfile):
    """
    Function to extract a list of genes and write to file
    """
    with open(infile, "r") as f:
        with open(outfile, "w") as f1:
            tag=False
            for line in f:
                if line.startswith('_______'):
                    tag=True
                if line.startswith('-'):
                    tag=False
                if tag:
                    lineList=line.split()        
                    if len (lineList)>0:         
                        f1.write('%s\n' %lineList[0]) 
                    


infile = sys.argv[1] 
outfile = sys.argv[2] 
readAndWrite(infile,outfile)
            

