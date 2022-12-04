#Lowercase item types a through z have priorities 1 through 26.
#Uppercase item types A through Z have priorities 27 through 52.

from string import ascii_lowercase, ascii_uppercase

all_characters = ascii_lowercase+ascii_uppercase
priorities = {f"{c}": i+1 for i,c in enumerate(all_characters)}

with open('list.txt') as f:
    lines = [line.strip() for line in f.readlines()]

sum_priorities = 0
for line in lines:
    firstpart = set(line[:int(len(line)/2)])
    secondpart = set(line[int(len(line)/2):])
    common_letter = firstpart.intersection(secondpart).pop()
    sum_priorities += priorities[common_letter]

print(sum_priorities)

groups = []
for i in range(len(lines)):
    groups.append(lines[0:3])
    del lines[0:3]
    if len(lines) == 0:
        break
 
sum_badge_priorities = 0
for group in groups:
    badge_letter=(set(group[0])&set(group[1])&set(group[2])).pop()
    sum_badge_priorities += priorities[badge_letter]

print(sum_badge_priorities)


