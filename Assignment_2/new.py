import random
import pprint
def play_cards():
    deck = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    random.shuffle(deck)
    p1 = []
    p2 = []

    for i in range(0,4):
        p1.append(deck[i])

    for j in range(4,8):
        p2.append(deck[j])

    print("Abdul Samad: ",p1)
    print("Sir Raheel: ",p2)
    
    chosen_cardp1 = input('Choose one card from above: ')
    chosen_cardp2 = random.choice(p2)
    print(chosen_cardp1.capitalize())
    print(chosen_cardp2)
    
    if chosen_cardp1 not in p1:
        print("Invalid card selection. Exiting...")
        return
        
    if chosen_cardp1 > (chosen_cardp2):
        winner = "Abdul Samad"
    elif chosen_cardp1 < (chosen_cardp2):
        winner = "Sir Raheel"
    else:
        winner = "It's a tie!"
    print('Winner',winner)
play_cards()