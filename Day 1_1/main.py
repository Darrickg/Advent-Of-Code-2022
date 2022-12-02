file = open("day1_1", "r")

#test test
maxElf = 0
maxCalories = 0
tmpElf = 0
tmpCalories = 0

for line in file:
    actualLine = line.rstrip('\n')
    # print(actualLine)

    if actualLine == '':
        if tmpCalories > maxCalories:
            maxCalories = tmpCalories
            maxElf = tmpElf

        tmpElf += 1
        tmpCalories = 0
    else:
        tmpCalories += int(actualLine)

print("max calories is: ", maxCalories)
print("it belongs to elf ", maxElf)