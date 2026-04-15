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
    
    name = input('Enter Your Name: ')
    opponent = input('Enter Your Opponent Name: ')

    print(name, ':', p1)
    
    chosen_card_p1 = input('Choose one card from above: ')
    chosen_card_p2 = random.choice(p2)
    print(name, chosen_card_p1)
    print(opponent, ':', p2)
    print(opponent, chosen_card_p2)
    
    if chosen_card_p1.capitalize() not in p1:
        print("Invalid card selection. Exiting...")
        return
    
    if deck[chosen_card_p1.capitalize()] > deck[chosen_card_p2]:
        print(name,'You Got One Point')
    elif deck[chosen_card_p1.capitalize()] < deck[chosen_card_p2]:
        print(opponent,'Your opponent is leading by One Point')
    else:
        print ("It's a tie!")
    
    p1.remove(chosen_card_p1)
    print("Remaining cards:", p1)
    
    print(name, p1)
    chosen_card_p12 = input('Choose one card from above: ')
    
    p1.remove(chosen_card_p12)
    print("Remaining cards:", p1)
    
    print(name, p1)
    chosen_card_p13 = input('Choose one card from above: ')
    p1.remove(chosen_card_p13)
    print("Remaining cards:", p1)
    
  #  print('Winner:', winner)

play_cards()
