file = open("input.txt", "r")

tmpCalories = 0
calories = []

for line in file:
    actualLine = line.rstrip('\n')
    # print(actualLine)

    if actualLine == '':
        calories.append(tmpCalories)
        tmpCalories = 0
    else:
        tmpCalories += int(actualLine)

calories.sort()

totalCalories = 0
j = 0
for i in range(len(calories)-1, -1, -1):
    totalCalories += calories[i]
    j += 1
    print("the ", j, "calories is ", calories[i])

    if j == 3:
        break

print("the total calories of the top 3 is ", totalCalories)