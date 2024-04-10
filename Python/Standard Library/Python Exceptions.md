Errors in python are being divided into 2 groups: Syntax errors, and exceptions

Syntax errors, also known as parsing errors, are perhaps the most common kind of complaint you get while you are still learning Python

Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it. Errors detected during execution are called _exceptions_ and are not unconditionally fatal: you will soon learn how to handle them in Python programs. Most exceptions are not handled by programs, however, and result in error messages

Features about exceptions:

### Exception groups
The builtin ExceptionGroup wraps a list of exception instances so that they can be raised together. It is an exception itself, so it can be caught like any other exception.
```python
def f():
    excs = [OSError('error 1'), SystemError('error 2')]
    raise ExceptionGroup('there were problems', excs)

f()

'''
  + Exception Group Traceback (most recent call last):
  |   File "<stdin>", line 1, in <module>
  |   File "<stdin>", line 3, in f
  | ExceptionGroup: there were problems
  +-+---------------- 1 ----------------
    | OSError: error 1
    +---------------- 2 ----------------
    | SystemError: error 2
    +------------------------------------
'''
```

### Enriching Exceptions with Notes
We can use Exception.add_note(str) to extend it's traceback
```python
try:
    raise TypeError('bad type')
except Exception as e:
    e.add_note('Add some information')
    raise


'''
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: bad type
Add some information
Add some more information
'''
```