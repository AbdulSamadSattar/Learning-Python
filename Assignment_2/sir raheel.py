import random

card = ["AD","KD","QD","JD","AH","KH","QH","JH",
       "AC","KC","QC","JC","AS","KS","QS","JS"]
random.shuffle(card)

p1 = []
p2 = []
p3 = []
p4 = []
p5=[]

for i in range(0,4):
    p1.append(card[i])

for j in range(4,8):
    p2.append(card[j])

for k in range(8,12):
    p3.append(card[k])

for l in range(12,16):
    p4.append(card[l])
    
print("Player 1: ",p1)
print("Player 2: ",p2)
print("Player 3: ",p3)
print("Player 4: ",p4)