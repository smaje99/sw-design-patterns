from receiver import CreditCard
from concrete_command import CreditCardActivateCommand, CreditCardDeactivateCommand
from invoker import CreditCardInvoker

def main():
    credit_card = CreditCard()
    credit_card_deactivate = CreditCard()

    invoker = CreditCardInvoker()
    invoker.set_command(CreditCardActivateCommand(credit_card))
    print(invoker.run())

    invoker.set_command(CreditCardDeactivateCommand(credit_card_deactivate))
    print(invoker.run())



if __name__ == '__main__':
    main()
