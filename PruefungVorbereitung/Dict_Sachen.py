#Dictionary kreieren und darauf zugreiffen
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])
print(dict)


#Dictionary Elemente ändern oder neue ELemente dazu addieren
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School" # Add new entry

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])

#Dictioary Elemente löschen
del dict['Name'] # remove entry with key 'Name'
print(dict)

dict.clear()     # remove all entries in dict
print(dict)

del dict         # delete entire dictionary
print(dict)

#Laenge eines Dictionaries
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(len(dict))


#list of tuples mit key value pairs
a=dict.items()
print(a)

#durch dict loopen
for key, value in dict.items():
    print(str(key) + " " + str(value) + "; ")

for key in dict.keys():
    print(str(key) + " " + str(dict[key]) + "; ")


#dictionaries addieren
dict2= {'test': 3, 'test1': 7}
dict.update(dict2)
print(dict)

#kopiren von Dictionaries: achtung: nicht dict3=dict!!!!!!
dict3=dict.copy()
print(dict3)

#dictionaries vergleichen
print(dict==dict3)