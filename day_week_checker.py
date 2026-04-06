days = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
day_number = int(input("Enter a day number from 1-7. : "))
if day_number == 1:
    print("The day for 1 is:",days[0])
elif day_number == 2:
    print("The day for 2 is:",days[1])
elif day_number == 3:
    print("The day for 3 is:",days[2])
elif day_number == 4:
    print("The day for 4 is:",days[3])
elif day_number == 5:
    print("The day for 5 is:",days[4])
elif day_number == 6:
    print("The day for 6 is:",days[5])
elif day_number == 7:
    print("The day for 7 is:",days[6])
else:
    print("Not an available number. Please pick a number from 1-7. ")