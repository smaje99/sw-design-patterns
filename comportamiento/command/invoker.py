from command import Command


class CreditCardInvoker:
    def __init__(self):
        self.__command: Command = None

    def set_command(self, command):
        self.__command = command

    def run(self) -> str:
        return self.__command.execute()
