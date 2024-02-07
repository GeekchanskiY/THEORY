
instance attributes:
@variable_name

Static (class) attributes:
@@variable_name
Or, using another way:
```
@instances = 0

  class << self
    attr_accessor :instances
  end

  def initialize
    self.class.instances += 1
    @number = self.class.instances
  end
```
