#   STRING DATA TYPES

# literal assignments
first = 'Anyeyure'
last = 'Atibila'

#checking file types
# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

print('')

# constructor functions
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# concatination
fullname = first + ' ' + last
# print(fullname)

# fullname += " !"
# print(fullname)

# casting a number to a string
decade = str(1980)
# print(type(decade))

statement = 'I like hip hop music from the ' + decade + 's'
# print(statement)

#multiple lines
multiline = ''''
Hello How are you doing

How are you doing.

                    my angel my one and only

'''

# print(multiline)

#escaping special characters 
sentence = 'I\'m all your\'s\tHey!\n\nWhere\'s this at\\located?'

# print(sentence)

#string methods
# print(first)
# print(first.lower())
# print(first.upper())
# print(first)

# print(multiline.title())
# print(multiline.replace('angel', 'dearest'))
# print(multiline)

# print(len(multiline))
# multiline += "                                   "
# multiline = "                " + multiline
# print(len(multiline))

# print(len(multiline.strip()))
# print(len(multiline.lstrip()))
# print(len(multiline.rstrip()))

print('')
# Bulild a menu mini project
title = "menu".upper()
# print(title.center(20, "="))
# print("Coffee".ljust(16, '.') + "$1".rjust(4))
# print("Muffin".ljust(16, '.') + "$2".rjust(4))
# print("Cheesecake".ljust(16, '.') + "$4".rjust(4))

#string index values
# print(first[0])
# print(first[1])
# print(first[2])
# print(first[3])
# print(first[4])
# print(first[5])
# print(first[6])
# print(first[7])

# print(first[-1])

# print(first[0:4])

# some methods return boolean date

# print(first.startswith('A'))
# print(first.endswith('z'))

# boolean data types

myvalue = True
x = bool(False)
# print(type(x))
# print(isinstance(myvalue, bool))

#numeric data types
price = 100
best_price = int(80)
# print(type(price))
# print(isinstance(myvalue, int))

#float types
gpa = 3.28
y = float(1.14)
# print(type(gpa))
# print(isinstance(gpa, float))

#complex type
comp_value = 5+3j
# print(type(comp_value))
# print(comp_value.real)
# print(comp_value.imag)

# built in functions for numbers
# print(abs(gpa))
# print(abs(gpa * -1))
# print(round(gpa))
# print(round(gpa, 1))

import math

# print(math.pi)
# print(math.sqrt(64))
# print(math.ceil(gpa))
# print(math.floor(gpa))

#casting string to number
zipcode = '10001'
zip_value =int(zipcode)
# print(type(zip_value))

# can have an error if you attempt to cast incorrect date
# zip_value = int('New York')

