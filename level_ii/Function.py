def printyen():
    print("#", end='')

print("\n------1--------\n")

printyen()
print(5)

print("\n------2--------\n")

def return_Yen ():
    return "#"
print(return_Yen(), end="")
print(5)

print("\n-------3-------\n")

def return_yen_(amount):
    return "@" + str(amount)
print(return_yen_(5))

print("\n-------4-------\n")

def return_yen_amount(amount):
    return "@" + str (amount)

input_amount = int(input("Enter the amount : "))
print(return_yen_amount(input_amount))

print("\n-------5-------\n")

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