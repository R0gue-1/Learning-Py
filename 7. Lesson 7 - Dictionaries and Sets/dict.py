# Dictionaries => Store data values in key value pairs

band = {
    "vocals": "Plant",
    "guitar": "page",
}

#usign the constructor functions
band2 = dict(vocals='Plant', guitar='Page')
print(band)

print('')

print(band2)

print('')

print(type(band))
print(len(band))

# Access Items
print(band['vocals'])
print(band.get('guitar'))

print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')

# list all keys
print(band.keys())

print('')
 
# list all values
print(band.values())

print('')
 

# list key vlaue pairs as tuples
print(band.items())

# verify if a key exists in a dictionaru
print('guitar' in band)
print('triangle' in band)

print('')
 
#change/replace values
band['vocals'] = 'Coverdale'
band.update({'bass': 'JPJ'})
print(band)

print('')
 
#remove items
print(band.pop('bass')) #when you pop the popped value is returned but not the key
print(band)

print('')
 
band['drums'] = 'Bonham'
print(band)

print(band.popitem()) #removes the last item that was added and returns it as a tuple
print(band)

print('d')
 
#delete or clear items
band["drums"] = 'Bonham'
print(band)

print('')

del band['drums']
print(band)

#empty out a dictional=ry completel
band2.clear()
print(band2)

print('')

del band2




#copying dictionaries

band2 = band #rcreates a reference : means both point to the same plaec in memory

print('Bad copy|!') #don copy like above
print(band2)
print(band)

print('')

band2['drums'] = 'Dave' 

# right cpy style 
band3 =band.copy
band2['dtrums'] = 'Dave'
print('Good Copy style')
print(band)
print(band2)

# or use the band constructor =constructor function
band3 = dict(band)
print("Good Copy!")
print(band3)

# nested dictionaries => the value for key value pairs can be a dictionary

Memeber1 = {
    "name" : "Plant", 
    "Instrument" : "Vocals"
}
Member2 = {
    "name" : "Page", 
    "Instrument" : "guitar"
}
band = {
    "Member1" : Memeber1, 
    "Member2" : Member2
}

print(band)
print(band['Member1']['name'])


# use the dot notation to see all methods associated with any calss/oject