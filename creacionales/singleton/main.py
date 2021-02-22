from singleton import Card


def main():
    card1 = Card()
    card1.card_number = '0000'
    print(f'card1={card1.card_number}')

    card2 = Card()
    card2.card_number = '1111'

    print(f'card1={card1.card_number}')
    print(f'card2={card2.card_number}')
    print(f'card1={id(card1.card_number)}')
    print(f'card2={id(card2.card_number)}')


if __name__ == '__main__':
    main()