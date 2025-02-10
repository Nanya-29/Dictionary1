#create a dictionary

dict1={
    "name":"Aananya",
    "age":13,
    "Gender":"female"
}

#printing/ accessing values from a dictionary

print(dict1)
print(dict1["name"])
print(dict1["Gender"])

# get all the keys

print(dict1.keys())

#get all the values

print(dict1.values())

#get the list of keys and values

for i in dict1.keys():
    print(i,dict1[i])

#checking if a key exists in dictionary

a=input("Enter the key to be checked: ")
if a in dict1:
    print("key exists")
else:
    print("key does not exist")

# Add a key-value pair in the dictionary

dict1["Profession"]="Scientist"
print(dict1)

# delete a key value pair from a dictionary

del(dict1["Gender"])
print(dict1)

# Changing a value in the dictionary

dict1["Profession"]="Software engineer"
print(dict1)


# store a list as a value

dict1["Marks"]=[95, 97, 100, 98]
print(dict1)

# accessing an item in the list stored in the dictionary
print(dict1["Marks"][1])

# make a nested dictionary

classroom={
    "Izzy":{"age":23,"marks":[98,23,78,34]},
    "Alex":{"age":24,"marks":[67,99,12,24]}
}

# go through basic dictionary operations for nested dictionary

print(classroom.keys())
print(classroom.values())

for i in classroom.keys():
    print(classroom[i])
    
