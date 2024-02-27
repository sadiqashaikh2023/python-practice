print("hello world,1")
#this is single line comment
''' this is
multi line comment''' 
print("first line \nsecond line")
print("this is \"python\"")
print("hay",1,2,sep="~",end="007\n")
print("hello")
#variable and data types
a=1
a1=123
b="sadiqa"
c=True
d=None
e=complex(5,4)
f=2.2
#printin data types
print(a+a1)
print("type of a is", type(a))
print("type of a is", type(b))
print("type of a is", type(c))
print(e)
print(type(f))
# list is a collection of data seprated with comma and enclose with perenthess
list1=[1,2],[2,2.4],[-4,4],["apple","banana"]
print(list1)
# tuple is a collection of data seprated with comma and enclose with perenthess this is immutable(can not change)
tuple1=(("apple","banana"),("parrot","sparrow"),("tiger","lion"))
print(tuple1)
# mapped data:dict 
# dict is a collection of key value pair
dict1 = {"id":1,"name":"sadiqa","age":30,"canvote":"true"}
print(dict1)
#oprators
print(5+5)#addition oprator
print(5-3)#substraction
print(5/3)#division
print(5//3)#floor division
print(5*5)#multiplication
print(5**3)#exponential
print(5%3)#modulus
a=20 #calculator using two numbers
b=30
print("the value of", a, "+", b, "is:", a+b)
print("the value of", a, "-", b, "is:", a-b)
print("the value of", a, "*", b, "is:", a*b)
print("the value of", a, "/", b, "is:", a/b)
# typecasting in python
#conversion of one data type into another data type
a="1"
b="4"
print(int(a)+int(b))
#implicit typecasting
c=1.8 # automatically convert c to float
print(type(c))
d=8 # automatically covert d to int
print(type(d))
e=c+d # automatically convert e to float
print(e)
print(type(e))
# user input
a = input("enter your name:")
print("my name is", a)
x=input("enter first number:")
y=input("enter second number:")
print(int(x)+int(y))
a = input("Enter first number:")
b = input("Enter second number:")
print(int(a) * int(b))
# string in python
name = "rohan"
print("hello, "+ name)
apple = "he said, \"i want to eat an apple"
print(apple)
banana = 'he said, "i want to eat an banana'
print(banana)
# #multi line string
mango = '''he said, 
hi i am good
i want to eat mango'''
print(mango)
#INDAX START FROM 0
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print("lets use a for loop\n")
for character in mango:
    print(character)
name = "yahya,maryam"
print(name[0:4])
#length of string
print(len(name))
fruit = "mango"
print("mango is", len(fruit), "letter word")
#string slicing
print(fruit[0:3])
print(fruit[:3])
print(fruit[1:3])#including 0 not 3
print(fruit[:]) # show full string
print(fruit[0:-3]) # 5-3=2, mango-3=ma
print(fruit[-1:-3]) #5-1=4,5-3=2(4:2)nothing will show
print(fruit[-3:-1])#5-3=2,5-1=4(2:4) including 0 but not 4
nm="harry"
print(nm[-4:-2]) #5-4=1,5-2=3(1:3)inclugin 0 not 3
# strings are immutable
# rstrip(remove any trailing(!) character)
nm="yahya!!!"
print(nm.rstrip("!"))
nm="!!!yahya!!!!!" # will not remove starting (!)
print(nm.rstrip("!"))
#replace() method replace all occurance of string with another srting
name="!!!!!sadiqa!!!!!!sadiqa!!"
print(nm.replace("sadiqa","yahya"))
# split() method split the give string at the specified instance and retuns the seprated string as yhe list item
x= "i am the best"
print(x.split())
# first letter capitalize
blogheading = "introduction to js"
print(blogheading.capitalize())
blogheading = "introduction tO Js"#first upper and rest lower
print(blogheading.capitalize())
# center() method aligns the string to the centre as per the parameters given by the user
str1 = "welcome to the console!"
print(str1.center(50))
# count() numbers of times the given value has occured with in the given string
print(name.count("sadiqa"))
# endswith() method checks if the string ends with a given value.if yes retuns yes else retuns false
print(name.endswith("!!"))
print(str1.endswith("to",4,10))
#find() retuns the first occurence of given value retunce index if not found retuns -1
print(str1.find("to"))
# index method search for first occurence of given value and retuns the where it is present. if given value absent then rais an exception
print(str1.index("tohh"))
# isalpha() A-Z,a-z,0-9 if present retuns true else false
a="sadiqa"
print(a.isalpha())
# islower() retuns true or false
print(a.islower())
# #isprintable 
print(a.isprintable()) #true
# b="welcome to the world\n"
print(b.isprintable()) #false
# isspace() wide space using space bar or tab button show true else false
name="      "
print(name.isspace())
# istittle(if the first letter of the string is capitalize then true else false)
name1="My Name Is Sadiqa"
print(name1.istitle()) 
# #startswith
x = "python is a language"
print(x.startswith("python"))
#swapcase() change lowwer to upper and upper to lower
print(x.swapcase())
#conditional operators
# < , > , <= , >= , == , !=
a=(int(input("enter your age: ")))
print("your age is", a)
print(a>18)
print(a<18)
print(a>=18)
print(a<=18)
print(a==18)
print(a!=18)
# if else 1 in python
a = int(input("Enter your age:"))
print("your age is", a)
if (a>18):
    print("you can drive.")
else:
    print("you can not drive.")
#if else 2
appleprice=210
budget=200
if(appleprice<=budget):
    print("alexa, add 1kg apple to the cart.")
else:
    print("alexa, do not add apple to the cart.")
# if else elif
    a=int(input("Enter the value of num: "))
    if(a<0):
        print("number is negative.")
    elif(a==0):
        print("number is zero.")
    elif(a==999):
        print("number is special.")    
    else:
        print("number is positive.") 
    print("i am happy now")           
# nested if statement
num = 18
if(num < 0):
    print("number is negative")
elif(num > 0):
    if (num <= 10):
        print("number is 1 to 10.")
    elif (num > 10 and num <= 20):
        print("number is between 11 to 20.")
    else:
        print("number is greater than 20.") 
else:
    print("number is zero.")
#date and time module
import datetime

current_datetime = datetime.datetime.now()#curnt date and time
print(current_datetime)
year = current_datetime.strftime("%Y")# capital Y for current year
print("YEAR", year)
month = current_datetime.strftime("%B")# capital B for current month
print("MONTH", month)
minute = current_datetime.strftime("%M")# capital M for current minute
print("Minute", minute)               
sec = current_datetime.strftime("%S")# capital S for current sec
print("sec", sec) 
hours = current_datetime.strftime("%H")# capital H for current HOURS
print("HOURS", hours)
#creating date object
x = datetime.datetime.now() 
print(x)
print(datetime.datetime(2024,1,1)) 
#accoring to the time print good morning, good afternoon and good evening ang good night
import time
current_time = time.strftime("%H:%M:%S")
print(current_time)
hrs = int(time.strftime("%H"))
print(hrs) 
min = int(time.strftime("%M"))
print(min)
sec = int(time.strftime("%S"))
print(sec)
a = input("enter your name:")
if(hrs >= 4 and hrs < 12):
    print("good morning.", a)
elif(hrs >=12 and hrs < 17):  
    print("good afternoon", a)
elif(hrs >= 17 and hrs < 21):
    print("good evening", a)
else:
    print("good night", a)





      









