class CreditCard:
    def send_pin_number_to_customer(self) -> str:
        return 'El pin number ha sido enviado al cliente.'

    def send_sms_to_customer_activate(self) -> str:
        return 'Enviado SMS al cliente informando que su tarjeta ha sido activada. ' \
               'Ponte en contacto si no la has recibido.'

    def activate(self) -> str:
        return 'La tarjeta ha sido activada.'

    def deactivate(self) -> str:
        return 'La tarjeta ha sido desactivada.'

    def send_sms_to_customer_deactivate(self) -> str:
        return 'Enviando SMS al cliente informando que su tarjeta ha sido desactivada.'
