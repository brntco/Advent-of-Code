import re
f = open("221203input.txt")
aoc_input = f.readlines()
aoc_input = [item.replace("\n", "") for item in aoc_input]


sum_priorities = 0

for each in aoc_input:
    each2 = each[int(len(each)/2):]
    each1 = each[:int(len(each)/2)]

    for letter in range(int(len(each)/2)):
        x = re.search(each1[letter], each2)
        if x:
            if (ord(each1[letter])) < 97:
                sum_priorities += ord(each1[letter])-38
            else:
                sum_priorities += ord(each1[letter])-96
            break

print(sum_priorities)

#part 2
badge_priorities = 0

for member in range(0, len(aoc_input), 3):
    elf1 = aoc_input[member]
    elf2 = aoc_input[member + 1]
    elf3 = aoc_input[member + 2]
    for char in range(len(aoc_input[member])):
        p = re.search(elf1[char], elf2)
        q = re.search(elf1[char], elf3)
        if p and q:
            if (ord(elf1[char])) < 97:
                badge_priorities += ord(elf1[char])-38
            else:
                badge_priorities += ord(elf1[char])-96
            break


print(badge_priorities)
