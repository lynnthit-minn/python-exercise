positive_list = []
while True :
    number = int(input("Enter positive number : "))
    if number > 0:
        positive_list.append(number)
    else:
        print("That is a negetive number ")
        break
print("The possitive number list ",positive_list)