import re

with open('crates.txt') as f:
    lines = [line.strip() for line in f.readlines()]

crates_dict = {
    "1": ["G", "F", "V", "H", "P", "S"],
    "2": ["G", "J", "F", "B", "V", "D", "Z", "M"],
    "3": ["G", "M", "L", "J", "N"],
    "4": ["N", "G", "Z", "V", "D", "W","P"],
    "5": ["V", "R", "C", "B"],
    "6": ["V", "R", "S", "M", "P", "W", "L", "Z"],
    "7": ["T", "H", "P"],
    "8": ["Q", "R", "S", "N", "C", "H", "Z", "V"],
    "9": ["F", "L", "G", "P", "V", "Q", "J"]
}

for i in range(10, len(lines)):
    numbers = re.findall('[0-9]+', lines[i])
    last_n_boxes = crates_dict[f"{numbers[1]}"][-int(numbers[0]):]
    loop_length = len(last_n_boxes)
    for element in range(loop_length):
        crates_dict[f"{numbers[2]}"].append(last_n_boxes.pop())
    del crates_dict[f"{numbers[1]}"][len(crates_dict[f"{numbers[1]}"]) -int(numbers[0]):]

my_code = ""
for key, value in crates_dict.items():
    my_code += value[-1]

print(my_code)
