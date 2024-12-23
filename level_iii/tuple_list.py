my_tuple = (1,2,3)
print(my_tuple)

print("\n------1-------\n")

my_int1 = 1
my_int2 = 2
my_int3 = 3
my_tuple =my_int1,my_int2,my_int3
print(my_tuple)

print("\n------2-------\n")

my_str = "Hello,world!"
my_int = 2
my_float = 3.4
my_tuple = my_str , my_int , my_float
print(my_tuple)

print("\n------3-------\n")
my_str = "Hello,world!"
my_int = 2
my_float = 3.4
my_tuple = my_str , my_int , my_float
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])

print("\n------4-------\n")

my_str = "Hello,world!"
my_float = 5.1
my_int1 = 5
my_character = "Q"
my_int2 = -1
my_tuple = (my_str,my_float,my_int1,my_character,my_int2)
#print value from 4 to end
print(my_tuple[3:])
#print first two value
print(my_tuple[:2])
#print second and third value
print(my_tuple[1:3])
#print last three value
print(my_tuple[-3:])
#print all but the last three value of tuple
print(my_tuple[:-3])

print("\n------5-------\n")

my_str = "Hello,world!"
my_float = 5.1
my_int1 = 5
my_character = "Q"
my_int2 = -1
my_tuple = (my_str,my_float,my_int1,my_character,my_int2)
(my_new_str,my_new_float,my_new_int1,my_new_character,my_new_int2) = my_tuple

print(my_new_str)
print(my_new_character)
print(my_new_float)
print(my_new_int1)
print(my_new_int2)

print("\n------6-------\n")

#usefulness_of_tuple-1
# return the tuple containing quotient and remainder
def quotientandremainder(dividend, divisor):
  #get the quotient
  quotient = dividend //divisor
  #get the remainder
  remainder = dividend % divisor
  # return the tuple of the quotient and remainder
  return (quotient , remainder)

my_dividend = 11
my_divisor = 4
tuple_result = quotientandremainder(my_dividend , my_divisor)
# print the first result of tuple
print("Quotient:", tuple_result[0])
print("Remainder:", tuple_result[1])

print("\n------7-------\n")

#usefulness_of_tuple-2
# return the tuple containing quotient and remainder
def quotientandremainder(dividend, divisor):
 #return the tuple of the quotient and remainder
  return (dividend // divisor , dividend % divisor)

my_dividend =11
my_divisor = 4
#assigm the first value of the result to my_quotient and second to my_remainder
(my_quotient, my_remainder) = quotientandremainder(my_dividend ,my_divisor)
print("Quotient:", my_quotient)
print("Remainder:",my_remainder)

print("\n------8-------\n")

#Nesting tuple
my_tuple1 =(1,2,3)
my_tuple2 = (4,5,6)
my_tuple3 = (7,8,9)
my_super_tuple = (my_tuple1,my_tuple2,my_tuple3)
print(my_super_tuple)

print("\n------9-------\n")

my_super_tuple = ((1,2,3),(4,5,6),(7,8,9))
print(my_super_tuple)

print("\n------10-------\n")

my_tuple1 =(1,2,3)
my_tuple2 = (4,5,6)
my_tuple3 = (7,8,9)
my_super_tuple = (my_tuple1,my_tuple2,my_tuple3)
#print the first item of the second tuple
print(my_super_tuple[1][0])
# print the second item of the third tuple
print(my_super_tuple[2][1])
print(my_super_tuple[2])


print("\n------11-------\n")
#list arw mutable means items can be add and remove
#nearly everything we did with tuples , we can do with lists

#list as tuple -1
my_list1 = [1,2,3]
print(my_list1)
print()
my_int1 = 1
my_int2 = 2
my_int3 = 3
my_list2 = [my_int1,my_int2,my_int3]
print(my_list2)
print()

my_str = "Hello,world!"
my_float = 5.1
my_int1 = 5
my_character = "Q"
my_int2 = -1
my_list3 = [my_str,my_float,my_int1,my_character,my_int2]
print(my_list3)
print("---------------")

print(my_list3[0])
print(my_list3[1])
print(my_list3[2])
print("----------------")

print(my_list3[3:])
print(my_list3[:2])
print(my_list3[1:3])
print(my_list3[-3:])

print("\n------12-------\n")

#list as tuple -2
# return the tuple containing quotient and remainder
def quotientandremainder(dividend, divisor):
 #return the tuple of the quotient and remainder
  return (dividend // divisor , dividend % divisor)

my_dividend =11
my_divisor = 4
#assigm the first value of the result to my_quotient and second to my_remainder
[my_quotient, my_remainder] = quotientandremainder(my_dividend ,my_divisor)
print("Quotient:", my_quotient)
print("Remainder:",my_remainder)

print("---------------")

#list as tuple -3
my_super_tuple = [[1,2,3],[4,5,6],[7,8,9]]
print(my_super_tuple)

print("\n------13-------\n")

#List function
my_list = [17,12,9,18,11,19,7,13,14,16,1,10,8,4,6,3,15,2,5,20]
print(my_list,":Original list")
my_list.sort()
print(my_list,":After sorting")
my_list.append(21)
print(my_list,":After appending 21")
print("---------------")

my_other_list = [26,22,23,24]
my_list.extend(my_other_list)
print(my_list,":After extending with my_other_list")
my_list.insert(15,25)
print(my_list,";After inserting 25 at the index 15")
my_list.remove(26)
print(my_list,":After removing 26")

print("\n-------------\n")
my_list.sort()
print(my_list,":After sorting again")
my_list.reverse()
print(my_list,":After reversing")
my_list.pop()
print(my_list,":After popping")
del my_list[-5:]
print(my_list,":After deleting the last five items")

print("\n------14-------\n")

#Scope debugging in python-1

grades = [100,95,93,91,90,89,87,87,85,84,82]
sum = 0
count =0
for grade in grades:
    count= count+1
    sum = grade
print(sum/count)

print("\n------15-------\n")
#Iterating over a list
#average the number in the list
def average(inlist):
  sum = 0
  for number in inlist:
      sum += number
  return sum/len(inlist)

my_list1 = [1,2,3,4,5,6,7,8,9]
my_list2 = [97,87,91,83,85,91,95,99,81,85]

print("The average of my_list1 is:", average(my_list1))
print("The average of my_list2 is:", average(my_list2))

print("\n------16-------\n")
#iterating over a 2D lst
#average the number in the list
#average each list in 2D list
def twoD_average(in2Dlist):
    result = []
    #for each list in the list of lists
    for numlist in in2Dlist:
        sum = 0
        #for each number in the current list
        for number in numlist:
            sum += number
        #Append this list's average to result
        result.append(sum/len(numlist))
    return result

my_2Dlist = [[91,95,89,92,85],
             [85,87,91,81,82],
             [79,75,85,83,89],
             [81,89,91,91,90],
             [99,91,95,89,90]]
print("Averages:",twoD_average(my_2Dlist))

print("\n------17-------\n")

#List and function-1
#Average each list in 2D list
def TwoDaverage_with_pop(in_2D_list):
    reuslt = []
    #Repeat until in2D_list is empty
    while len(in_2D_list) > 0:
        #Remove and assign the last item of in2D_list to numlist
        numlist = in_2D_list.pop()
        sum = 0
        count = 0
        #repeat until numlist is empty
        while len(numlist)>0:
            #remove and save last item of numlist to number
            number = numlist.pop()
            sum += number
            count += 1
        #Insert the result at the beginning of the result
        reuslt.insert(0,sum/count)
    return reuslt

my_2D_list = [[91,95,89,92,85],[85,87,91,81,82],[79,75,85,83,89],[81,89,91,91,90],[99,91,95,89,90]]

print("Averages:", TwoDaverage_with_pop(my_2D_list))
print("my_2D_list:",my_2D_list)

print("\n------18-------\n")

#List and functions-2
my_string = "Hello,world"
my_list = [4,1,2,3]
print("my_string before upper():",my_string)
print("my_list before short():",my_list)
#Return an uppercase of my_string
my_string.upper()
#shorts my list in place
my_list.sort()
print("my_string before upper():",my_string)
print("my_list before sort():",my_list)

print("\n------19-------\n")
# List vs. Tuple






