# Functions => resuable blocks of code

#function definition

# def hello():
#     print('Hello World!')

# function calling

# hello()

#functions must all be lower case and use underscore to show spaces

# def hello_world():
#     print('Hello new world')

# hello_world()

#functiions with parameters

# def sum(num1, num2):
#     print(num1 + num2)

# when using functions with parameter, we parse in arguments
# arguments can change with every functin call

# sum(2,3)
# sum(3,3)
# sum(2,93)
# sum(8,3)

# returning values

# def sum(num1, num2):
#     if (type(num1) is not int or type(num2) is not int):
       # return  exit funtion. does not return nothin.. this is called an early return
    # return num1 + num2

# total = sum(2,9)
# print(total)

# functions with default parameter values
# def sum(num1=0, num2=3):
#     if (type(num1) is not int or type(num2) is not int):
       # return 0  exit funtion. does not return nothin.. this is called an early return / adding zero returns 0 in place of none which is an unexpectec output
#     return num1 + num2

# total = sum(7, 2)
# print(total)

# FUNCTIONS WITH MULTIPLE PARAMETER INPUT

# def multiple_items(*args):
#     print(args)
#     print(type(args))

# multiple_items('Atibils', 'Anyeyure', 'C')
# print('')

# NAMED ARGUEWMENT
def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

mult_named_items(first = 'Atibils', middle = 'Anyeyure', last = 'C')
