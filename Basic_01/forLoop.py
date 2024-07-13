count = 0

for number in range(1, 10):
    if number % 2 == 0:
        count = count+1
        print(number)
print(f'there are {count} even numbers between 1 and 10')
# ---
s = 'bitch'
print(s)
# ---x
for number0 in range(1, 10 + 1, 2):
    print("Attempt", number0, (number0 + 1 - 1) * ".")
# ---
successful = False
number0 = 0
for number0 in range(1,10 + 1):
    print("Attempt", number0)
    if successful:
        print("Successful")
        break
else:
    print("unsuccessful")
    # else statement after a for statement executes when the for statement completes wihtout an early termination
    # basically if a for loop executes naturally
    # this is seen when the boolean 'successful' is turned false


messages:list = ["kill me", "no dont do it", "why not", "you have so much to live for", "thats what they all say", "..."]
for index, message in enumerate(messages):
    print(f"{index:3} : {message}")