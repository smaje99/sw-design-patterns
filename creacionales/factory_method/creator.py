from product import Payment
from concrete_product import TypePayment, CardPayment, GooglePayment


class PaymentFactory:
    @classmethod
    def build_payment(cls, type_payment: TypePayment) -> Payment:
        if type_payment == TypePayment.CARD:
            return CardPayment()
        elif type_payment == TypePayment.GOOGLE_PAY:
            return GooglePayment()
        else:
            raise TypeError("Tipo de pago no correcto")


