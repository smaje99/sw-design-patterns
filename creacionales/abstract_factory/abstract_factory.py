from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create(self, type: str) -> object: pass
