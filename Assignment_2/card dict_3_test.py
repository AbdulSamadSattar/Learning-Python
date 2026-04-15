import random

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

    print(name, ':', p1)
    
    counter = 0
    a = 0
    b = 0

    while counter < 3:
        counter += 1
        chosen_card_p1 = input('Choose one card from above: ')
        chosen_card_p2 = random.choice(p2)
        print(name, chosen_card_p1)
        print(opponent, chosen_card_p2)
    
        if chosen_card_p1.capitalize() not in p1:
            print("Invalid card selection. Exiting...")
            return
     
        if deck[chosen_card_p1.capitalize()] > deck[chosen_card_p2]:
            print(name, 'You Got One Point')
            a += 1
        elif deck[chosen_card_p1.capitalize()] < deck[chosen_card_p2]:
            print(opponent, ' got One Point')
            b += 1
        else:
            print("It's a tie!")
    
        p1.remove(chosen_card_p1.capitalize())
        print("Remaining cards:", p1)
        p2.remove(chosen_card_p2)
        print("Points of", name, a)
        print("Points of", opponent, b)
        
    if a > b:
        print("\n\tWinner: '", name, "'")
    else:
        print("\n\tWinner: '", opponent, "'")


play_cards()
