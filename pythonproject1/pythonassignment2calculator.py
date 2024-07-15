Aastha = True
print("1-Addition\n2-Subtraction\n3-Multiplication\n4-Division\n5-Power\n6-Rounding\n7-Remaining\n0-Exit")

while Aastha is True:
    First = int(input("Enter the first digit:"))
    if First == 0:
        print("Closing the app")
        exit()
    Second = int(input("Enter the second digit:"))
    if Second == 0:
        print("Closing the app")
        exit()
    opp = int(input("Enter the Operator:"))
    if opp == 1:
        Sum = First + Second
        print(Sum)
    elif opp == 2:
        Sum = First - Second
        print(Sum)
    elif opp == 3:
        Sum = First * Second
        print(Sum)
    elif opp == 4:1
        Sum = First / Second
        print(Sum)
    elif opp == 5:
        Sum = First ** Second
        print(Sum)
    elif opp == 6:
        Sum = First // Second
        print(Sum)
    elif opp == 7:
        Sum = First % Second
        print(Sum)
    elif opp == 0:
        Aastha = False
        print("Closing the app")
    else:
        print("Wrong input")
