mark = []
total = 0
for i in range(1,6) :
    score = int(input("Enter student's {i} mark : "))
    mark.append(score)
for j in range(len(mark)) :
    total = total + mark[j]
print("*"*60)
print("Total : ",total)
print("Average : ",total/len(mark))