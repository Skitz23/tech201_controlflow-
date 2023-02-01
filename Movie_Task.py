def How_old(years):
    if years.isdigit() and -1 < int(years) < 117:
        if int(years) < 12:
            return print("You can watch universal or pg films")
        elif 12 <= int(years) < 15:
            return print("You can watch 12 films")
        elif 14 < int(years) < 18:
            return print("You can watch films that are 15")
        else:
            return print("You can watch films that are 18 or above if you show ID")
    else:
        years = input("How old are you? ")
        How_old(years)


years = input("How old are you? ")
How_old(years)
