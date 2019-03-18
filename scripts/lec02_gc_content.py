#!/Users/user/miniconda2/envs/py3k/bin/python

# The DNA sequence
trna = 'AAGGGCTTAGCTTAATTAAAGTGGCTGATTTGCGTTCAGTTGATGCAGAGTGGGGTTTTGCAGTCCTTA'

#Counting Cs
C_count=trna.count('C')

#Counting Gs
G_count=trna.count('G') 

#GC content
GC_content= (G_count+C_count)/len(trna)*100

#AT content
AT_content=100-GC_content

#Output
print("The GC content of trna sequence is %.2f %% and the AT content is %.2f %%" %(GC_content, 
                                                                                   AT_content))