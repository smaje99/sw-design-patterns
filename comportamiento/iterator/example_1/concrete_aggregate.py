import typing

from aggregate import List
from iterator import Iterator
from data import Card
from concrete_iterator import CardIterator


class CardList(List):
    def __init__(self, cards: typing.List[Card]) :
        self.__cards = cards

    def iterator(self) -> Iterator:
        return CardIterator(self.__cards)
