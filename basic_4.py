# Q:WRITE A PYTHON PROGRAM TO COUNT THE FREQUENCY OF WORDS APPEARING IN A STRING

a = "i love apple and banana and apple is very very tasty and banana is also".split()
d ={}
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)

# Q write a python program to convert two list into a dictonary
l1 = [1,2,3,4]
l2 = ["one","two","three","four"]
result=dict(zip(l1,l2))
print(result)

# convert dictinary to tuple
x = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
for i in x.items():
    print(i)

# Q:FIND MISSING NUMBER IN AN ARRAY IN PYTHON
'''SUMMATION METHOD
n = a[-1] (last num of the list)
sum of n natural num = n*(n+1)//2
missing number = sum of n natural num - total of (a)
'''
n = a[-1]
natural_sum = n*(n+1)//2
sum_a = sum(a)
missing_value = natural_sum - sum_a
print(f"missing num is {missing_value}")

# with for loop
a = [1,2,4,5,7]
x = a[0]
for z in a:
    if x != z:
        print(x)
        x += 1
    x += 1 

# with for loop, if and else  
for i in a:
    if x == i:
        x += 1
    else:
        print(x)
        x +=2

# Find Out Pairs with given sum in an array in python of time complexity
arry = [5,7,4,3,9,8,19,21]
arry.sort()
left = 0
right = len(arry)-1
sum1 = 17
while (left < right):
    if arry[left]+arry[right] < sum1:
        left = left + 1
    elif arry[left]+arry[right]> sum1:
        right = right - 1
    elif arry[left]+arry[right] == sum1:
        print("value of  left and right arry is ",arry[left], "&",arry[right])
        left = left + 1
        right = right - 1   







    




  




    


    
    
    
