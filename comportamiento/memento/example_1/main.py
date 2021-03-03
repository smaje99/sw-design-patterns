from comportamiento.memento.example_1.caretaker import Caretaker
from comportamiento.memento.example_1.originator import Article


def main():
    caretaker = Caretaker()
    article = Article('Alberto', 'Memento es una película')
    article.text += ' de Nolan'
    print(article.text)

    caretaker.add_memento(article.create_memento())
    article.text += ', protagonizada por Guy Pearce'
    print(article.text)

    caretaker.add_memento(article.create_memento())
    article.text += ' y Leonardo DiCaprio'
    print(article.text)

    article.restore_memento(caretaker.get_memento(1))
    print(article.text)

    article.restore_memento(caretaker.get_memento(0))
    article.text += ' del año 2000'
    print(article.text)


if __name__ == '__main__':
    main()
