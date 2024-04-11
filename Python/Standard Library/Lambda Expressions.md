Small anonymous functions can be created with the lambda keyword.  Lambda functions can be used wherever function objects are required. They are syntactically restricted to a single expression. Semantically, they are just syntactic sugar for a normal function definition. Like nested function definitions, lambda functions can reference variables from the containing scope.
Example which will blow mind:

```python
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0)
# 42
f(1)
# 43

```