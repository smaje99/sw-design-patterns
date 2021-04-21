from abc import ABC, abstractmethod


class Secure(ABC):
    @abstractmethod
    def pay_with_secure(self): pass


class GoldCreditCard(Secure):
    def pay_with_secure(self):
        print('Tarjeta Gold: Pagando con Seguridad BAJA nivel Z')


class BlackCreditCard(Secure):
    def pay_with_secure(self):
        print('Tarjeta Gold: Pagando con Seguridad ALTA nivel A')
