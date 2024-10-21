squared = lambda num : num * num

print(squared(2))
print("")

addTwo = lambda num : 2 + num

print(addTwo(12))
print("")

sum_total = lambda a, b : a + b

print(sum_total(10,8))
print("")

#########################################

def funcBuilder(x):
    return lambda num : num + x
    
addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print("")

print(addTwenty(7))

##########################################
# Higher Order Functions map()

numbers = [3, 7, 12, 18, 20, 21]

squared_nums = map(lambda num : num * num, numbers)

print(list(squared_nums))
print("")

##########################################
# Higher Order Functions filter()

odd_nums = filter(lambda num: num % 2 != 0, numbers)

print(list(odd_nums))
print("")

##########################################
# Higher Order Functions reducce()
from functools import reduce



numbers = [1,2,3,4,5,1]
total = reduce(lambda acc, curr : acc + curr, numbers, 10)

print(total)
print("")

# a more efficient way tho 

print(sum(numbers, 10))
print("")

#  MORE COMPLEX APPLICATION



names = ['Atibs Tibsis','Sara Ito','John Jacob']
char_count = reduce(lambda acc, curr : acc + len(curr), names, 0)

print(char_count)