from creacionales.abstract_factory.abstract_factory import AbstractFactory
from creacionales.abstract_factory.abstract_product import Card, PaymentMethod
from creacionales.abstract_factory.concrete_product import Visa, MasterCard, Credit, Debit


class CardFactory(AbstractFactory):
    def create(self, type: str) -> Card:
        if 'visa' == type.lower():
            return Visa()
        elif 'mastercard' == type.lower():
            return MasterCard()
        else:
            raise ValueError('Valor de tarjeta invalido')


class PaymentMethodFactory(AbstractFactory):
    def create(self, type: str) -> PaymentMethod:
        if 'credit' == type.lower():
            return Credit()
        elif 'debit' == type.lower():
            return Debit()
        else:
            raise ValueError('Valor de método de pago invalido')


class FactoryProvider:
    @classmethod
    def get_factory(cls, choose_factory: str) -> AbstractFactory:
        if 'card' == choose_factory.lower():
            return CardFactory()
        elif 'paymentmethod' == choose_factory.lower():
            return PaymentMethodFactory()
        else:
            raise ValueError('Valor de fabrica invalido')
