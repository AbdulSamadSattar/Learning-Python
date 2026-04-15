'''Design and develop a card game for two players; when player one and player two pass the card,
it compares who will winthe game, and then it prints using "pretty print.'''

import random
import pprint

def play_cards():
    deck = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    p1 = random.choice(deck[9:13])
    p2 = random.choice(deck)

    print("Abdul Samad:",p1)
    print("Sir Raheel:", p2)

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


