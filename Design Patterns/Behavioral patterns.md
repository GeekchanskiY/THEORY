[[Design Patterns]]

They used to define the interaction between objects, increasing the flexibility

<p style='font-size: 32px; font-weight: bold;'> Chain of Responsibility </p>
**Chain of Responsibility** is a behavioral design pattern that lets you pass requests along a chain of handlers. Upon receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain.

Detail info: https://refactoring.guru/design-patterns/chain-of-responsibility

UML:
![[ChainOfResponsibility.png]]
<p style='font-size: 32px; font-weight: bold;'> Command </p>
**Command** is a behavioral design pattern that turns a request into a stand-alone object that contains all information about the request. This transformation lets you pass requests as a method arguments, delay or queue a request’s execution, and support undoable operations.

Detail info: https://refactoring.guru/design-patterns/command 

UML:
![[Command.png]]

<p style='font-size: 32px; font-weight: bold;'> Iterator </p>
**Iterator** is a behavioral design pattern that lets you traverse elements of a collection without exposing its underlying representation (list, stack, tree, etc.).

Detail info: https://refactoring.guru/design-patterns/iterator

UML:
![[Iterator.png]]


<p style='font-size: 32px; font-weight: bold;'> Mediator </p>
**Mediator** is a behavioral design pattern that lets you reduce chaotic dependencies between objects. The pattern restricts direct communications between the objects and forces them to collaborate only via a mediator object.

Detail info: https://refactoring.guru/design-patterns/mediator

UML:
![[Mediator.png]]
<p style='font-size: 32px; font-weight: bold;'> Memento </p>
**Memento** is a behavioral design pattern that lets you save and restore the previous state of an object without revealing the details of its implementation.

Detail info: https://refactoring.guru/design-patterns/memento

UML:
![[Memento.png]]
1. The **Originator** class can produce snapshots of its own state, as well as restore its state from snapshots when needed.
2.  The **Memento** is a value object that acts as a snapshot of the originator’s state. It’s a common practice to make the memento immutable and pass it the data only once, via the constructor.
3.  The **Caretaker** knows not only “when” and “why” to capture the originator’s state, but also when the state should be restored.
    A caretaker can keep track of the originator’s history by storing a stack of mementos. When the originator has to travel back in history, the caretaker fetches the topmost memento from the stack and passes it to the originator’s restoration method.
4.  In this implementation, the memento class is nested inside the originator. This lets the originator access the fields and methods of the memento, even though they’re declared private. On the other hand, the caretaker has very limited access to the memento’s fields and methods, which lets it store mementos in a stack but not tamper with their state.
<p style='font-size: 32px; font-weight: bold;'> Observer </p>
**Observer** is a behavioral design pattern that lets you define a subscription mechanism to notify multiple objects about any events that happen to the object they’re observing.

Detail info: https://refactoring.guru/design-patterns/observer

UML:
![[Observer.png]]

<p style='font-size: 32px; font-weight: bold;'> State </p>

<p style='font-size: 32px; font-weight: bold;'> Strategy </p>

<p style='font-size: 32px; font-weight: bold;'> Template method </p>

<p style='font-size: 32px; font-weight: bold;'> Visitor </p>

