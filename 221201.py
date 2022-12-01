pack, packofpacks, cal_pack = [], [], []
inpt = open("221201input.txt")
lst = inpt.readlines()
lst = [item.replace("\n", "") for item in lst]
lst.append("")
for each in lst:
    if each != "":
        num = int(each)
        pack.append(num)
    else:
        packofpacks.append(pack)
        pack = []
for packs in packofpacks:
    cal_load = 0
    for snacks in packs:
        cal_load += snacks
    cal_pack.append(cal_load)
cal_pack.sort(reverse = True)
elf = cal_pack[0]
backup_elf1 = cal_pack[1]
backup_elf2 = cal_pack[2]
print(elf)
print(elf + backup_elf1 + backup_elf2)

