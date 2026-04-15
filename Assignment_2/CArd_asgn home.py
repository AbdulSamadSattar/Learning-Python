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
        
    name=input('Enter Your Name:')
    opponent=input('Enter Your 0pponent Name:')

    print(name, ':' ,p1)
    
    chosen_cardp1 = input('Choose one card from above: ')
    chosen_cardp2 = random.choice(p2)
    print(name,chosen_cardp1.capitalize())
    print(opponent,':' ,p2)
    print(opponent,chosen_cardp2)
    
    if chosen_cardp1.capitalize() not in p1:
        print("Invalid card selection. Exiting...")
        return
    if chosen_cardp1.capitalize() > (chosen_cardp2):
        winner = name
    elif chosen_cardp1.capitalize() < (chosen_cardp2):
        winner = opponent
    else:
        winner = "It's a tie!"
    print('Winner',winner)
    
play_cards()

