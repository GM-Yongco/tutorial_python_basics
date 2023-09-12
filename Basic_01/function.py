# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu
# FUNCTIONS ---------------------------------------------------------------------------------------
def add(x, y):
    z = x + y
    return z

def add_wDefault_parameters(x = 68, y = 1):
    print(x + y)

# MAIN --------------------------------------------------------------------------------------------
print("\nSTART ----------------------------------\n")

num1 = int(input("num1 to add to num2: "))
num2 = int(input("num2 to add with num1: "))

print(add(num1, num2))

add_wDefault_parameters()
add_wDefault_parameters(1, 5)

temp_function = add

print(temp_function(399, 21))

print("\nEND ------------------------------------\n")
