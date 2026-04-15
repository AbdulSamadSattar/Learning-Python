#Design and develop a card game for two players; when player one and player two pass the card, it compares who will win the game, and then it prints using "pretty print
#Abdul Samad
#Assignment 3(1)
import random
import pprint
def play_cards():
    deck = {'Ace': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13}
    cards = list(deck.keys())
    random.shuffle(cards)
    
    p1 = []
    p2 = []
    
    for i in range(0, 3):
        p1.append(cards[i])
    for j in range(3, 6):
        p2.append(cards[j])
    
    name = input('Enter Your Name: ')
    opponent = input('Enter Your Opponent Name: ')
    print('\n'+name.title(), ':', p1)
    
    counter = 0
    a=0
    b=0
    while counter < 3:
        counter += 1
        chosen_card_p1 = input('Choose one card from above: ')
        chosen_card_p2 = random.choice(p2)
        print(name.title(), chosen_card_p1)
        #print(opponent, ':', p2)  #if wonna see opponent card
        print(opponent.title(), chosen_card_p2)
    
        if chosen_card_p1.capitalize() not in p1:
            print("Invalid card selection. Exiting...")
            return
     
        if deck[chosen_card_p1.capitalize()] > deck[chosen_card_p2]:
            print(name.title(),'You Got One Point\n')
            a += 1
        elif deck[chosen_card_p1.capitalize()] < deck[chosen_card_p2]:
            print(opponent.title(),' got One Point\n')
            b += 1
            
        else:
            print ("It's a tie!")
    
        p1.remove(chosen_card_p1.capitalize())
        p2.remove(chosen_card_p2)
        print("Points of",name.title(),':',a)
        print("Points of",opponent.title(),':',b)
        print("Remaining cards:", p1)
    if a>b:
            print('\n\tWinner: \'',name.title(),'\'')
    else:
            print('\n\tWinner: \'',opponent.title(),'\'')
    pprint.pprint(deck)
    
play_cards()


