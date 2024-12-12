from os.path import samefile


def addone(aninteger):
   aninteger = aninteger + 1
   print("aninteger:",aninteger)

myinteger = 5
print("myinteger before addone:", myinteger)
# call addone on myinteger
addone(myinteger)
print("myinteger after addone:", myinteger)

print("\n--------1--------\n")

def additem (alist):
    alist.append("New Item!")
    print("alist:", alist)

mylist = ["One", "Two", "Three"]
print("My list before additem:", mylist)
additem(mylist)
print("My list after additem:", mylist)

print("\n---------2-------\n")

my_string = "David"
my_string.upper()
print(my_string)

print("\n--------3--------\n")

my_string = "David"
my_string = my_string.upper()
print(my_string)

print("\n-------4---------\n")

my_list1 = ["one", "two", "three"]
my_list2 = my_list1
my_list1.append("four")
print("my list1:", my_list1)
print("my list2:", my_list1)

print("\n--------5--------\n")

myint1 = 5
myint2 = myint1
myint1 = 7
print("myint1:", myint1)
print("myint2:", myint2)

print("\n--------6--------\n")

my_list1 = ["one", "two", "three"]
my_list2 = my_list1
my_list1.append("four")
print("my list1:", my_list1)
print("my list2:", my_list2)

print("\n--------7--------\n")

myint1 = 5
print(id(myint1))
myint1 = 6
print(id(myint1))

print("\n--------8--------\n")

mylist = ["one", "Two", "Three"]
print(id(mylist))
mylist.append("Four")
print(id(mylist))
mylist = ["Five","Six","Seven"]
print(id(mylist))

print("\n--------9--------\n")

myint1 = 5
myint2 = 5
print(id(myint1) == id(myint2))
#Print true if myint1 & myint2
# point to the same spot in memory

print("\n--------10--------\n")

my_list1 = ["one", "Two", "three"]
my_list2 = ["one", "Two", "three"]
my_list2.append("Four")
print(id(my_list1) == id(my_list2))
my_list2.append("Four")
print(id(my_list1))
print(id(my_list2))
print(my_list1)
print(my_list2)

print("\n-------11---------\n")

my_numeric_string = "12345"
my_non_numeric_string = "ABCDE"
print(my_numeric_string.isdigit())
print(my_non_numeric_string.isdigit())







