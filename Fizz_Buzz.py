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