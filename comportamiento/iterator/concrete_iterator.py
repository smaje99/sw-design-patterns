from typing import List

from iterator import Iterator
from data import Card


class CardIterator(Iterator):
    def __init__(self, cards: List[Card]):
        self.__cards = cards
        self.__position = 0

    def next(self) -> Card:
        card = self.current_item()
        self.__position += 1
        return card

    def has_next(self) -> bool:
        return self.__position < len(self.__cards)

    def current_item(self) -> Card:
        return self.__cards[self.__position]