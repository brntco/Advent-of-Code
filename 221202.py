opponent_lst = []
inpt = open("221202input.txt")
lst = inpt.readlines()
lst = [item.replace("\n", "") for item in lst]
opponent_lst = lst

my_score = 0
for rps in range(len(lst)):
    #rock rock = 1+3
    if opponent_lst[rps]=="A X":
        my_score += 4
    #rock paper = 6 + 2
    if opponent_lst[rps] == "A Y":
        my_score += 8
    #rock smash scissors = 0+3
    if opponent_lst[rps] == "A Z":
        my_score += 3
    #paper covers rock = 0+1
    if opponent_lst[rps] == "B X":
        my_score += 1
    #paper paper = 3+2
    if opponent_lst[rps] == "B Y":
        my_score += 5
    #paper cutby scissors = 6+3
    if opponent_lst[rps] == "B Z":
        my_score += 9
    #scissors smashby rock = 6+1
    if opponent_lst[rps]=="C X":
        my_score += 7
    #scissors cuts paper =  0+2
    if opponent_lst[rps] == "C Y":
        my_score += 2
    #scissors scissors = 3+3
    if opponent_lst[rps] == "C Z":
        my_score += 6
print(my_score)

myscore=0
for rps in range(len(lst)):
    #rock lose with scissors 0+3
    if opponent_lst[rps]=="A X":
        myscore += 3
    #rock draw with rock = 3+1
    if opponent_lst[rps] == "A Y":
        myscore += 4
    #rock win with paper = 6 + 2
    if opponent_lst[rps] == "A Z":
        myscore += 8
    #paper lose with rock= 0+1
    if opponent_lst[rps] == "B X":
        myscore += 1
    #paper draw with paper= 3+2
    if opponent_lst[rps] == "B Y":
        myscore += 5
    #paper win with scissors= 6+3
    if opponent_lst[rps] == "B Z":
        myscore += 9
    #scissors lose with paper = 0+2
    if opponent_lst[rps]=="C X":
        myscore += 2
    #scissors draw scissors=  3+3
    if opponent_lst[rps] == "C Y":
        myscore += 6
    #scissors win rock= 6+1
    if opponent_lst[rps] == "C Z":
        myscore += 7
print(myscore)
