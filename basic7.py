#  how import works

import math
a =math.floor(4.23445)
print(a)

import math
a = math.sqrt(9)
print(a)

### from keyword (you ca also import specific function or variables from a module using the from keyword 
### for example to import only the sqrt function from the math module you would write: from math import sqrt)
### you can ailso import multiple function and variables

from math import sqrt,pi
result = sqrt(9)*pi
print(result)  


### import everything
from math import *
result = sqrt(9)
print(result)


### as keyword in python
import math as m
result = m.sqrt(25)
print(result)

from math import sqrt as s
result = s(9)
print(result)

import math as m
result = m.sqrt(9)* m.pi
print(result)


### dir function (we can veiw name of all function and variable define as a module )
import math
print(dir(math))

### import function from harry.py file to basic&.py
from harry import welcome, harry
welcome()
print(harry)

from harry import *
welcome()

### if __name__=="__main":
###  in python  the line if __name__ == "__main__": is used to check
###  whether the current script is being run directly by the Python interpreter,
###  or if it is being imported as a module into another script.

from harry import welcome #(import from harry.py when we import file all the content of harry.py
# import 2 time to avoid this we use if __name__=="__main": in harry.py script)
welcome()




