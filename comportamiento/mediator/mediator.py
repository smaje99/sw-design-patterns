from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def send(self, message: str, colleague): pass
