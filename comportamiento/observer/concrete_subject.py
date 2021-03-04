from comportamiento.observer.data import Semaforo
from comportamiento.observer.observer import Observer
from comportamiento.observer.subject import Subject


class MessagePublisher(Subject):
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify_all(self, semaforo: Semaforo):
        for observer in self._observers:
            observer.update(semaforo)

