#!/Users/user/miniconda2/envs/py3k/bin/python

print("Question 1 begins here") 
#question1
#a while loop that starts with x = 0 and increments x until x is equal to 5
x = 0
while x <=5 :
    print(x)
    x+=1
   
print("This is the end of Question 1 \n Question 2 begins here") 
#question2
#repeat that the loop will skip printing x = 5 to the console but will print values of x from 6 to 10.

x = 0
while x <= 10 :
    print(x)
    x+=1
    if x==5 :
        print("We skip this")
        x+=1

#question3
#for loop that prints values from 4 to 10 to the console.

print("This is the end of Question 2 \n Question 3 begins here") 
for x in range(4,11):
    print (x)