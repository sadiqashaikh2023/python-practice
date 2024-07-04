### if __name__=="__main": in python  the line if __name__ == "__main__": is used to check
###  whether the current script is being run directly by the Python interpreter,
###  or if it is being imported as a module into another script.

###(import from harry.py when we import file all the content of harry.py
### import 2 time to avoid this we use if __name__=="__main": in harry.py script)

def welcome():
    print("welcome to my home.")

harry = "a good boy"
if __name__=="__main":
    welcome()

print(__name__) #(show __main__ this script run from main file harry.py )  
 
 

#localvariable vs global variable  

x = 10

def myfunctn():
    global x
    x=5
    print(f"local var is {x}")

myfunctn()
print(x)

### file io on python (file mode read,write,append)

f = open("basic7.py","r") #(to read file content (r mode is defulte mode))
print(f)
text = f.read()
print(text)
f.close()

### write mode
f = open("basic8.py","w") #(to write file if file not available automatically "w" make file)
print(f)
text = f.write('Hello, World!\n')
print(text)
f.close()

### append mode
with open("basic8.py","a") as f:
f.write("i am the best") 

### binary mode
with open("basic8.py","rb") as f:
    text=f.read()
print(text)    

### with statement (you can use the with statement to automatically close the file and we can use any mode)
with open("basic8.py","a") as f:
f.write("i am the best") 

### read() and readlines methods in python

f = open('basic8.py','r')
while True:
    line = f.readline()
    print(line) 
    if not line:
      break

f = open('basic8.py','r')
i = 0
while True:
    i = i+1
    line = f.readline()
    if not line:
        break
    m1 = (line.split(",")[0])
    m2 = (line.split(",")[1])
    m3 = (line.split(",")[2])
    print(f"marks of stu {i} in english is: {m1} ")
    print(f"marks of stu {i} in maths is: {m2} ")
    print(f"marks of stu {i} in hindi is: {m3} ")
    print(line)

### writelines() method
### write a sequence of string to a file sequence can be any itrable object, such as list or tuple

f = open('basic8.py','w')
lines = ['line1\n','line2\n','line3\n']
f.writelines(lines)
f.close()

### seek() and tell() function in file io
### the seek function allow you to move the current position within a file
### to a specific point,the position is specified in bytes,and you can move either forword or backword
### from the current position.
with open('basic8.py','r') as f:
    f.seek(10)
    data = f.read(5)
print(data)    

### tell() show position of seek
with open('basic8.py','r') as f:
    f.seek(10)
    print(f.tell())
    data = f.read(5)
print(data) 


### truncate  
with open('basic8.py','w') as f:
    f.write('hello i am good')
    f.truncate(5)

with open('basic8.py','r') as f:    #(reading file)
    print(f.read())
        


