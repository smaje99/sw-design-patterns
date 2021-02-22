from colleague import Colleague
from mediator import Mediator


class ConcreteColleague1(Colleague):
    def __init__(self, mediator: Mediator):
        super().__init__(mediator)

    def send(self, message: str) -> str:
        return self.mediator.send(message, self)

    def message_received(self, message: str) -> str:
        return f'Colleague 1 ha recibido el siguiente mensaje: {message}'


class ConcreteColleague2(Colleague):
    def __init__(self, mediator: Mediator):
        super().__init__(mediator)

    def send(self, message: str) -> str:
        return self.mediator.send(message, self)

    def message_received(self, message: str) -> str:
        return f'Colleague 2 ha recibido el siguiente mensaje: {message}'
