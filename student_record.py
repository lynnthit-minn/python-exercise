student_record = [
    ("Joe",68)
]
while True :
    print("CLICK 1 to add new student, CLICK 2 to display student record, CLICK 3 to exit program")
    choice = int(input("Choose 1,2 or 3 : "))
    if choice == 1 :
        name = input("Enter student name : ")
        marks = input("Enter student mark : ")
        result = name,marks
        student_record.append(result)
    elif choice == 2 :
        for i in range(len(student_record)) :
            print(student_record[i])
    elif choice == 3 :
        print("Exiting the program")
    else:
        print("Not an available number. Please enter 1,2 or 3 : ")