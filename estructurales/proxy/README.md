# Proxy

```
@startuml
'https://plantuml.com/class-diagram

class Client
interface Subject {
    doAction()
}
class Proxy {
    doAction()
}
class RealSubject {
    doAction()
}

Subject <.left. Client
RealSubject <-- Proxy: delegate

Subject <|.. Proxy
Subject <|.. RealSubject

@enduml
```
