f = open("221205input.txt")
data = f.readlines()
data = [item.replace("\n", "") for item in data]
for space in range(len(data)):
    if data[space] == "":
        x = space - 1
        break
stack = data[:x]
instructions = data[(x+2):]
column_list = (data[x:x+1])[-1]
column_number = int(column_list[-2])

templist = []
complete_list = []
columns = []
for row in stack:
    for letter in range(1, len(row), 4):
        templist.append(row[letter])
    complete_list.append(templist)
    templist = []

for column in range(column_number):
    for row in complete_list:
        if row[column] != " ":
            templist.append(row[column])
    columns.append(templist)
    templist = []
print(columns)
#Part 1:
# for each in instructions:
#     move = int(each[5:-12])
#     from_column = columns[int(each[-6])-1]
#     to_column = columns[int(each[-1])-1]
#     for moves in range(move):
#         to_column.insert(0, from_column[0])
#         from_column.pop(0)
#part 2:
print(columns)
for each in instructions:
    move = int(each[5:-12])
    from_column = columns[int(each[-6])-1]
    to_column = columns[int(each[-1])-1]
    templist = from_column[0:move]
    for q in range(len(templist)):
        to_column.insert(q, templist[q])
    for moves in range(move):
        from_column.pop(0)
    templist = []


answer = ""
for each in columns:
    answer += each[0]
print(answer)