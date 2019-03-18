#!/Users/user/miniconda2/envs/py3k/bin/python

#Creating a dictionary with complemnetary bases
d = { 'T':'A', 'A':'T', 'G':'C', 'C':'G'}

#DNA sequence assigned my_seq. It is a string
my_seq = 'AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA'

#Generating a list since it is more mutable (To generate a complement)
var = list(my_seq)

#Generating a reverse sequence
var.reverse()

#Applying the dictionary to generate a complement of the reverse. Now we have a reverse complement
var3 = [d[m] for m in var]

#We need our string variable back
rev_complement = "".join(var3)

#Output
print(rev_complement)