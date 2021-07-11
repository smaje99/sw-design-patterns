# Builder Pattern

```
@startuml
'https://plantuml.com/class-diagram

class Director {
    - builder: Builder
    + construct()
}

class Builder {
    + buildPart()
}

class ConcreteBuilder {
    + buildPart()
    + getResult(): Product
}

class Product

note right of Director::construct
    this.builder.buildPart()
end note

Director o-- Builder
Builder <|-- ConcreteBuilder
ConcreteBuilder .right.> Product: <<create>>

@enduml
```
