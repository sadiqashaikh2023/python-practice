# enumerate function in python
marks = [12,45,98,14,78,8,9]
for index,mark in enumerate(marks):
    print(mark)
    if (index == 3):
        print("sadiqa is awsome!")  

fruits = ["apple","mango","banana","orange"]
for index, fruit in enumerate(fruits):
    print(index,fruit)  


# name = "sadiqa"
# for index, alphabet in enumerate(name):
#     print(index,alphabet)     

# changing the start index
name = "sadiqa"
for index, alphabet in enumerate(name,start=1):
    print(index,alphabet) 