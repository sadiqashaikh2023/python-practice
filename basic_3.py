
# Q:method:1 WRITE A PROGRAM TO FIND COMMON LETTERS BETWEEN TWO STRINGS.
def common_letters():
    name1 = input("enter first name:")
    name2 = input("enter second name:")
    str1 = set(name1)
    str2 = set(name2)
    lst = str1 & str2
    return(lst)  
print(common_letters())  

# # method 2
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

# # with while loop

s = input("enter your name:")
output = ""
i = len(s)-1
while i >=0:
    output = output+s[i]
    i = i-1
print(output)

# # with for loop

x = input("enter your name:")
output = ""
for i in range(len(x)-1,-1,-1): #(start,stop,step)
    output = output+x[i]
print(output)

# # Q:write a program to reverse order of word presnt in given string

# a = "python is very easy language"
# l = a.split()
# l1 = l[::-1]
# b = ' '.join(l1)
# print(b)

a = "my name is sadiqa"
b = a.split()
a1 = reversed(b)
r = ' '.join(a1) 
print(r) 

s = "i love python"
x = s.split()
output = []
i = len(x)-1
while i >= 0:
    output.append(x[i])
    i = i-1
print(' '.join(output))          

# Q: write a program to reverse internal content of each word

s = "i am from mumbai"
l = s.split()
e = []
for word in l:
    e.append(word[::-1])
    l1 = ' '.join(e)
print(l1)

# Q: write a program to reverse internal content of every second word of given string
# output should be like("one owt three ruof five xis")
# even num indax same odd number index reverse
     

# Q: write a program to print the charecters present at odd numbers and even numbers

s = "sadiqashaikh"
i = 0
print("character at even num is:")
while i < len(s):
    print(s[i])
    i = i+2
i = 1
print("character at even num is:")
while i < len(s):
    print(s[i])
    i = i + 2

# Q:Wrt a prog to merge characters of 2 strings into a single string by taking characters alternativly
# ex:"sadiqa","maryam" output = smaardyiaqma
a = "ravi"
b = "teja"
output = ''
i,j = 0,0
while len(a)<0 or len(b)<0:
    output = output+(a[i])+(b[j])
print(output)

# Q: Program to sort characters of the string, first alphabet symbols followed by digits
# output = ABDG1378 
x = "BA1D3G78"
strg = []
num = []
for ch in x:
    if ch.isalpha():
        strg.append(ch)
    else:
        num.append(ch)
l = ''.join(sorted(strg)+sorted(num)) 
print(l)       

# Q:Program for the requirement,input: a4b3c2 and expected output: aaaabbbcc

a = "a4b3c2"
output = ''
for ch in a:
    if ch.isalpha():
        x=ch
    else:
        b=int(ch)
        output+=x*b
print(output)

# output should be hh4444b
a = "2h4j1b"
output = ''
count = 0
for ch in a:
    if ch.isdigit():
        count = int(ch)
    else:
        output= output+ch*count
print(output)