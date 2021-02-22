from abc import ABC, abstractmethod

from mediator import Mediator

class Colleague(ABC):
    def __init__(self, mediator: Mediator):
        self.mediator = mediator

    @abstractmethod
    def send(self, message: str): pass

    @abstractmethod
    def message_received(self, message: str) -> str: pass
