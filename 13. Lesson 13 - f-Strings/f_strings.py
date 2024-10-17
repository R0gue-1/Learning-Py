person = "Atibila"
coins = 3

# Older ways of printing strings 
print("\n" + person + " has " + str(coins) + " coins left.")

message = "\n%s has %s coins left." %(person,coins)
print(message)

# Newer ways of printing strings (f-strings)
message = "\n{} has {} coins left.".format(person,coins)
print(message)

# Other things you can do with f-strings
# Using index numbers to say which position of the value is going int he field
message = "\n{1} has {0} coins left.".format(person,coins)
print(message)

# Using place holders and assigning the place holders in the format string
message = "\n{p} has {c} coins left.".format(p = person,c = coins)
print(message)

# Using dictionaries with f-strings
player = {'p':'Anyeyure', 'c':7} 
message = "\n{p} has {c} coins left.".format(**player)
print(message)

#######################################
# f-strings! This is the way.

message = f"\n{person} has {coins} coins left."
print(message)

# another application of f-strings
message = f"\n{person} has {2 * 5} coins left."
print(message)

# use functions
message = f"\n{person.lower()} has {coins} coins left."
print(message)

# use 
message = f"\n{player['p']} has {2 * 5} coins left."
print(message)

###################################33
# You can pass formatting options

num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f} \n")

for num in range(1,11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")

print ("")

for num in range(1,11):
    print(f"{num} divided 4.52 is {num / 4.52:.2%}")