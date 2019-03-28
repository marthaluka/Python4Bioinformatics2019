#! /usr/bin/python

#I am generating a module
#opening a file
def readFile (filename):
    openFile = open(filename, 'r')
    return openFile


#generating a genelist
def geneList (openFile):
   for line in openFile:
        tag=False
        if line.startswith('_______'):
            tag=True
        if line.startswith('-'):
            tag=False
        if tag:
            lineList=line.split()
            if len (lineList)>0:
                print(lineList[0])
           
                    

#writing gene list to a new file
#def writeGeneList(filename):




openFile = readFile ("../Data/humchrx.txt")
listGene = geneList(openFile)


    