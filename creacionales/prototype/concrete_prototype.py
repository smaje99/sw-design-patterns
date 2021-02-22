from creacionales.prototype.prototype import PrototypeCard
from copy import copy


class Visa(PrototypeCard):
    def __init__(self):
        self.name = None

    def card(self) -> str:
        return 'Tarjeta Visa'

    def clone(self):
        return copy(self)


class Amex(PrototypeCard):
    def __init__(self):
        self.name = None

    def card(self) -> str:
        return 'Tarjeta Amex'

    def clone(self):
        return copy(self)
