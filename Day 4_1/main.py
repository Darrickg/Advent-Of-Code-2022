def createSet(array):
    setList = set()
    for i in range(int(array[0]), int(array[1]) + 1):
        setList.add(i)
    return setList

file = open("day4_1.txt", "r")

count = 0
for line in file:
    actualLine = line.rstrip('\n')
    tasks = actualLine.split(',')
    elf1 = tasks[0].split('-')
    elf2 = tasks[1].split('-')
    elf1list = createSet(elf1)
    elf2list = createSet(elf2)
    if (elf1list.issubset(elf2list) == True or elf2list.issubset(elf1list) == True):
        count += 1

print(count, "is the answer")