from abc import ABC, abstractmethod


class Internet(ABC):
    @abstractmethod
    def connect_to(self, url: str): pass
