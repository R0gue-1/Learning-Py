# lists are one of 4 cllection data types that hold values which can be referrenced with a common name
users = ['Atibila', 'Anyeyure', 'Tibsis']
data = ['Atibila', 42, False]
emptylist= []

print('Atibila' in data)
print('Atibila' in emptylist)

print('')

print(users[0])
print(users[-1])

print('')

# printing items in a lils
print(users.index('Tibsis'))
print(users[0:2])
print(users[1:])
print(users[-3:-1])

print('')

# length of items in a list
print(len(data))

users.append('Kingsis')
print(users)

# how to add a second list to an already existing list
users.append('Kingsis')
print(users)

print('')

# must be a list on the right of the operator
users += ['Jason','Baba']

print(users)

print('')

users.extend(['Lucy','Angeline','Emmanuel'])
print(users)

print('')

# users.extend(data)
# print(users)

#insert
users.insert(0, 'Maurice')
print(users)

#insert without losing values
users[2:2] = ['Eddie', 'Alex']
print(users)

#replace values
users[1:3] = ['Robert','JPJ']
print('\n', users)

#slices
# [2:2] => does not replace values
# [1:3] => will replace values

#removing data from lists
 
#remove methods
users.remove('Maurice')
print(users)

print('')

# pop last item from any list, will return popped value
print(users.pop())
print(users)

print('')

#remove specific item from a list
del users[0]
print(users)

print('')

#can be useed to completely delete a list
# del data
data.clear() #empty the list but the list still exists
print(data)

print('')

#sorting lists
users[1:2] = ['dave']
users.sort()
print(users)

print('')

users.sort(key=str.lower)
print(users)
print('')

users.sort(key=str.upper)
print(users)

#number lists
nums = [4,42,78,1,5]
nums.reverse()
print(nums)

print('')

# nums.sort(reverse=True)
# print(nums)

print('')

# globlal sorted function
print(sorted(nums, reverse=True))
print(nums)

print('')


# making list copies of original arraays
numcopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numcopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

#all the above are different but have the same value

print(type(nums))

mylist = list([1, 'Niel', True])
print(mylist)












