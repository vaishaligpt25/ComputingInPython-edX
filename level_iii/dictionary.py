#Dictionary = A data structure comprised of key, value pairs where a key is entered into the dictionary to get out a value.
#DIctonary key = A key then, when passed into o dictionary, returns a corresponding value, like as word and its definition.Similar to variable.
#Dictionary Value= A value returned in response to a key in a dictionary. Similar to a value of a variable outside a dictionary

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

print("\n--------4-------\n")
#Adding and removing from dictionary -3
#my_dictionary = { "David" : "4045551234", "Lucy" : "4045555678", "Vrushali" : "4045559101"}
#print(my_dictionary["Dana"])

print("\n--------5-------\n")
#Traversing dictionaries-1
my_dictionary = {"sprockets" : 5, "widgets" : 11, "cogs" :3,"gizmos":15, "gadgets": 1}
for value in my_dictionary.values():
    if value < 5:
        print("A value less than 5 was found:", value)

print("\n--------6-------\n")
#Traversing dictionaries-1
my_dictionary = {"sprockets" : 5, "widgets" : 11, "cogs" :3,"gizmos":15, "gadgets": 1}
for key in my_dictionary.keys():
    value = my_dictionary[key]
    if value < 5:
        print(key,"is less than 5:", value)

print("\n--------7-------\n")

#Examples of dictionary-1
my_string = "This is the string whose words we would like to count. This string contains some repeated words, as well as some unique words. It contains punctuation, and it contains words that are capitalized in different ways. If the method we write runs correctly,it will count 4 instances of the word 'it'. 3 instances of the word 'this', and 3 instances of the word 'count'."

my_string = my_string.replace(".","")#remove periods
my_string = my_string.replace(",","")#remove commas
my_string = my_string.replace("'","")#remove apostrphes
my_string = my_string.lower()#make all lower case
my_split_string = my_string.split()# split by spaces
word_dictionary = {}#create empty dictionary
for word in my_split_string: #for each word in the split spring
    if word in word_dictionary:
        word_dictionary[word] += 1
    else:
        word_dictionary[word] = 1
print(word_dictionary)

print("\n--------8-------\n")
#Examples of dictionary-2
seating_chart = {"David" : 3, "Lucky" : 3, "Dana" : 2,"Addision" : 2,"Vrushali" : 1, "Bilbo" : 3,
                 "Sara" : 1, "Lugos" : 1, "Mireia" : 1,"Partha" : 2, "Venijamain" : 1, "Terra" :2, "Tryphon" : 3,"Gevorg" : 1,"Raza" : 3,"Rein" : 3, "Sofia" :2, "Perle" :2}
#for each name , table pair in the seating chart
for (name , table) in seating_chart.items():
    #print the table for the name
    print(name,"is seated at table#", table,sep="")
print()

print("\n--------9-------\n")

#for each table number
for i in range(1,4):
    print("The guests at table #",i , " are: ", sep = "", end = "" )
    #for each name table pair
    for (name, table) in seating_chart.items():
        #if the table number is this number
        if i == table:
          print(name,end="")
    print()
