# # for loop with else
for i in range(5):
    print(i)
else:
    print("not in i") 
   
for i in []: # (else exicute)
    print(i)
else:
    print("no i")    

for i in range(10): #(else not exicute with break)
    print(i)
    if i == 5:
        break
else:
    print("not found")        

i = 0 
while i < 7:
    print(i)
    i = i+1
else:
    print("no i")    

# # else with f string 
for x in range(5):
    print("itration no {} in loop".format(x+1))
else:
    print("in else")
print("out of the loop")        
