from implementor import ICreditCard


class UnsecureCreditCard(ICreditCard):
    def make_payment(self):
        print('Pago realizado SIN SEGURIDAD')


class SecureCreditCard(ICreditCard):
    def make_payment(self):
        print('Pago realizado CON SEGURIDAD')
