from abc import ABC, abstractmethod


class Expression(ABC):
    @abstractmethod
    def interpret(self, context: str) -> bool: pass
