from comportamiento.mediator.colleague import Colleague
from mediator import Mediator
from concrete_colleague import ConcreteColleague1, ConcreteColleague2


class ConcreteMediator(Mediator):
    def __init__(self):
        self.__user1: ConcreteColleague1 = None
        self.__user2: ConcreteColleague2 = None
        
    @property
    def user1(self):
        return self.__user1
    
    @user1.setter
    def user1(self, user1: ConcreteColleague1):
        self.__user1 = user1

    @property
    def user2(self):
        return self.__user2

    @user2.setter
    def user2(self, user2: ConcreteColleague2):
        self.__user2 = user2
    
    def send(self, message: str, colleague: Colleague) -> str:
        if colleague == self.user1:
            return self.__user2.message_received(message)
        elif colleague == self.__user2:
            return self.__user1.message_received(message)
