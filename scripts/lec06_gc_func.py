#!/Users/user/miniconda2/envs/py3k/bin/python
#Write a function percentageGC that calculates the GC content of a DNA sequence
#The function should return the %GC content

mydna = "CAGTGATGATGACGAT"
yourdna = "ACGATCGAGACGTAGTA"
testdna = "ATFRACGATTGHAHYAK"

#define 2 functions but have one function call the other function
#A function to detect invalid DNA sequences
def validSequence(seq):
    valid = ['A','C','T','G']
    isValid=True
    for letter in seq: #CK Your code and Hendrick's are similar, who coied from the other? -2
        if letter not in valid:
            isValid = isValid and False #CK isValid and False not correct or necessary -1
        else:
            isValid = isValid and True ## CK this block is not necessary
    return isValid
#A function to calculate GC content
def percentageGC(dnaseq):
    validSequence(dnaseq)
    if validSequence(dnaseq):
        for base in dnaseq:
            G_count = dnaseq.count ('G')
            C_count = dnaseq.count ('C')
            GC_Sum = G_count + C_count
            return (GC_Sum / len(dnaseq))*100
    else:
        print("This is not a valid DNA sequence")

a= percentageGC(mydna)
b= percentageGC(yourdna)
c= percentageGC(testdna)


print("The GC content of mydna is %.2f" %(a,))
print("The GC content of yourdna is %.2f" %(b,))


