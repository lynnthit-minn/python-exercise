number = int(input("Enter a number between 1-5 : "))
if number == 1:
    factorial1 = 1 * 1
    print("The factorial number of 1 is ", factorial1)
elif number == 2:
    factorial2 = 2 * 1
    print("The factorial number of 2 is ", factorial2)
elif number == 3:
    factorial3 = 3 * 2 * 1
    print("The factorial number of 3 is ", factorial3)
elif number == 4:
    factorial4 = 4 * 3 * 2 * 1
    print("The factorial number of 4 is ", factorial4)
elif number == 5:
    factorial5 = 5 * 4 * 3 * 2 * 1
    print("The factorial number of 5 is ", factorial5)
else:
    print("Number not available.")