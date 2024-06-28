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


