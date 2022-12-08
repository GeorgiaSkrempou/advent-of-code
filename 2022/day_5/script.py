import itertools
import re

with open ('crates.txt') as f: 
    lines = [line for line in f.readlines()]

move_lines = [line.strip() for line in lines[10:]]
crate_lines = [item[:-1] for item in itertools.islice([line for line in lines], 8)]

crate_lines.reverse()
crate_lines_part_two = crate_lines

x = 1
crates_dict = {}
crates_dict_part_two = {}
mapping = {}
for i in range(1,10):
    crates_dict.update({i: []})
    crates_dict_part_two.update({i: []})
    mapping.update({x:i})
    x+=4

for line in crate_lines:
    for i, character in enumerate(line):
        if character not in ' []':
            crates_dict[mapping[i]].append(character)
            crates_dict_part_two[mapping[i]].append(character)

for i, ele in enumerate(move_lines):
    numbers = re.findall('[0-9]+', move_lines[i])
    last_n_boxes = crates_dict[int(numbers[1])][-int(numbers[0]):]
    loop_length = len(last_n_boxes)
    for element in range(loop_length):
        crates_dict[int(numbers[2])].append(last_n_boxes.pop())
    del crates_dict[int(numbers[1])][len(crates_dict[int(numbers[1])]) -int(numbers[0]):]

code = ""
for key, value in crates_dict.items():
    code += value[-1]

print(code)

for i, ele in enumerate(move_lines):
    numbers = re.findall('[0-9]+', move_lines[i])
    last_n_boxes = crates_dict_part_two[int(numbers[1])][-int(numbers[0]):]
    loop_length = len(last_n_boxes)
    for crate in crates_dict_part_two[int(numbers[1])][-int(numbers[0]):]:
        crates_dict_part_two[int(numbers[2])].append(crate)
    del crates_dict_part_two[int(numbers[1])][-int(numbers[0]):]

code = ""

for key, value in crates_dict_part_two.items():
    code += value[-1]

print(code)

