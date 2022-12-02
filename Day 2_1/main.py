# rock = a = x
# paper = b = y 
# scissors = c = z

def opponentValue(value):
    if value == "A":
        return "rock"
    elif value == "B":
        return "paper"
    else:
        return "scissors"

def yourValue(value):
    if value == "X":
        return "rock"
    elif value == "Y":
        return "paper"
    else:
        return "scissors"

def match(oppVal, yourVal):
    if oppVal == "rock":
        if yourVal == "rock":
            return "draw"
        elif yourVal == "paper":
            return "win"
        else:
            return "lose"
    elif oppVal == "paper":
        if yourVal == "paper":
            return "draw"
        elif yourVal == "scissors":
            return "win"
        else:
            return "lose"
    else:
        if yourVal == "scissors":
            return "draw"
        elif yourVal == "rock":
            return "win"
        else:
            return "lose"

def calculateScore(yourVal, state):
    if state == "win":
        x = 6
    elif state == "draw":
        x = 3
    else:
        x = 0

    if yourVal == "rock":
        y = 1
    elif yourVal == "paper":
        y = 2
    else:
        y = 3
    
    return x + y

file = open("day2_1.txt", "r")

score = 0

for line in file:
    actualLine = line.rstrip('\n')
    # print(actualLine)
    oppVal = opponentValue(actualLine[0])
    # print(oppVal)
    yourVal = yourValue(actualLine[2])
    # print(yourVal)
    state = match(oppVal, yourVal)
    # print(state)
    currScore = calculateScore(yourVal, state)
    # print(currScore)
    score += currScore
    
print("your score is", score)