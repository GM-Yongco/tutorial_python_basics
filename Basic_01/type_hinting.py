# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu
# HEADER ------------------------------------------------------------------------------------------

def add_concat(x:int | str , y:int | str)->(int|str):
    # these are called union operators me thinks
    # only works python 3.10 above
    return x + y

def only_multiply(x:int , y:int )->int:
    return x*y*69

# MAIN --------------------------------------------------------------------------------------------
print("\nSTART ----------------------------------\n")

print(add_concat(6, 9), add_concat("yes", "no"))
print(only_multiply(7, 2))
# only gives warning
# but mostly for good practice
# it also makes documentation easier

print("\nEND ------------------------------------\n")