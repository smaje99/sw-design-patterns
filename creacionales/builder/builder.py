from typing import NamedTuple


class Card(NamedTuple):
    cardType: str
    number: str
    name: str
    expires: int
    credit: bool


class CardBuilder:
    def __init__(self, card_type: str, number: str):
        self.__card_type: str = card_type
        self.__number: str = number
        self.__name: str = None
        self.__expires: int = None
        self.__credit: bool = None

    def build(self) -> Card:
        return Card(
            self.__card_type,
            self.__number,
            self.__name,
            self.__expires,
            self.__credit
        )

    def name(self, name: str):
        self.__name = name
        return self
    
    def expires(self, expires: int):
        self.__expires = expires
        return self
    
    def credit(self, credit: bool):
        self.__credit = credit
        return self
