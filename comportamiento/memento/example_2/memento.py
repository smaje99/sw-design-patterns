from copy import copy


class Memento:
    def __init__(self, state):
        self.__state = state

    @property
    def state(self):
        return copy(self.__state)


class Caretaker:
    def __init__(self):
        self.__mementos = []

    def add_memento(self, memento: Memento):
        self.__mementos.append(memento)

    def get_memento(self, n: int) -> Memento:
        return self.__mementos[n]

    def first_memento(self) -> Memento:
        return self.__mementos[0]

    def last_memento(self) -> Memento:
        return self.__mementos[-1]
