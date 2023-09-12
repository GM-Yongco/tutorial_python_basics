print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
from array import *

vals = array('i',(5,6,7))
print(vals[1])
vals.append(9)
print(vals)
print(vals[3])

print("the length of vals is " + str(len(vals)))

i = 0
for i in range (len(vals)):
    print (vals[i])