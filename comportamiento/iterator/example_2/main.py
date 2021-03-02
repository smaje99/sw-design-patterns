from concrete import CardList
from data import Card


def iterator_while(card_list):
    iterator = iter(card_list)
    while iterator:
        print(next(iterator))


def iterator_for(card_list):
    for card in card_list:
        print(card)


def main():
    cards = [
        Card('Visa'),
        Card('Amex'),
        Card('GoogleCard'),
        Card('MasterCard'),
        Card('AppleCard'),
    ]
    card_list = CardList(cards)
    iterator_while(card_list)
    print()
    iterator_for(card_list)


if __name__ == '__main__':
    main()
