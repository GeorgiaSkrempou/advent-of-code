with open('list.txt') as f:
    lines = [line.strip() for line in f.readlines()]

elf_pairs = [line.split(',') for line in lines]

count_exact = 0
count_overlaps = 0
for elf_pair in elf_pairs:
    both_elves = []
    for sections in elf_pair:
        x, y = sections.split("-")
        x = int(x)
        y = int(y)        
        elf_sections = [i for i in range(x, y+1)]
        both_elves.append(elf_sections)

    elf_a = set(both_elves[0])
    elf_b = set(both_elves[1])
    
    if (elf_a & elf_b):
        count_overlaps+=1
   
    if (all(item in both_elves[0] for item in both_elves[1]) or all(item in both_elves[1] for item in both_elves[0])):
        count_exact+=1

print(count_exact)
print(count_overlaps)

    
