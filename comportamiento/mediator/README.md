# Mediator Pattern

```
@startuml
'https://plantuml.com/class-diagram

interface Mediator
interface Colleague
class ConcreteMediator
class ConcreteColleague1
class ConcreteColleague2

Mediator <|.up. ConcreteMediator
Colleague <|.. ConcreteColleague1
Colleague <|.. ConcreteColleague2
ConcreteColleague1 <-- ConcreteMediator
ConcreteColleague2 <-- ConcreteMediator

@enduml
```
