from itertools import count

my_string = "'12345'"
print(my_string)
my_string = '"abcde"'
print(my_string)

my_string = '''"'12345'"'''
print(my_string)
print("Hello\nWorld")

print("\n-------1--------\n")

#my_string = "'"Hello,world!"'"
print(my_string)#

print("\n--------2--------\n")

my_string_with_new_line = "12345\n67890"
print(my_string_with_new_line)


print("\n--------3--------\n")
# \n (it is a new line character)
my_string = "12345\n67890\tabcde\"fghijklm\\no"
print(my_string)

print("\n--------4--------\n")

my_string = '''12345
67890'''
print(my_string)

print("\n--------5--------\n")
# String concatenation
my_string1 = "12345"
my_string2 = "67890"
my_string = my_string1 + my_string2
print(my_string)
print("Assignment Concatenation: " + my_string)
print("Assignment Concatenation:" + my_string1 +my_string2)
my_string1 += my_string2
print("self Assignment Concatenation:" + my_string1)

print("\n------------------\n")
my_string1 = "12345\n"
my_string2 = "67890"
print(my_string1)
print(my_string2)
print("In line concatenation :" +my_string1 + my_string2)

print("\n--------6--------\n")
#String slicing
my_string = "ABCDE"
print(my_string[0])
print(my_string[2])

print("\n--------7--------\n")

my_string = "ABCDE"
my_substring = ""
#run a loop for each character in my_string
for character in my_string:
    #add character i to my_string
  my_substring += character
print("my_substring:" + my_substring)

print("\n--------8--------\n")

my_string = "ABCDE"
my_substring = ""
#run a loop from i=0 to i=2
for i in range (0,3):
# add character i to my string
 my_substring += my_string[i]
print("First three characters:" + my_substring )

print("\n--------9--------\n")

my_string = "ABCDE"
start = 0
end = 3
print("first three characters:" + \
      my_string [start:end])

print("\n--------10--------\n")
my_string = "ABCDE"
print("first three characters:" + my_string[0:3])
print("characters 1 through 3:" + my_string[1:4])
# 4-1 = 3

print("\n--------11--------\n")

my_string = "ABCDE"
print("first three characters:" + \
      my_string[:3])
print("characters from 3 to end:" +\
my_string[3:])
print("characters from 3 to 10:" + \
my_string[3:10])

print("\n--------12--------\n")

#Negative indices
my_string ="ABCDE"
print("Last two characters:" +\
      my_string[len(my_string)-2:])
# 5-2 = 3
#start with 3rd indices

print("\n--------13--------\n")

my_string ="ABCDE"
print("All but the last two character:" +my_string[:-2])
# 5-2 =3 then start with 2   range(0,3)
print("last two characters:" + my_string[-2:])
# 5-2 =3 then start with 3   range(3,)

print("\n--------14--------\n")

my_string = "ABCDE"
if "BC" in my_string:
    print("BC was found!")
else:
    print("BC was not found!")

print("\n--------15--------\n")

#the find method -1
my_string = "ABCDE"
print(my_string.find("CDE"))
print(my_string.find("ACE"))


print("\n----------16------------\n")
#the find method -2
#check if search string in check string
def checkinstring(checkstring,searchstring):
    if checkstring.find(searchstring)>=0:
        print(searchstring+" was found!")
    else:
        print(searchstring+" was not found!")

#Ex-
my_string = "ABCDE"
checkinstring(my_string,"BC")
checkinstring(my_string,"EF")

print("\n----------17------------\n")
#the find method -3
#print the index in string
my_string = "ABCDEABCDE"
print(my_string.find("CDE"))
print(my_string.find("cde"))

print("\n----------18------------\n")
#parameter of the find method
my_string = "ABCDEABCDEABCDEFGHIJFGHIJABCDEABCDEFGHIJ"
findstring = "CDE"
print(my_string.find("CDE"))
#print the first index of "CDE" in my_string after 5
print(my_string.find("CDE",5))
print(my_string.find("CDE",13))
print(my_string.find("CDE",4 , 10))
print(my_string.find("CDE",3 , 6))

print("\n------------\n")
print("count of", findstring, ":", my_string.count(findstring) )


