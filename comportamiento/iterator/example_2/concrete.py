from typing import List

from data import Card


class CardIterator:
    def __init__(self, cards: List[Card]):
        self.__cards = cards
        self.__position = 0

    def __bool__(self) -> bool:
        return self.__position < len(self.__cards)

    def __next__(self) -> Card:
        """
        Si se ejecuta con un while no hay necesidad del condicional ni del raise.
        Si se ejecuta con un for este es el ejemplo apropiado.

        Return:
            Card
        """
        if self:
            card = self.__cards[self.__position]
            self.__position += 1
            return card
        raise StopIteration


class CardList:
    def __init__(self, cards: List[Card]):
        self.__cards = cards

    def __iter__(self) -> CardIterator:
        return CardIterator(self.__cards)
