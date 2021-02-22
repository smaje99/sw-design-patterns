from command import Command
from receiver import CreditCard

class CreditCardDeactivateCommand(Command):
    def __init__(self, credit_card: CreditCard):
        self.credit_card = credit_card

    def execute(self):
        return f'{self.credit_card.deactivate()}\n' \
               f'{self.credit_card.send_sms_to_customer_deactivate()}'


class CreditCardActivateCommand(Command):
    def __init__(self, credit_card: CreditCard):
        self.credit_card = credit_card

    def execute(self):
        return f'{self.credit_card.send_pin_number_to_customer()}\n' \
               f'{self.credit_card.activate()}\n' \
               f'{self.credit_card.send_sms_to_customer_activate()}'
