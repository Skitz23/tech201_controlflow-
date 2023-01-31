age = input("What is your age?")

if age.isdigit() and int(age) < 1 and int(age) > 117 :
    print("Enter an age between 1 and 117")
elif age.isdigit() and int(age) >= 1 and int(age) < 10:
    print(f"You are {age}  able to watch universal movies")
elif age.isdigit() and int(age) >= 10 and int(age) < 12:
    print(f"Your are {age} are able to watch universal and pg movies")
elif age.isdigit() and int(age) >= 13 and int(age) < 15:
    print(f"Your are {age} are able to watch universal, pg and 15 rated movies with adult supervision")
elif age.isdigit() and int(age) >= 18 and int(age) < 117:
    print(f"Your are {age} are able to watch universal, pg, 15 rated films and 18 plus")
