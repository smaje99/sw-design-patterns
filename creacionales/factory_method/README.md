# Factory Method

```
@startuml
'https://plantuml.com/class-diagram

interface Creator {
    # factoryMethod(): Product
    + anOperation()
}

interface Product

class ConcreteCreator {
    + factoryMethod(): Product
}

class ConcreteProduct

Product <|-- ConcreteProduct
Creator <|-- ConcreteCreator
Product <.. Creator: <<use>>
ConcreteProduct <.. ConcreteCreator: <<create>>

@enduml
```
