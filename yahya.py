# for loop 1
name = "sadiqa"
for i in name:
    print(i)
# # for loop 2
colours =["red","orange","green","blue","pink","black"]
for colour in colours:
    print(colour)  
    for i in colour:
     print(i)
# #range()
for k in range(5):# 0 to 5
   print(k)
# # 1 to 5
for k in range(5):
    print(k+1)  
for k in range(1,12,3): # 1+3=4, 4+3=7, 7+3=10,
    print(k)    
# while loop 1
i = 0
while(i<3):
    print(i)
    i = i+1
#while loop 2    
i = int(input("Enter your number:"))
while(i<=50):
    print(i)
    i = int(input("Enter your number:"))
print(i)
# while loop 2 (to print 5 to 1)
count = 5
while (count>0):
    print(count)
    count = count - 1
# break and continue
for i in range(12):
    print("5x",i,"=",5*(i+1))
    if(i==10):
        print("left the loop") 
        break
      
#continue
for i in range(12):
    print("5x",i,"=",5*(i+1))
    if(i==10):
        print("skip the altration")
        continue
# geometric mean(function in python)
import math
a=9
b=8
gmean = math.sqrt(a*b) 
print(gmean) 
import math
a = 5
b = 8
def calculategmean(a,b):
    gmean=math.sqrt(a*b)
    print(gmean)
# function apply
    
c = 3
d = 4
calculategmean(c,d)  
# # greater number function
def isgreater (a,b):
    if(a>b):
        print("first number is greater.")
    else:
        print("second number is greater.")  
a = 5
b = 8
isgreater(a,b) 

# pass (we can make function later, it will not show error)
def islesser(a,b):
    pass

def name(fname, lname):
    print("hello", fname, lname)

    name("sadiqa", "bano")
# # default argument

def mean(a=25, b=10):
    print("mean is",(a+b)/2)
# mean()
# kyeword argument(we can give "b" value first then "a" value using key value pair)
# mean(b=15,a=13)

# required argument
#in case we dont pass the argument in key value syntax then it is nessery pass tha argument
# in correct positional order.

# variable length argument
def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
        print("the average is", sum/len(numbers))

        average(5,5,6)   



       

 
    




