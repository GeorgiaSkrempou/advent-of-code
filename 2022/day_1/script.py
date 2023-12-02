with open('list.txt') as f:
    lines = f.readlines()

elf_calories = []
calories=0
for line in lines:
    if line == "\n":
        elf_calories.append(calories)
        calories=0
    else:
        calories += int(line)

print(max(elf_calories))

elf_calories.sort()
print(sum(elf_calories[-3:]))
