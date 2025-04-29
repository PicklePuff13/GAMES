#creating dictionary
Pickle={"Name":"person","Age":11,"Hobby":"Art","Age":56}
print(Pickle["Hobby"])
print(Pickle)

#length of dictionary
print(len(Pickle))

#adding new item to dictionary
Pickle["Colour"]="Green"
print(Pickle)

#accesing items
print(Pickle["Hobby"])
print(Pickle["Age"])

#modifying existing item
Pickle["Name"]="Eva"
print(Pickle)

#removing an item
del Pickle["Hobby"]
print(Pickle)

#dictionary methods
print (Pickle.values())
print (Pickle.keys())
