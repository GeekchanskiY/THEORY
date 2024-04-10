An ORM, or **Object Relational Mapper**, is a piece of software designed to translate between the data representations used by databases and those used in object-oriented programming.  Provides an object-oriented layer between relational databases and object-oriented programming languages without having to write SQL queries. It standardizes interfaces reducing boilerplate and speeding development time.


### Types of ORM's
ORMs employ two different strategies: active record pattern and data-mapper pattern.

#### Active record pattern
This strategy maps data within the structure of objects in the code. You manage data using classes and structures within your programming code. This method has problems since the database structure is tightly connected to the code, making it difficult to remove the database and migrate it to a different application.

#### Data-mapper patterns
The data-mapper pattern attempts to decouple the business logic in the objects from the database. This separation can make it easier to change databases and use the same programming logic.
