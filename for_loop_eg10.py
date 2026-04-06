students =["James","Luke","Lynn","Mark"]
find_students = str(input("Enter student name ; "))
result = students[0]
found = False
for i in range(len(students)) :
    if find_students == students[i] :
        result = students[i]
        found = True
        break
if found==True:
    print(f"Found students name {result} at position {i}")
else:
    print("Not found")