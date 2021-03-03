import copy


class ArticleMemento:
    def __init__(self, state: str):
        self.__state = state

    @property
    def state(self) -> str:
        return copy.copy(self.__state)
