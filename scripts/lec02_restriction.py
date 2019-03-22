#!/Users/user/miniconda2/envs/py3k/bin/python

#DNA sequence
dna='AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA'

#Restriction site assigned r_site
r_site='TCCGGA'

#output
print("The first restriction site in the DNA sequence begins at index", 
      dna.find('TCCGGA'),"and is %d nucleotides long" %len('TCCGGA'),sep=' ', end='.')

      #CK: New line not printed, and the last position of the RE site could be useful -1