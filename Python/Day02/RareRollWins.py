import random
a = [1,2,3,4,5,6]
b = [1,2,3,4,5,6]

outcomes = []
for i in a :
    for j in b :
        outcomes.append((i,j))

dict = {}
for i in outcomes :
    sum = i[0]+i[1]
    if sum in dict :
        dict[sum] += 1/len(outcomes)
    else :
        dict[sum] = 1/len(outcomes)

no_of_rounds = int(input("Enter no of rounds"))
p1 = 0
p2 = 0
for i in range(0,no_of_rounds) :
    p1_1 = random.randint(1,6)
    p1_2 = random.randint(1,6)
    p2_1 = random.randint(1,6)
    p2_2 = random.randint(1,6)
    sump1 = p1_1 + p1_2
    sump2 = p2_1 + p2_1
    if dict[sump1] < dict[sump2] :
        p1 += 1
    else :
        p2 += 1
    
if p1 > p2:
    print("Player1")
elif p2 > p1 :
    print("Player2")
else :
    print("Draw")