from target import Payment
from adapter import Adapter


class CreditCard(Payment):
    def pay(self, type: str):
        if type == 'classic':
            print('Tarjeta Classic: Pagando sin ningún tipo de Seguridad')
        elif type in ('gold', 'black'):
            Adapter().pay(type)
        else:
            raise TypeError('card type value unknown')
