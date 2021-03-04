from abc import ABC, abstractmethod

from comportamiento.observer.data import Semaforo
from observer import Observer


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer): pass

    @abstractmethod
    def detach(self, observer: Observer): pass

    @abstractmethod
    def notify_all(self, semaforo: Semaforo): pass
