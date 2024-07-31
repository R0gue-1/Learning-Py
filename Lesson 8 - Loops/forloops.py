# for loops

# a for loop iterates over a sequence of any item

names = ["Atibila", "Anyeyure", "Aboningayiretibilanyeyure", "Caleb"]

# for x in names:
#     print(x)

# for x in "Aboningayiretibilanyeyure":
#     print(x)

# for x in names:
#     print(x)
#     if x == 'Anyeyure':
#         break
#     print(x)

# for x in names:
#     print(x)
#     if x == 'Anyeyure':
#         continue
#     print(x)

# iterating in ranges
# for x in range(4):
#     print(x)

# for x in range(2, 4): #slice
#     print(x)

# for x in range(2, 101, 5): #count from zero to ninety five and increment by 5
#     print(x)
# else:
#     print('glad that\'s over')

actions = ['codes', 'eats', 'sleeps']
# for name in names:
#     for action in actions:
#         print(name + " " + action + '.')
#     print('')

for action in actions:
    for name in names:
        print(name + " " + action + '.')
    print('')


