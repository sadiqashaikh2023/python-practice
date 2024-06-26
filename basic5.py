# Exception handiling in python

# (if we enter string show error )
try:
    a = int(input("enter your number:"))
    print(f"multiplication table of {a} is")
    for i in range(1,11):
        print(f"{a} x {i} = {a*i}")
except:
   print("invalid input")
print("some important lines")    
print("shoud be print") 
 
# value error
try:
    a = int(input("enter an integer:"))
except ValueError:
    print("number entered is not an integer")

# index error
try:
    num = int(input("enter index number:"))
    a = [45,78,67,89]
    print(a[num])
except IndexError:
    print("index error!!!")

# finally keyword (finally will alway print but if we are making def functn and we not use finally after except code will not excecute )
def func1():
    try:
        l = [12,56,59,51,76,89]
        i = int(input("enter num:"))
        print(l[i])
    except:
        print("some error occurred")
    finally:
        print("i am always executed")    

func1() #(to call a funtion) 

# raising custom error
a = int(input("enter any number between 5 to 10:"))
print(a)
if (a<5) or (a>10):
    raise ValueError ("value should be ")

 # short hand if else
a = 122
b = 189
print("A") if a>b else print("=") if a==b else print("B")    
c = 9 if a>b else 0
print(c)
