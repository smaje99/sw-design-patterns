from comportamiento.memento.example_1.memento import ArticleMemento


class Caretaker:
    def __init__(self):
        self.__list = []

    def add_memento(self, memento: ArticleMemento):
        self.__list.append(memento)

    def get_memento(self, index: int) -> ArticleMemento:
        return self.__list[index]
