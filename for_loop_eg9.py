numbers = [23,45,34,55,67]
find_number = int(input("Enter number :"))
result = numbers[0]
found = False
for i in range(len(numbers)):
    if find_number == numbers[i]:
        result = numbers[i]
        found = True
        break
if found==True:
    print(f"Found! the value {result} of position is :",i)
else:
    print("Not found")