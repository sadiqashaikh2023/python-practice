# list are order collection of date items
# list is a collection of data seprated with comma and enclose with square bracket[]
# list are changable
list1=[1,2],[2,2.4],[-4,4],["apple","banana"]
print(list1)
# we can add string in list
l = [3,5,8,"apple","true"]
print(l)
l2 = [4,7,8]
print(l2)
print(type(l2))
print(l2[0]) #indexing start from zero
print(l2[1])

# nagative indaxing
l3 = [34,56,78,"harry","mango"]
print(l3[-3])
print(l3[len(l3)-3])
print(l3[5-3])
print(l3[2])

# check item present in the list
numbers = [2,5,7,5]
if 8 in numbers:
    print("yes")
else:
    print("no")
print(numbers)#to print all the element of list 
print(numbers[:])#to print all the element of list 
print(numbers[1:])
print(numbers[1:-1])#(1:4-1)(1:3)

marks = [2,4,6,7,8,45,3,5,5]
print(marks[1:8:2])#1 start,8 stop(n-1 ),2 step

# list comprehensive
lst = [i*2 for i in range(10) if i%2==0]
print(lst)

names = ["sadiqa","yahya","maryam","rizwan"]
names_with_q = [i for i in names if "q" in i]
print(names_with_q)

items = ["abc","xyzzz","pqrs","pink"]
with_4 = [i for i in items if (len(i)>4)]
print(with_4)

#list method..
price = [12,67,90,10,23,56,12,11,11,90,10]
price.append(60) # to add new value in list
price.sort(reverse=True)# starting from max to min value
price.reverse()# reverse the list
print(price.index(67))#to print index no.
print(price.count(10))# to print how many time 10 in the list
price.insert(1,100)# to print 100 on 1 index no.
print(price)

m = [800,900,600]
price.extend(m) # to merge 2 list 
print(price)
k = price+m # to merge 2 list
print(k)

# tuple is a collection of data seprated with comma and enclose with perenthess this is immutable(can not change)
tuple1=(("apple","banana"),("parrot","sparrow"),("tiger","lion"))
print(tuple1)
# tuple in python
# tubles are unchangable
# we can add string in tuple
tup = (1,5,6,"green",True)
print(type(tup), tup) 
tup_1 = (1,) # to print 1 element in tuple
print(tup_1)
#indexing in tuple
print(tup[0])
print(tup[-1])
print(tup[2])
print(tup[-4:-1])
# condition in tuple
if "green" in tup:
    print("yes is always present.")
# create new tuple using exsiting tuple
tup2 = (tup[0:3]) # create new tuple using exsiting tuple
print(tup2) 
# create tuple using for loop
t = (i for i in range(5))
t_tuple = tuple(t)
print(t_tuple)

#tuple methods
countries = ("india","china","america","uk")
temp = list(countries) #convert tuple in list
temp.pop(3) # remove item
temp.insert(3,"finland") # add item on index no.3
temp.append("russia") #add item last in list
countries = tuple(temp) #convert list to tuple
print(countries)

# solution 2 conversion of tuple to list
food = ("pizza","pasta","sandwitch","biryani","samosa")
temp_food = list(food)
temp_food.pop(2)
temp_food.insert(1,"vada pav")
temp_food.append("sweets")
food = tuple(temp_food)
print(food)

# concate two tuple
country22 = ("abc","xyz","pqr","xyz")
country33 = (1,45,23,45,67,87)
new_country = country22 + country33
print(new_country) 

# count in tuple
tuple_100 = (1,2,5,6,7,2,1,5,9)
res = tuple_100.count(1)
print("total count of 1 is", res)

# index method
# give index no of the element, if element not find raise en error.
no = (12,34,56,78,34,6,90,456,789,56) 
# print(no.index(12))
print(no.index(6,5,8)) # (element,start,stop)
print(len(no)) # to print length of tuple

# f string in python
# 1
letter = ("hay my name is {} i am from {}")
name = "sadiqa"
city = "mumbai"
print(f"my name is {name}, i am from {city}")
# 2
txt = "only only {} dollar"
price = 24.099999
print(f"only only {price:.2f} dollar") # .2f is tak only 2 value after decimal.

# 3 if print as it is use {{}}
txt = "only only {} dollar"
price = 24.099999
print(f"only only {{price:.2f}} dollar") # to print same use {{}}

# to print int as a string using f string
print(f"{2*4}") 
print(type((f"{2*4}")))

# doc string
# python doc string are the string litrals that appear right after the 
# defination of function, method, class, module.
 
 # 1.
def square(n):
    '''thaks in a number n return the square of n'''
    print(n**2)
square(5) 
print(square.__doc__) # to print doc string

# 2.
def average(a,b):
    '''average of two number'''
    print(a+b/2)
average(3,5)   
print(average.__doc__)

# PEP8
# PEP8 is a document that provide guidlines and best practice on how to write python code. it was written in 2001
# guido von russom.PEP8 stands for (python enhancement proposal)
 
# The zen of python
# long time pythoneer tim peters succinctiy channel's the BDFL's guidlines principle for python design
# into 20 aphrosims, only 19 of which have been written down.

# Recursion in python
# recursion is a process of defining something in term of it self.

# 1.
def factorial(num):
    if (num == 1 or num == 0):
      return 1
    else:
        return (num * factorial(num-1))
print(factorial(5))
# 2.  
# def fibonacci_sequence(n):
#     if(n==0):
#         return 0
#     elif(n==1):
#         return 1
#     else:
#         return fibonacci_sequence(n-1) + fibonacci_sequence(n-2)
# y = int(input("enter the number for n:"))
# print(fibonacci_sequence(y))  

# SET IN PYTHON
# sets are unorder collection of data item. they store multiple item in a single variable, set item are seprated by commas
# and enclosed with in curly bracket. sets are unchangable.sets do not contain duplicate items.
 
s = {"sadiqa",23,"iram",True,"zahida","sadiqa"} # duplicate item will not print
print(type(s))
print((s)) 

e = {}
print(type(e)) # (e) type is dict 

# to make empty set
e = set()
print(type(e)) # this is empty set

# to accessing set item.
for i in s:
    print(i)

# sets method

# joining sets (union and update)
s1 = {1,2,4,5,6}
s2 = {6,7,9,3,1,2,4}
# print(s1.union(s2))

# intersection(showing same value in both sets)
cities = {"tokyo","madrid","burlin","delhi"}
cities2 = {"tokyo", "delhi","mumbai","burlin"}
# cities3 = cities.intersection(cities2)
# print(cities3)
# cities.intersection_update(cities2) # cities matching value with cities2 
# print(cities)
# print(cities.symmetric_difference(cities2)) # diffrent value of cities ans cities2
# print(cities.difference(cities2)) # cities value which is not present in cities2 

s1 = {1,2,4,5,6}
s2 = {6,7,9,3,1,2,4}
s1.difference_update(s2)
print(s1) # modify the set s1 by removing element that are also present in s2

# isdisjoint (this method check the intersection is present in the set if their is an intersection show false else true)
name1 = {"rah","atul","atul","shurti","rohan"}
name2 = {"rina","sohan","shurti"}
# print(name1.isdisjoint(name2))

# issuperset
name1 = {"rah","atul","atul","shurti","rohan"}
name2 = {"rah","atul","atul","shurti","rohan","sadiqa","maryem"}
print(name1.issubset(name2)) # ALL the elemant of name1 is present in name2, if yes show true else false 
               
t = {"a","h","c","j","x"} # show true
h = {"a","h","c"}
print(h.issubset(t))

num1 = {12,13,14,15}
num2 = {11,56,13,67}
print(num1.issuperset(num2)) # false

# add (to add single item in a set)
pin_no = {40061,40052,40038}
pin_no.add(40021)
print(pin_no)

# update ( to add more than one item)
pin_no.update(500061,70013) 
print(pin_no)

 



