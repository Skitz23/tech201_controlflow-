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