from data import Card
from concrete_aggregate import CardList


def main():
    cards = [
        Card('Visa'),
        Card('Amex'),
        Card('GoogleCard'),
        Card('MasterCard'),
        Card('AppleCard'),
    ]

    list_of_cards = CardList(cards)
    iterator = list_of_cards.iterator()

    while iterator.has_next():
        print(iterator.next())


if __name__ == '__main__':
    main()
