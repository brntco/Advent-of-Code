import re

f = open("221204input.txt")
data = f.readlines()
data = [item.replace("\n", "") for item in data]
data_r1 = [pair.split(",") for pair in data]
data_r2 = []
for pair in data_r1:
    for each in pair:
        div = each.split("-")
        data_r2.append(div)
data_r3 = [int(sector) for pair in data_r2 for sector in pair]
print(data_r3)
overlaps = 0
duplicates = 0
print(len(data_r3))

for sector in range(0, len(data_r3), 4):
    elf_A_start = data_r3[sector]
    elf_A_end = data_r3[sector + 1]
    elf_A_scope = elf_A_end - elf_A_start + 1
    elf_B_start = data_r3[sector + 2]
    elf_B_end = data_r3[sector + 3]
    elf_B_scope = elf_B_end - elf_B_start + 1
    scope_difference = elf_A_scope - elf_B_scope

    # A encompasses
    if elf_A_start <= elf_B_start and elf_A_end >= elf_B_end:
        overlaps += 1
    # B encompasses
    elif elf_B_start <= elf_A_start and elf_B_end >= elf_A_end:
        overlaps += 1

    if elf_B_start >= elf_A_start and elf_B_start <= elf_A_end:
        duplicates += 1
    elif elf_B_end >= elf_A_start and elf_B_end <= elf_A_end:
        duplicates += 1
    elif elf_A_end >= elf_B_start and elf_A_end <= elf_B_end:
        duplicates += 1
    elif elf_A_start >= elf_B_start and elf_A_start <= elf_B_end:
        duplicates += 1
print(overlaps)
print(duplicates)
