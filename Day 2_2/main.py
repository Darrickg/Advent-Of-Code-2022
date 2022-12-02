# rock = a
# paper = b 
# scissors = c
# x = lose
# y = draw
# z = win

def opponentValue(value):
    if value == "A":
        return "rock"
    elif value == "B":
        return "paper"
    else:
        return "scissors"

def yourState(value):
    if value == "X":
        return "lose"
    elif value == "Y":
        return "draw"
    else:
        return "win"

def yourValue(oppVal, yourState):
    if oppVal == "rock":
        if yourState == "draw":
            return "rock"
        elif yourState == "win":
            return "paper"
        else:
            return "scissors"
    elif oppVal == "paper":
        if yourState == "draw":
            return "paper"
        elif yourState == "win":
            return "scissors"
        else:
            return "rock"
    else:
        if yourState == "draw":
            return "scissors"
        elif yourState == "win":
            return "rock"
        else:
            return "paper"

def calculateScore(yourState, yourVal):
    if yourState == "win":
        x = 6
    elif yourState == "draw":
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

file = open("day2_2.txt", "r")

score = 0

for line in file:
    actualLine = line.rstrip('\n')
    oppVal = opponentValue(actualLine[0])
    state = yourState(actualLine[2])
    yourVal = yourValue(oppVal, state)
    currScore = calculateScore(state, yourVal)
    score += currScore
    
print("your score is", score)