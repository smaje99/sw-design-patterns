from product import Payment
from enum import Enum, unique


class GooglePayment(Payment):
    def do_payment(self):
        return 'Pagando con Google Payment'


class CardPayment(Payment):
    def do_payment(self):
        return 'Pagando con Tarjeta de Crédito'


@unique
class TypePayment(Enum):
    """ unique evitará que se dupliquen valores """
    CARD = 'card',
    GOOGLE_PAY = 'google'
