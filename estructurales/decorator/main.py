from concrete_component import Black, Gold
from concrete_decorator import SecureDecorator, InternationalPaymentDecorator


def main():
    gold = Gold()
    black_international_payment = InternationalPaymentDecorator(Black())
    gold_secure_international = SecureDecorator(InternationalPaymentDecorator(Gold()))

    print(f'--- Tarjeta Gold sin configuración ---\n{gold.show_credit()}\n')
    print(f'--- Tarjeta Black con configuración ---\n{black_international_payment.show_credit()}\n')
    print(f'--- Tarjeta Gold con configuración ---\n{gold_secure_international.show_credit()}\n')


if __name__ == '__main__':
    main()
