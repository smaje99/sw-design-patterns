class Semaforo:
    def __init__(self, status: str):
        self.__status = status

    @property
    def status(self) -> str:
        return self.__status
