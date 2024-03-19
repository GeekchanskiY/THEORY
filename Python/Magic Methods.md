[[Python]]


	`def __new__(cls)`
To get called in an object's instantiation.

	`def __init__(self) -> None`
To get called by the __new__ method.

	`def __del__(self)`
Destructor method.

	`def __repr__(self) -> str`
Representation of object. Called by `str()` if `__str__` is not implemented, and by `__repr__`

	`def __str__(self) -> str`
Used in `str()`

	`def __call__(self)`
Makes Instance a callable.

	`def __len__(self) -> int`
Used in `len()`

	`def __add__(self, other) -> any`
Used with `+` operator

	`def __sub__(self, other) -> any`
Used with `-` operator

	`def __mul__(self, other) -> any`
Used with `*` operator

	`def __truediv__(self, other) -> any`
Used with `/` operator

	`def __floordiv__(self, other) -> any`
Used with `//` operator

	`def __mod__(self, other) -> any`
Used with `%` operator

	`def __pow__(self, other) -> any`
Used with `**` operator

	`def __radd__(self, other) -> any`
Used with `+` operator, but when the instance is a right-hand

Same for all other `__arithmetic__` methods, e.g. `__rsub__`, `__rmul__`, `__rtruediv__`, `__rfloordiv__`, `__rmod__`, `__rpow__`