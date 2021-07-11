# Memento Pattern

```

@startuml
'https://plantuml.com/class-diagram

class Memento {
    - state
    + Memento(state)
    + getState()
}
note left of Memento::state
    objeto inmutable
end note
note left of Memento::getState
    return state.clone()
end note

class CareTaker {
    - mementos: Memento[]
    + addMemento(memento)
    + getMemento()
}

class Originator {
    - state
    + createMemento(): Memento
    + setMemento(memento)
}
note left of Originator::createMemento
    return new Memento(state)
end note

class Client

Client <.. CareTaker
Memento <.up. Originator
Originator <.right. Client
CareTaker o-left- Memento

@enduml
```
