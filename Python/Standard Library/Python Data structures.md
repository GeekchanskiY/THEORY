
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


### Looping techniques
When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the `items()` method.

When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the `enumerate()` function.

To loop over two or more sequences at the same time, the entries can be paired with the `zip()` function.

To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the `reversed()` function.

To loop over a sequence in sorted order, use the `sorted()` function which returns a new sorted list while leaving the source unaltered.

!!! Note: Using `set()` on a sequence eliminates duplicate elements. The use of sorted() in combination with set() over a sequence is an idiomatic way to loop over unique elements of the sequence in sorted order.

It is sometimes tempting to change a list while you are looping over it; however, it is often simpler and safer to create a new list instead.

### Comparing Sequences and Other Types
Sequence objects typically may be compared to other objects with the same sequence type. The comparison uses lexicographical ordering: first the first two items are compared, and if they differ this determines the outcome of the comparison; if they are equal, the next two items are compared, and so on, until either sequence is exhausted. If two items to be compared are themselves sequences of the same type, the lexicographical comparison is carried out recursively. If all items of two sequences compare equal, the sequences are considered equal. If one sequence is an initial sub-sequence of the other, the shorter sequence is the smaller (lesser) one. Lexicographical ordering for strings uses the Unicode code point number to order individual characters. Some examples of comparisons between sequences of the same type:
```python 
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
```

Note that comparing objects of different types with < or > is legal provided that the objects have appropriate comparison methods. For example, mixed numeric types are compared according to their numeric value, so 0 equals 0.0, etc. Otherwise, rather than providing an arbitrary ordering, the interpreter will raise a TypeError exception.

