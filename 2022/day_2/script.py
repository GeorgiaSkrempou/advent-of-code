# FIST PART

# A = Rock (1)
# B = paper (2)
# C = Scissors (3)

# X = Rock (1)
# Y = Paper (2)
# Z = Scissors (3)

rock = 1
paper = 2
scissors = 3
win = 6
draw = 3
loss = 0

combos = {
    "A X": rock+draw, 
    "A Y": paper+win,
    "A Z": scissors+loss,
    "B X": rock+loss,
    "B Y": paper+draw,
    "B Z": scissors+win,
    "C X": rock+win,
    "C Y": paper+loss,
    "C Z": scissors+draw,
}

with open('list.txt') as f:
    lines = [line.strip() for line in f.readlines()]

score = 0
for line in lines: score +=combos[line]

print(score)

# SECOND PART

# A = Rock (1)
# B = paper (2)
# C = Scissors (3)

# X = loose 0
# Y = draw 3
# Z = win 6


second_combos = {
    "A X": loss+scissors, 
    "A Y": draw+rock,
    "A Z": win+paper,
    "B X": loss+rock,
    "B Y": draw+paper,
    "B Z": win+scissors,
    "C X": loss+paper,
    "C Y": draw+scissors,
    "C Z": win+rock,
}

with open('list.txt') as f:
    lines = [line.strip() for line in f.readlines()]

score = 0
for line in lines: score +=second_combos[line]

print(score)