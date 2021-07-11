# Facade Pattern

```
@startuml
'https://plantuml.com/class-diagram

class Facade
class ModuleA
class ModuleB
class ModuleC

ModuleA <-left- Facade
ModuleA <-- ModuleB
ModuleA <-- ModuleC

ModuleB <-left- Facade
ModuleB <-right- ModuleA
ModuleB <-down- ModuleC

ModuleC <-left- Facade
ModuleC <-right- ModuleA
ModuleC <-- ModuleB

@enduml
```
