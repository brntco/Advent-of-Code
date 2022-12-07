f = open("221206input.txt")
data = f.readlines()
data = [item.replace("\n", "") for item in data]
#part1
for code in data:
    for x in range(len(code)-4):
        if len(set(code[x:x+4])) == 4:
            r = len(code[0:x+4])
            break
    print(r)
for code in data:
    for x in range(len(code)-14):
        if len(set(code[x:x+14])) == 14:
            r = len(code[0:x+14])
            break
    print(r)
