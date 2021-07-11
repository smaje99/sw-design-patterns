# Iterator Pattern

```
@startuml
'https://plantuml.com/class-diagram

interface Iterator {
    + next()
    + hasNext()
}
interface Aggregate {
    + iterator()
}
class ConcreteIterator
class ConcreteAggregate

Iterator <|.. ConcreteIterator
Aggregate <|.. ConcreteAggregate
Iterator <.left. Aggregate: <<create>>
ConcreteIterator <.. ConcreteAggregate: <<create>>
ConcreteIterator o-- ConcreteAggregate

@enduml
```
