import re

stacks = [
    ['Z', 'T', 'F', 'R', 'W', 'J', 'G'],
    ['G', 'W', 'M'],
    ['J', 'N', 'H', 'G'],
    ['J', 'R', 'C', 'N', 'W'],
    ['W', 'F', 'S', 'B', 'G', 'Q', 'V', 'M'],
    ['S', 'R', 'T', 'D', 'V', 'W', 'C'],
    ['H', 'B', 'N', 'C', 'D', 'Z', 'G', 'V'],
    ['S', 'J', 'N', 'M', 'G', 'C'],
    ['G', 'P', 'N', 'W', 'C', 'J', 'D', 'L']
]

file = open("day5_1.txt", "r")

for line in file:
    actualLine = line.rstrip('\n')
    actualLine = re.findall(r'\d+', actualLine)

    fromVal = int(actualLine[1]) - 1
    toVal = int(actualLine[2]) - 1
    amount = int(actualLine[0])

    for i in range(amount):
        value = stacks[fromVal].pop()
        stacks[toVal].append(value)

lastCrates = []
for i in stacks:
    lastCrates.append(i[-1])

print(stacks)
print(lastCrates)
