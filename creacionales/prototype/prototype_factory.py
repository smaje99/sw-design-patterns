from enum import Enum

from typing import Dict

from creacionales.prototype.prototype import PrototypeCard
from creacionales.prototype.concrete_prototype import Visa, Amex


class CardType(Enum):
    VISA = 'visa'
    AMEX = 'amex'


__prototypes: Dict[CardType, PrototypeCard] = dict()

def load_card():
    global __prototypes
    if not __prototypes:
        visa = Visa()
        visa.name = 'Tarjeta Visa con número 0000'
        __prototypes[CardType.VISA] = visa

        amex = Amex()
        amex.name = 'Tarjeta Amex con número 0000'
        __prototypes[CardType.AMEX] = amex

def get_instance(type: CardType) -> PrototypeCard:
    global __prototypes
    return __prototypes.get(type, 'Undefined value').clone()
