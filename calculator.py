while True:
    print("1 is for addition, 2 is for subtraction, 3 is for multiplication, 4 is for division")
    choice = input("Choose option 1,2,3,4,5 : ")
    if choice == "1" :
        num1 = int(input("Enter first number : "))
        num2 = int (input("Enter second number : "))
        print(f"The sum of {num1} + {num2} =", num1 + num2)
    elif choice == "2" :
        num1 = int(input("Enter first number : "))
        num2 = int(input("Enter second number : "))
        print(f"The subtraction of {num1} - {num2} =", num1 - num2)
    elif choice == "3" :
        num1 = int(input("Enter first number : "))
        num2 = int(input("Enter second number : "))
        print(f"The subtraction of {num1} * {num2} =", num1 * num2)
    elif choice == "4" :
        num1 = int(input("Enter first number : "))
        num2 = int(input("Enter second number : "))
        print(f"The subtraction of {num1} / {num2} =", num1 / num2)
    elif choice == "5" :
        print("Exiting program")
        break
    else:
        print("Not an available number")