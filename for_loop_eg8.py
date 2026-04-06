numbers = (65,78,90,34,55,23)
maximum = numbers[0]
minimum = numbers[0]
for i in range(len(numbers)):
    if numbers[i] > maximum:
        maximum = numbers[i]
    if numbers[i] < minimum:
        minimum = numbers[i]
print("The maximum number is :",maximum)
print("The minimum number is :",minimum)