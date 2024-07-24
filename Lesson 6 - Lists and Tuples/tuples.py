# tuples => like lists except data does not change and order does not change

#tuples
mytuple = tuple(('Dave',42,True))
anothertuple = (1,4,2,2,2,8)
print(mytuple)
print(type(mytuple))
print(type(anothertuple))

# copynig tuples 
newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

# unpacking tuples
(one, two,*hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))