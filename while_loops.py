# While Loops

# While loops monitor data rather than iterate

x = 0

# while x < 10:
#    print(f"it's working -> {x}")
#    x += 1 # incrementer

# using break

#while x < 10:
#    print(f"it's working -> {x}")
#    if x == 4:
#        break
#    x += 1

#print(x) # x = 4

# verify user input

# Asking for someone's age
# This can either be an int (20) or a string (twenty)
# age = input("What is your age?")
#
# print(f"your age is {age} ")

user_prompt = True

while user_prompt:
    age = input("What is your age?")
    if age.isdigit() and int(age) < 117:
        user_prompt = False
    else:
        print("Please provide your answer in digits")

print(f"Your age is {age}")