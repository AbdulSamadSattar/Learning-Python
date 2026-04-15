import random

def play_cards():
    deck = {'Ace': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13}
    cards = list(deck.keys())
    random.shuffle(cards)
    
    p1 = []
    p2 = []
    
    for i in range(0, 4):
        p1.append(cards[i])

    for j in range(4, 8):
        p2.append(cards[j])
        
    print("Abdul Samad:", p1)
    chosen_card_p11 = input('Choose one card from above: ')
    p1.remove(chosen_card_p11)
    print("Remaining cards:", p1)
  
    print("Abdul Samad:", p1)
    chosen_card_p12 = input('Choose one card from above: ')
    p1.remove(chosen_card_p12)
    print("Remaining cards:", p1)
    
    print("Abdul Samad:", p1)
    chosen_card_p13 = input('Choose one card from above: ')
    p1.remove(chosen_card_p13)
    print("Remaining cards:", p1)
play_cards()
