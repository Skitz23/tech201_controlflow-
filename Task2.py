# Write a program that prompts a user for their hours worked and their rate of pay. Calculate their gross pay for the week. Take into account that the business pays them 1.5 times their rate for hours worked over 40.

hrs = input("Enter Hours:")
h = float(hrs)
x1 = input("Enter the Rate:")
x = float(x1)
if h <= 40:
 	print( h  * x)
elif h > 40:
	print(40* x + (h-40)*1.5*x)

# Write a program that asks the user for a number. If the number is odd print "The number is odd!" and if it is even print "The number is even".

num = int(input("Enter any number:"))

if (num % 2) == 0:
    print(f"{num} is an even an number")
else:
    print(f"{num} is an odd number")

# FizzBuzz - Write a program that prints numbers from 1 - 100 but for multiples of 3 print "Fizz" and for multiples of 5 print "Buzz". For multiples of 3 and 5 print "FizzBuzz

def fizzBuzz(s):
    if s % 3 == 0 and s % 5 == 0:
        print("FizzBuzz")
    elif s % 3 == 0:
        print("Fizz")
    elif s % 5 == 0:
        print("Buzz")
    elif s % 3 == 0 and s % 5 == 0:
        print("FizzBuzz")
    else:
        print(s)


for i in range(1, 100):
    fizzBuzz(i)
# Write a program that has a number variable assigned between 1-20. Give the user three guesses to guess the number correctly. Try to give them a clue each time (do they need to go higher or lower?). Make sure to tell them if their guess does not fit in the limitations (1-20).

import random
num = random.randint(1, 20)
Guess = 0
while Guess < 3:
    guess = int(input("Take a guess: "))
    if guess == num:
        print("Your guess was correct")
    elif guess < num:
        print("Wrong, the number is bigger")
        Guess += 1
    elif guess > num:
        print("Wrong, the number is smaller")
        Guess += 1
print(f"Better luck next time, the number was {num}")