class Card:
    __instance = dict()

    def __init__(self):
        self.__dict__ = self.__instance
        self.card_number = None
