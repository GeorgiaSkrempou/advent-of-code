import itertools
import re

with open ('crates.txt') as f: 
    lines = [line for line in f.readlines()]

move_lines = [line.strip() for line in lines[10:]]
crate_lines = [item[:-1] for item in itertools.islice([line for line in lines], 8)]

crate_lines.reverse()

x = 1
crates_dict = {}
mapping = {}
for i in range(1,10):
    crates_dict.update({i: []})
    mapping.update({x:i})
    x+=4

for line in crate_lines:
    for i, character in enumerate(line):
        if character not in ' []':
            crates_dict[mapping[i]].append(character)

for i in range(len(move_lines)):
    numbers = re.findall('[0-9]+', move_lines[i])
    last_n_boxes = crates_dict[int(numbers[1])][-int(numbers[0]):]
    loop_length = len(last_n_boxes)
    for element in range(loop_length):
        crates_dict[int(numbers[2])].append(last_n_boxes.pop())
    del crates_dict[int(numbers[1])][len(crates_dict[int(numbers[1])]) -int(numbers[0]):]

my_code = ""
for key, value in crates_dict.items():
    my_code += value[-1]

print(my_code)
