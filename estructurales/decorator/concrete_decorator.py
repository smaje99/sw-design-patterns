from decorator import CreditDecorator
from component import Credit


class InternationalPaymentDecorator(CreditDecorator):
    def __init__(self, credit: Credit):
        super().__init__(credit)

    def show_credit(self) -> str:
        return self._credit.show_credit() + '\n' + \
                self.config_international_payment()

    def config_international_payment(self) -> str:
        return 'La tarjeta ha sido configurada para hacer pagos internacionales'


class SecureDecorator(CreditDecorator):
    def __init__(self, credit: Credit):
        super().__init__(credit)

    def show_credit(self) -> str:
        return self._credit.show_credit() + '\n' + \
                self.config_secure()

    def config_secure(self) -> str:
        return 'La tarjeta ha sido configurada con Seguridad Máxima'
