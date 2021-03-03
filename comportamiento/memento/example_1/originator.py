from comportamiento.memento.example_1.memento import ArticleMemento


class Article:
    def __init__(self, author, text):
        self.__author = author
        self.text = text

    def create_memento(self) -> ArticleMemento:
        return ArticleMemento(self.text)

    def restore_memento(self, memento: ArticleMemento):
        self.text = memento.state

    @property
    def author(self):
        return self.__author
