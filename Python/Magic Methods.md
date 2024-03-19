[[Python]]


	`def __new__(cls)`
To get called in an object's instantiation.

	`def __init__(self)`
To get called by the __new__ method.

	`__def__(self)`
Destructor method.

	`def __repr__(self)`
Representation of object. Called by `str()` if `__str__` is not implemented, and by `__repr__`

	`def __str__(self)`
Used in `str()`