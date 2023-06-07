[[Design Patterns]]

They used to create new instances, which can be previously specified, or just an abstract objects. Abstract the process of instantiation. They make it possible to make the system independent of the method of creating, composing and presenting objects. The template that generates classes uses inheritance to modify the class being instantiated, while the template that generates objects delegates the instantiation to another object.

<p style='font-size: 32px; font-weight: bold;'> Abstract Factory </p>
**Abstract Factory** is a creational design pattern that lets you produce families of related objects without specifying their concrete classes.

Detail info: https://refactoring.guru/design-patterns/abstract-factory

UML:
![[AbstactFactory.png]]


<p style='font-size: 32px; font-weight: bold;'> Builder </p>
**Builder** is a creational design pattern that lets you construct complex objects step by step. The pattern allows you to produce different types and representations of an object using the same construction code.

Detail info: https://refactoring.guru/design-patterns/builder

UML:
![[Builder.png]]
<p style='font-size: 32px; font-weight: bold;'> Factory Method </p>
also known as Virtual Constructor

**Factory Method** is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.

Detail info: https://refactoring.guru/design-patterns/factory-method

UML
![[Factory Method.png]]
<p style='font-size: 32px; font-weight: bold;'> Prototype </p>
**Prototype** is a creational design pattern that lets you copy existing objects without making your code dependent on their classes.

Detail info: https://refactoring.guru/design-patterns/prototype

UML:
![[Prototype.png]]
<p style='font-size: 32px; font-weight: bold;'> Singleton </p>
**Singleton** is a creational design pattern that lets you ensure that a class has only one instance, while providing a global access point to this instance.

Detail info: https://refactoring.guru/design-patterns/singleton

UML:
![[Singleton.png]]