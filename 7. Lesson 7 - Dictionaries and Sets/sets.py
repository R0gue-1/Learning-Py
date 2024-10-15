#SETS 
nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums2))
print(len(nums2))

print(type(nums))
print(len(nums))

# sets  do not allow duplicates

nums = {1, 2, 2, 3}

print(nums)

# True is a dupe of 1 and False is a dupe of 0

print('')

nums = {1, True, 2, False, 3, 4, 0}
print(nums)
print('')

#check if a value is iin a set
print(2 in nums)

#but you can not refer to an element in a set with an index positiono or key butyou can check if te value is in the set

#add value to a set

nums.add(8)
print(nums)

# add elements from one set to another
morenums = {5, 6, 7,}
nums.update(morenums)

print(nums)

# you can use update with lists, tuples and dictionaries. You can pass in  lists, tuples and dictionariest o sets and it would work

# merge two sets to create q new set

one = {1, 2, 3}
two = {5, 6, 7}

print('')
mynewset = one.union(two)
print(mynewset)

# keep dups from two sets to make new set

one = {1, 2, 3}
two = {2, 6, 3}
one.intersection_update(two)
print(one)

print('')

# keep everything except dups from two sets to make new set

one = {1, 2, 3}
two = {2, 6, 3}
one.symmetric_difference_update(two)
print(one)

print('')