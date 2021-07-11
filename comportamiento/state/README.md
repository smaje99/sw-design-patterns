# State Pattern

```
@startuml
'https://plantuml.com/class-diagram

interface State {
    + handle()
}

class Context {
    + request()
}
note left of Context::request
    state.handle()
end note

class ConcreteStateA
class ConcreteStateB



Context o-right- State

State <|.. ConcreteStateA
State <|.. ConcreteStateB

@enduml
```
