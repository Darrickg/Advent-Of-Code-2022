def createSet(array):
    setList = []
    for i in range(int(array[0]), int(array[1]) + 1):
        setList.append(i)
    return setList

def improperSubset(arr1, arr2):
    for i in arr1:
        for j in arr2:
            if (i == j):
                return True
    return False

file = open("day4_1.txt", "r")

count = 0
for line in file:
    actualLine = line.rstrip('\n')
    tasks = actualLine.split(',')
    elf1 = tasks[0].split('-')
    elf2 = tasks[1].split('-')
    elf1list = createSet(elf1)
    elf2list = createSet(elf2)
    if (improperSubset(elf1list, elf2list) == True):
        count += 1

print(count, "is the answer")