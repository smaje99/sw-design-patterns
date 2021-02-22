from abc import ABC, abstractmethod


class ApproveLoanChain(ABC):
    def __init__(self):
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, loan):
        self.__next = loan

    @abstractmethod
    def credit_card_request(self, total_loan: int) -> str: pass
