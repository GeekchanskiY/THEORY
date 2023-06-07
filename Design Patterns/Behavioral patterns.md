[[Design Patterns]]

They used to define the interaction between objects, increasing the flexibility

<p style='font-size: 32px; font-weight: bold;'> Chain of Responsibility </p>
**Chain of Responsibility** is a behavioral design pattern that lets you pass requests along a chain of handlers. Upon receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain.

Detail info: https://refactoring.guru/design-patterns/chain-of-responsibility

UML:
![[ChainOfResponsibility.png]]
1.  The **Handler** declares the interface, common for all concrete handlers. It usually contains just a single method for handling requests, but sometimes it may also have another method for setting the next handler on the chain.
    
2.  The **Base Handler** is an optional class where you can put the boilerplate code that’s common to all handler classes.
    
    Usually, this class defines a field for storing a reference to the next handler. The clients can build a chain by passing a handler to the constructor or setter of the previous handler. The class may also implement the default handling behavior: it can pass execution to the next handler after checking for its existence.
    
3.  **Concrete Handlers** contain the actual code for processing requests. Upon receiving a request, each handler must decide whether to process it and, additionally, whether to pass it along the chain.
    
    Handlers are usually self-contained and immutable, accepting all necessary data just once via the constructor.
    
4.  The **Client** may compose chains just once or compose them dynamically, depending on the application’s logic. Note that a request can be sent to any handler in the chain—it doesn’t have to be the first one.
<p style='font-size: 32px; font-weight: bold;'> Command </p>
**Command** is a behavioral design pattern that turns a request into a stand-alone object that contains all information about the request. This transformation lets you pass requests as a method arguments, delay or queue a request’s execution, and support undoable operations.

Detail info: https://refactoring.guru/design-patterns/command 

UML:
![[Command.png]]
1.  The **Sender** class (aka _invoker_) is responsible for initiating requests. This class must have a field for storing a reference to a command object. The sender triggers that command instead of sending the request directly to the receiver. Note that the sender isn’t responsible for creating the command object. Usually, it gets a pre-created command from the client via the constructor.
    
2.  The **Command** interface usually declares just a single method for executing the command.
    
3.  **Concrete Commands** implement various kinds of requests. A concrete command isn’t supposed to perform the work on its own, but rather to pass the call to one of the business logic objects. However, for the sake of simplifying the code, these classes can be merged.
    
    Parameters required to execute a method on a receiving object can be declared as fields in the concrete command. You can make command objects immutable by only allowing the initialization of these fields via the constructor.
    
4.  The **Receiver** class contains some business logic. Almost any object may act as a receiver. Most commands only handle the details of how a request is passed to the receiver, while the receiver itself does the actual work.
    
5.  The **Client** creates and configures concrete command objects. The client must pass all of the request parameters, including a receiver instance, into the command’s constructor. After that, the resulting command may be associated with one or multiple senders.
<p style='font-size: 32px; font-weight: bold;'> Iterator </p>
**Iterator** is a behavioral design pattern that lets you traverse elements of a collection without exposing its underlying representation (list, stack, tree, etc.).

Detail info: https://refactoring.guru/design-patterns/iterator

UML:
![[Iterator.png]]
1.  The **Iterator** interface declares the operations required for traversing a collection: fetching the next element, retrieving the current position, restarting iteration, etc.
    
2.  **Concrete Iterators** implement specific algorithms for traversing a collection. The iterator object should track the traversal progress on its own. This allows several iterators to traverse the same collection independently of each other.
    
3.  The **Collection** interface declares one or multiple methods for getting iterators compatible with the collection. Note that the return type of the methods must be declared as the iterator interface so that the concrete collections can return various kinds of iterators.
    
4.  **Concrete Collections** return new instances of a particular concrete iterator class each time the client requests one. You might be wondering, where’s the rest of the collection’s code? Don’t worry, it should be in the same class. It’s just that these details aren’t crucial to the actual pattern, so we’re omitting them.
    
5.  The **Client** works with both collections and iterators via their interfaces. This way the client isn’t coupled to concrete classes, allowing you to use various collections and iterators with the same client code.


<p style='font-size: 32px; font-weight: bold;'> Mediator </p>
**Mediator** is a behavioral design pattern that lets you reduce chaotic dependencies between objects. The pattern restricts direct communications between the objects and forces them to collaborate only via a mediator object.

Detail info: https://refactoring.guru/design-patterns/mediator

UML:
![[Mediator.png]]
1.  **Components** are various classes that contain some business logic. Each component has a reference to a mediator, declared with the type of the mediator interface. The component isn’t aware of the actual class of the mediator, so you can reuse the component in other programs by linking it to a different mediator.
    
2.  The **Mediator** interface declares methods of communication with components, which usually include just a single notification method. Components may pass any context as arguments of this method, including their own objects, but only in such a way that no coupling occurs between a receiving component and the sender’s class.
    
3.  **Concrete Mediators** encapsulate relations between various components. Concrete mediators often keep references to all components they manage and sometimes even manage their lifecycle.
    
4.  Components must not be aware of other components. If something important happens within or to a component, it must only notify the mediator. When the mediator receives the notification, it can easily identify the sender, which might be just enough to decide what component should be triggered in return.
    
    From a component’s perspective, it all looks like a total black box. The sender doesn’t know who’ll end up handling its request, and the receiver doesn’t know who sent the request in the first place.
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
1.  The **Publisher** issues events of interest to other objects. These events occur when the publisher changes its state or executes some behaviors. Publishers contain a subscription infrastructure that lets new subscribers join and current subscribers leave the list.
    
2.  When a new event happens, the publisher goes over the subscription list and calls the notification method declared in the subscriber interface on each subscriber object.
    
3.  The **Subscriber** interface declares the notification interface. In most cases, it consists of a single `update` method. The method may have several parameters that let the publisher pass some event details along with the update.
    
4.  **Concrete Subscribers** perform some actions in response to notifications issued by the publisher. All of these classes must implement the same interface so the publisher isn’t coupled to concrete classes.
    
5.  Usually, subscribers need some contextual information to handle the update correctly. For this reason, publishers often pass some context data as arguments of the notification method. The publisher can pass itself as an argument, letting subscriber fetch any required data directly.
    
6.  The **Client** creates publisher and subscriber objects separately and then registers subscribers for publisher updates.
<p style='font-size: 32px; font-weight: bold;'> State </p>
**State** is a behavioral design pattern that lets an object alter its behavior when its internal state changes. It appears as if the object changed its class.

Detail info: https://refactoring.guru/design-patterns/state

UML:
![[State.png]]
1.  **Context** stores a reference to one of the concrete state objects and delegates to it all state-specific work. The context communicates with the state object via the state interface. The context exposes a setter for passing it a new state object.
    
2.  The **State** interface declares the state-specific methods. These methods should make sense for all concrete states because you don’t want some of your states to have useless methods that will never be called.
    
3.  **Concrete States** provide their own implementations for the state-specific methods. To avoid duplication of similar code across multiple states, you may provide intermediate abstract classes that encapsulate some common behavior.
    
    State objects may store a backreference to the context object. Through this reference, the state can fetch any required info from the context object, as well as initiate state transitions.
    
4.  Both context and concrete states can set the next state of the context and perform the actual state transition by replacing the state object linked to the context.
<p style='font-size: 32px; font-weight: bold;'> Strategy </p>
**Strategy** is a behavioral design pattern that lets you define a family of algorithms, put each of them into a separate class, and make their objects interchangeable.

Detail info: https://refactoring.guru/design-patterns/strategy

UML:
![[Strategy.png]]

1.  The **Context** maintains a reference to one of the concrete strategies and communicates with this object only via the strategy interface.
    
2.  The **Strategy** interface is common to all concrete strategies. It declares a method the context uses to execute a strategy.
    
3.  **Concrete Strategies** implement different variations of an algorithm the context uses.
    
4.  The context calls the execution method on the linked strategy object each time it needs to run the algorithm. The context doesn’t know what type of strategy it works with or how the algorithm is executed.
    
5.  The **Client** creates a specific strategy object and passes it to the context. The context exposes a setter which lets clients replace the strategy associated with the context at runtime.
<p style='font-size: 32px; font-weight: bold;'> Template method </p>
**Template Method** is a behavioral design pattern that defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps of the algorithm without changing its structure.

Detail info: https://refactoring.guru/design-patterns/template-method

UML:
![[TemplateMethod.png]]
1.  The **Abstract Class** declares methods that act as steps of an algorithm, as well as the actual template method which calls these methods in a specific order. The steps may either be declared `abstract` or have some default implementation.
    
2.  **Concrete Classes** can override all of the steps, but not the template method itself.
<p style='font-size: 32px; font-weight: bold;'> Visitor </p>

**Visitor** is a behavioral design pattern that lets you separate algorithms from the objects on which they operate.

Detail info: https://refactoring.guru/design-patterns/visitor

![[Visitor.png]]
1.  The **Visitor** interface declares a set of visiting methods that can take concrete elements of an object structure as arguments. These methods may have the same names if the program is written in a language that supports overloading, but the type of their parameters must be different.
    
2.  Each **Concrete Visitor** implements several versions of the same behaviors, tailored for different concrete element classes.
    
3.  The **Element** interface declares a method for “accepting” visitors. This method should have one parameter declared with the type of the visitor interface.
    
4.  Each **Concrete Element** must implement the acceptance method. The purpose of this method is to redirect the call to the proper visitor’s method corresponding to the current element class. Be aware that even if a base element class implements this method, all subclasses must still override this method in their own classes and call the appropriate method on the visitor object.
    
5.  The **Client** usually represents a collection or some other complex object (for example, a [Composite](https://refactoring.guru/design-patterns/composite) tree). Usually, clients aren’t aware of all the concrete element classes because they work with objects from that collection via some abstract interface.