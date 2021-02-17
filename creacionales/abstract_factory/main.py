from creacionales.abstract_factory.concrete_factory import FactoryProvider


def main():
    card = FactoryProvider.get_factory('Card').create('VISA')
    payment = FactoryProvider.get_factory('PaymentMethod').create('debit')

    print(f'Una tarjeta { card.card_type() } con el método de pago { payment.do_payment() }')


if __name__ == '__main__':
    main()
