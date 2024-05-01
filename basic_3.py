
# Q:method:1 WRITE A PROGRAM TO FIND COMMON LETTERS BETWEEN TWO STRINGS.
def common_letters():
    name1 = input("enter first name:")
    name2 = input("enter second name:")
    str1 = set(name1)
    str2 = set(name2)
    lst = str1 & str2
    return(lst)  
print(common_letters())  

# method 2
def common_letter(name1,name2):
    common_letter = []
    for i in name1:
        if i in name2:
            common_letter.append(i)
            new_common = set(common_letter)
    return(new_common)
print(common_letter("reene","naina"))   

# Q: write a program to reverse content of the given string by using slice oprator.

a = "sadiqa"
print(a[::-1])

# with reveresd object

b = "maryem"
r = reversed(b)
print(''.join(r))

# with while loop

s = input("enter your name:")
output = ""
i = len(s)-1
while i >=0:
    output = output+s[i]
    i = i-1
print(output)

# with fr loop

x = input("enter your name:")
output = ""
for i in range(len(x)-1,-1,-1): #(start,stop,step)
    output = output+x[i]
print(output)
     

    
