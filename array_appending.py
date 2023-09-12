print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
from array import *

vals = array('i',(5,6,7))
# im guessing the i tells you its an integer array

print(vals[1])
vals.append(9)
print(vals)
print(vals[3])

vals2 = array('i',())
vals2.append(420)
print(vals2[0])