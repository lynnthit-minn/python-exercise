sides = int(input("Enter how many equal sides your triangle has. 0,2 or 3 : "))
if sides == 3:
    print("That is an Equilateral triangle. ")
elif sides == 2:
    print("That is an Isosceles triangle. ")
elif sides == 0:
    print("That is a Scalene triangle. ")