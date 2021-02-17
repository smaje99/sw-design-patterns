from creacionales.abstract_factory.abstract_product import Card, PaymentMethod


class Visa(Card):
    def card_type(self) -> str:
        return 'VISA'

    def card_number(self) -> str:
        return f'{"0000 " * 3}VISA'


class MasterCard(Card):
    def card_type(self) -> str:
        return 'MASTERCARD'

    def card_number(self) -> str:
        return f'{"0000 " * 2}MAST CARD'


class Debit(PaymentMethod):
    def do_payment(self) -> str:
        return 'Pago a Débito'


class Credit(PaymentMethod):
    def do_payment(self) -> str:
        return 'Pago a Crédito'
