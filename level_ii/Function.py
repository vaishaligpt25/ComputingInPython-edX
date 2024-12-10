


def printyen():
    print("#", end='')




printyen()
print(5)



def return_Yen ():
    return "#"
print(return_Yen(), end="")
print(5)





def return_yen_(amount):
    return "@" + str(amount)
print(return_yen_(5))





def return_yen_amount(amount):
    return "@" + str (amount)

input_amount = int(input("Enter the amount : "))
print(return_yen_amount(input_amount))




def  currency_amount(currency , amount):
    if currency == "Jpy":
        return "X" + str(amount)
    elif currency == "USD":
        return "Y" + str(amount)
    elif currency == "GBP":
        return "Z" + str(amount)
    else:
        return str (amount)

print(currency_amount("GBP",5))





print ("A", "B", "C",sep = "@",)

print ("A", "B", "C",sep = "",end = "")
print("A", "B", "C", sep = "@", end = "!" )