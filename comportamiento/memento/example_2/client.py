from memento import *


class Person:
    def __init__(self, name: str, age: int, feel: str):
        self.name = name
        self.age = age
        self.feel = feel

    def create_memento(self) -> Memento:
        return Memento(self.feel)

    def restore_memento(self, memento: Memento):
        self.feel = memento.state

    def __str__(self):
        return f'{self.name} is {self.feel}'


if __name__ == '__main__':
    mementos = Caretaker()
    feels = ['Fine', 'Good', 'Bad']

    john = Person('John', 23, feels[1])

    mementos.add_memento(john.create_memento())
    john.feel = feels[0]

    print(john)
    print(mementos.last_memento().state)

