
def addone(aninteger):
   aninteger = aninteger + 1
   print("aninteger:",aninteger)


myinteger = 5
print("myinteger before addone:", myinteger)
# call addone on myinteger
addone(myinteger)
print("myinteger after addone:", myinteger)

print("\n----------------\n")

def additem (alist):
    alist.append("New Item!")
    print("alist:", alist)

mylist = ["One", "Two", "Three"]
print("My list before additem:", mylist)
additem(mylist)
print("My list after additem:", mylist)

my_string = "David"
my_string.upper()
print(my_string)



my_string = "David"
my_string = my_string.upper()
print(my_string)

my_list1 = ["one", "two", "three"]
my_list2 = my_list1
my_list1.append("four")
print("my list1:", my_list1)
print("my list2:", my_list1)

myint1 = 5
myint2 = myint1
myint1 = 7
print("myint1:", myint1)
print("myint2:", myint2)

my_list1 = ["one", "two", "three"]
my_list2 = my_list1
my_list1.append("four")
print("my list1:", my_list1)
print("my list2:", my_list2)






