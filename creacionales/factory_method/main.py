from concrete_product import TypePayment
from creator import PaymentFactory
from product import Payment


def main():
    payment: Payment = PaymentFactory.build_payment(TypePayment.GOOGLE_PAY)
    print(payment.do_payment())


if __name__ == '__main__':
    main()