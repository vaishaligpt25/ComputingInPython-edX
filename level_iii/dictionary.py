#Dictionary = A data structure comprised of key, value pairs where a key is entered into the dictionary to get out a value.
#DIctonary key = A value then, when passed into oa dictionary, returns a corresponding value, like as word and its definition.Similar to variable.
#Dictionary Value= A value returned in response to a key in a dictionary. Similar to a value ofo a variable outside a dictionary
#Creating_and accessing dictionaries-1
my_dictionary = {"sprockets" : 5, "widgets" : 11, "cogs" :3,"gizmos":15}
print(my_dictionary)

print("\n--------1-------\n")
#creating and accessing dictionaries-2
my_dictionary = {"sprockets": 5, "widgets": 11, "cogs" : 3,"gizmos": 15}
my_dictionary["sprockets"] += 1
print(my_dictionary)

print("\n--------2-------\n")
#Adding and removing from dictionary-1
my_dictionary = {"sprockets" : 5, "widgets" : 11, "cogs" : 3, "gizmos" : 15}
print(my_dictionary)
my_dictionary["gadgets"] = 1
print(my_dictionary)
del my_dictionary["gadgets"]
print(my_dictionary)

print("\n--------3-------\n")
#Adding and removing from dictionary-2
my_dictionary = { "David" : "4045551234", "Lucy" : "4045555678", "Vrushali" : "4045559101"}
print(my_dictionary)
#check if "David" is a key in the dictionary
if "David" in my_dictionary:
    print("David is already in the dictionary!")
    my_dictionary["David2"] = "4045551121"
else:
    my_dictionary["David"] = "4045551121"
print(my_dictionary)

print("\n--------3-------\n")
#Adding and removing from dictionary -3
#my_dictionary = { "David" : "4045551234", "Lucy" : "4045555678", "Vrushali" : "4045559101"}
#print(my_dictionary["Dana"])

print("\n--------4-------\n")
#Traversing dictionaries-1
my_dictionary = {"sprockets" : 5, "widgets" : 11, "cogs" :3,"gizmos":15, "gadgets": 1}
for value in my_dictionary.values():
    if value < 5:
        print("A value less than 5 was found:", value)

print("\n--------5-------\n")
#Traversing dictionaries-1
my_dictionary = {"sprockets" : 5, "widgets" : 11, "cogs" :3,"gizmos":15, "gadgets": 1}
for key in my_dictionary.keys():
    value = my_dictionary[key]
    if value < 5:
        print(key,"is less than 5:", value)

