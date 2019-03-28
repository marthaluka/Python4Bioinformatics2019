#!/usr/bin/env python

print("Please enter your DNA sequence: ")
dna = input()
print(dna)

dna.upper()
print(dna)

#GC_content= dna.count('G')+dna.count('C')



trna = 'AAGGGCTTAGCTTAATTAAAGTGGCTGATTTGCGTTCAGTTGATGCAGAGTGGGGTTTTGCAGTCCTTA'
C_count=trna.count('C')
G_count=trna.count('G') 
GC_content= (G_count+C_count)/len(trna)*100
AT_content=100-GC_content
print("The GC content of trna sequence is %.2f %% and the AT content is %.2f %%" %(GC_content, 
                                                                                   AT_content), end='.')