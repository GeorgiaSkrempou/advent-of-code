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

top_elf_calories = max(elf_calories)

print(top_elf_calories)

top_3_calories = top_elf_calories
for i in range(2):
    elf_calories.remove(top_elf_calories)
    top_elf_calories = max(elf_calories)
    top_3_calories += top_elf_calories


print(top_3_calories)


