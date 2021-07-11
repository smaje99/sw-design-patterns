# Bridge Pattern

```
@startuml
'https://plantuml.com/class-diagram

interface Abstraction {
    + function()
}
interface Implementor {
    + implementation()
}
class RefinedAbstraction {
    + refinedFunction()
}
class ConcreteImplementor {
    + implementation()
}

note left of Abstraction::function
    this.implementor.implementation
end note

Abstraction o-right- Implementor: - implementor
Abstraction <|-- RefinedAbstraction
Implementor <|.. ConcreteImplementor

@enduml
```
