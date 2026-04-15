import random

def play_cards():
    deck = {'Ace': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13}
    p1 = ['10', '7', 'Jack']
    p2 = ['8', '5', 'Queen']
    counter = 0
    a = 0
    b = 0
    
    while counter < 3:
        counter += 1
        chosen_card_p1 = input('Choose one card from above: ')
        chosen_card_p2 = random.choice(p2)
        print('A.Samad:', chosen_card_p1)
        print('Ahmed:', chosen_card_p2)

        if deck[chosen_card_p1.capitalize()] > deck[chosen_card_p2]:
            print('A.Samad', 'You Got One Point')
            a += 1
        elif deck[chosen_card_p1.capitalize()] < deck[chosen_card_p2]:
            print("Ahmed", 'got One Point')
            b += 1
        else:
            print("It's a tie!")
    
        p1.remove(chosen_card_p1.capitalize())
        print("Remaining cards:", p1)
        p2.remove(chosen_card_p2)
        print('A.Samad',a)
        print("Ahmed",b)

    if a > b:
        print("\n\tWinner: 'A.Samad'")
    else:
        print("\n\tWinner: 'Ahmed'")


play_cards()
