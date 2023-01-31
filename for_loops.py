# Looping

# A for loop is where you define an iterator number and cycle through data

# Creating a for loop

list_data = [1, 2, 3, 4, 5, 6]
embedded_lists = [[1, 2, 3] , [4, 5, 6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}

# for num in list_data:
#    print(num * 2)


# nested for loops
# for data in embedded_lists:
#    print(data)
#    for num in data:
#        print(num)

## loops for dictionaries

#for item in dict_data.values():
#    print(item)
#
for item in dict_data.values():
    print(item)
    for embed_value in item.values():
        print(embed_value)

for items in dict_data.values():
    print(items['money'])

# Please see python documentation for more you can do with dictionaries and loops

# Loops and if statements

list_1 = [1, 2, 3, 4, 5]

for num in list_1:
    if num == 3:
        print("I found three!")
    elif num > 3:
        print("Gone too far!")
    else:
        print("Too soon")

