#!/usr/bin/env python 

#Calculate GC percentage 
mydna = "CAGTGATGATGACGAT"
yourdna = "ACGATCGAGACGTAGTA"
testdna = "ATFRACGATTGHAHYAK"

def Percent(sequence):
G_count = sequence.count ('G')
C_count = sequence.count ('C')
Total_count = len(sequence)
GC_Sum = int(G_count) + int(C_count)
Percent_GC = (GC_Sum / Total_count)*100
return Percent_GC
