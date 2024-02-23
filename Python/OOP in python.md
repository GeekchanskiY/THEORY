
## Decorators
	- @final: says that object cant be inherited
	- @staticmethod: does not requires to get instance passed by
	- @classmethod: requires to get class reference as the first arg
	- @override: to indicate that a subclass method should override a superclass method

### Python interfaces:

To create python interface we can use:
	- Bare class 
	- using metaclesses:
```python
class ParserMeta(type):
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and 
                callable(subclass.load_data_source) and 
                hasattr(subclass, 'extract_text') and 
                callable(subclass.extract_text))

class UpdatedInformalParserInterface(metaclass=ParserMeta):
    pass
```

```python
issubclass(PdfParser, InformalParserInterface)
# -> bool
PdfParser.__mro__
# -> set of parents

```