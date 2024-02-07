
### What is the difference between a class and a module?

Modules are collections of methods and constants. They cannot generate instances. Classes may generate instances (objects), and have per-instance state (instance variables).

Modules may be mixed in to classes and other modules. The mixed in module’s constants and methods blend into that class’s own, augmenting the class’s functionality. Classes, however, cannot be mixed in to anything.

A class may inherit from another class, but ***not from a module***.

A module may not inherit from anything.

```ruby
module MyModule
  CONSTANT = 42

  def self.module_method
    puts "This is a module method"
  end

  class MyClass
    def class_method
      puts "This is a class method"
    end
  end
end
```