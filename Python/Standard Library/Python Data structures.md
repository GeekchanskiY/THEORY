
## List
### Using list as queue
```python
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
# -> 'Eric'
queue.popleft()                 # The second to arrive now leaves
# -> 'John'
queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
```

### Using list as stack
```python
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack.pop()
```

### Tuples and sequences
Packing and unpacking
```python
a, b, c = 123, 342, 321
# Unpacks variables
```

Creating tuple could be easy
```python
a = 1, 2, 3
b = 1, # <- Comma at the end says interpreter that it's a tuple
```

Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking (see later in this section) or indexing (or even by attribute in the case of namedtuples). Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list. Though tuples may seem similar to lists, they are often used in different situations and for different purposes.

### Sets
Curly braces or the set() function can be used to create sets.
!!! Note: to create an empty set you have to use set(), not {}; the latter creates an empty dictionary, a data structure that we discuss in the next section.
!!! Note, creating set() will use each variable as iterable, and it can cause string to be unpacked as `{'h', 'e', 'l', 'l', 'o'}`

### Dicts
Another useful data type built into Python is the _dictionary_ (see [Mapping Types — dict](https://docs.python.org/3/library/stdtypes.html#typesmapping)). Dictionaries are sometimes found in other languages as “associative memories” or “associative arrays”. Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by _keys_, which can be any immutable type; strings and numbers can always be keys. Tuples can be used as keys if they contain only strings, numbers, or tuples; if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key. You can’t use lists as keys, since lists can be modified in place using index assignments, slice assignments, or methods like `append()` and `extend()`.

Performing list(d) on a dictionary returns a list of all the keys used in the dictionary, in insertion order (if you want it sorted, just use sorted(d) instead). To check whether a single key is in the dictionary, use the `in` keyword.

The dict() constructor builds dictionaries directly from sequences of key-value pairs:
```python 
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
```

In addition, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:
```python
{x: x**2 for x in (2, 4, 6)}
# {2: 4, 4: 16, 6: 36}
```
