# CATCH ANY ERROR
try:
    print(x)
except:
    print('There is an error')

# SPECIFIC ERRORS this wont catch any other error
try:
    print(x)
except NameError:
    print('This means there is an undefined item that has been used')


# handle multiple errors
x = 2
try:
    # print(x / 0)
    if not type(x) is str:
        raise TypeError("Ony strings are allowed")

except NameError:
    print('This means there is an undefined item that has been used')
except ZeroDivisionError:
    print("you cann not divide anything by 0")
except Exception as error: #cathches and raises erros
    print(error)
else:
    print("No errors")
finally:
    print("I am going to print with or without an error")