[[Design Patterns]]

They used to create new instances, which can be previously specified, or just an abstract objects. Abstract the process of instantiation. They make it possible to make the system independent of the method of creating, composing and presenting objects. The template that generates classes uses inheritance to modify the class being instantiated, while the template that generates objects delegates the instantiation to another object.

<p style='font-size: 32px; font-weight: bold;'> Abstract Factory </p>
**Abstract Factory** is a creational design pattern that lets you produce families of related objects without specifying their concrete classes.

Detail info: https://refactoring.guru/design-patterns/abstract-factory

UML:
![[AbstactFactory.png]]
1.  **Abstract Products** declare interfaces for a set of distinct but related products which make up a product family.
    
2.  **Concrete Products** are various implementations of abstract products, grouped by variants. Each abstract product (chair/sofa) must be implemented in all given variants (Victorian/Modern).
    
3.  The **Abstract Factory** interface declares a set of methods for creating each of the abstract products.
    
4.  **Concrete Factories** implement creation methods of the abstract factory. Each concrete factory corresponds to a specific variant of products and creates only those product variants.
    
5.  Although concrete factories instantiate concrete products, signatures of their creation methods must return corresponding _abstract_ products. This way the client code that uses a factory doesn’t get coupled to the specific variant of the product it gets from a factory. The **Client** can work with any concrete factory/product variant, as long as it communicates with their objects via abstract interfaces.



<p style='font-size: 32px; font-weight: bold;'> Builder </p>
**Builder** is a creational design pattern that lets you construct complex objects step by step. The pattern allows you to produce different types and representations of an object using the same construction code.

Detail info: https://refactoring.guru/design-patterns/builder

UML:
![[Builder.png]]
1.  The **Builder** interface declares product construction steps that are common to all types of builders.
    
2.  **Concrete Builders** provide different implementations of the construction steps. Concrete builders may produce products that don’t follow the common interface.
    
3.  **Products** are resulting objects. Products constructed by different builders don’t have to belong to the same class hierarchy or interface.
    
4.  The **Director** class defines the order in which to call construction steps, so you can create and reuse specific configurations of products.
    
5.  The **Client** must associate one of the builder objects with the director. Usually, it’s done just once, via parameters of the director’s constructor. Then the director uses that builder object for all further construction. However, there’s an alternative approach for when the client passes the builder object to the production method of the director. In this case, you can use a different builder each time you produce something with the director.
<p style='font-size: 32px; font-weight: bold;'> Factory Method </p>
also known as Virtual Constructor

**Factory Method** is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.

Detail info: https://refactoring.guru/design-patterns/factory-method

UML
![[Factory Method.png]]
1.  The **Product** declares the interface, which is common to all objects that can be produced by the creator and its subclasses.
    
2.  **Concrete Products** are different implementations of the product interface.
    
3.  The **Creator** class declares the factory method that returns new product objects. It’s important that the return type of this method matches the product interface.
    
    You can declare the factory method as `abstract` to force all subclasses to implement their own versions of the method. As an alternative, the base factory method can return some default product type.
    
    Note, despite its name, product creation is **not** the primary responsibility of the creator. Usually, the creator class already has some core business logic related to products. The factory method helps to decouple this logic from the concrete product classes. Here is an analogy: a large software development company can have a training department for programmers. However, the primary function of the company as a whole is still writing code, not producing programmers.
    
4.  **Concrete Creators** override the base factory method so it returns a different type of product.
    
    Note that the factory method doesn’t have to **create** new instances all the time. It can also return existing objects from a cache, an object pool, or another source.
<p style='font-size: 32px; font-weight: bold;'> Prototype </p>
**Prototype** is a creational design pattern that lets you copy existing objects without making your code dependent on their classes.

Detail info: https://refactoring.guru/design-patterns/prototype

UML:
![[Prototype.png]]
1.  The **Prototype Registry** provides an easy way to access frequently-used prototypes. It stores a set of pre-built objects that are ready to be copied. The simplest prototype registry is a `name → prototype` hash map. However, if you need better search criteria than a simple name, you can build a much more robust version of the registry.
<p style='font-size: 32px; font-weight: bold;'> Singleton </p>
**Singleton** is a creational design pattern that lets you ensure that a class has only one instance, while providing a global access point to this instance.

Detail info: https://refactoring.guru/design-patterns/singleton

UML:
![[Singleton.png]]
1.  The **Singleton** class declares the static method `getInstance` that returns the same instance of its own class.
    
    The Singleton’s constructor should be hidden from the client code. Calling the `getInstance` method should be the only way of getting the Singleton object.