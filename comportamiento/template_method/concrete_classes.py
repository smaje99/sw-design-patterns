from abstract_class import Payment


class Paypal(Payment):
    def initialize(self):
        print('Inicializando el pago con Paypal...')

    def start_payment(self):
        print('Realizando el pago con Paypal...')

    def end_payment(self):
        print('Finalizado el pago por medio de Paypal.')


class Visa(Payment):
    def initialize(self):
        print('Inicializando el pago con Visa...')

    def start_payment(self):
        print('Realizando el pago con Visa...')

    def end_payment(self):
        print('Finalizado el pago por medio de Visa.')
