'''Design and develop a card game for two players; when player one and player two pass the card,
it compares who will winthe game, and then it prints using "pretty print.'''

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
    
    deck.index(p2)=(input('Choose one Card from above:' ,))
    
    if deck.index(p1) > deck.index(p2):
        winner = "Abdul Samad"
    elif deck.index(p1) < deck.index(p2):
        winner = "Sir Raheel"
    else:
        winner = "It's a tie!"

    print("Winner:", winner)

    # Pretty print the deck
    print("\nDeck:")
    pprint.pprint(deck)
play_cards()
