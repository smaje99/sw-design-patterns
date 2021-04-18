from abc import ABC, abstractmethod


class Payment(ABC):
    def make_payment(self):
        self.initialize()
        self.start_payment()
        self.end_payment()

    @abstractmethod
    def initialize(self):
        """Inicializa el servidor de pago
        """
        pass

    @abstractmethod
    def start_payment(self):
        """Inicia el pago
        """
        pass

    @abstractmethod
    def end_payment(self):
        """Finaliza el pago
        """
        pass
