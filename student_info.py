student_info = [["James",49],
                ["Lynn",80],
                ["Mike",68],
                ["Daisy",86],
                ["Adam",34]
                ]
passcount = 0
failcount = 0
passlist = []
faillist = []
for i in range(len(student_info)) :
    if student_info[i][1] >= 50 :
        passcount += 1
        passlist.append(student_info[i][0])
    else:
        failcount += 1
        faillist.append(student_info[i][0])
print("Total passed students : ",passcount)
print("Total failed students : ",failcount)
print("Students who passed are : ",passlist)
print("Students who failed are : ",faillist)