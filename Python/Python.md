[[Python frameworks & Libs]]


### Python + Obsidian example
(To have a better experience install 'Execute code' plugin: https://github.com/twibiral/obsidian-execute-code)

```python {pre}
import random
```

```run-python
def magic_commands() -> None:
	print("Vault path:", @vault_path)
	print("Vault url:", @vault_url)
	
	print("Note path:", @note_path)
	print("Note url:", @note_url)
	
	print("Note title:", @title)

if __name__ == '__main__':
	print('hello, OBSIDIAN!')
	print(f'Today\'s number is: {random.randint(1, 100)}')
	magic_commands()
	
```

```python {post}
pass
```

### Descriptors

Descriptors let objects customize attribute lookup, storage, and deletion.

They use [[Magic Methods]] like: __ get __ , __ set __ , __ delete __

descr. __ get __ (self, obj, type=None) -> value
descr. __ set __ (self, obj, value) -> None
descr. __ delete __ (self, obj) -> None

```run-python
import os

class DirectorySize:

    def __get__(self, obj, objtype=None):
        return len(os.listdir(obj.dirname))

class Directory:

    size = DirectorySize()              # Descriptor instance

    def __init__(self, dirname):
        self.dirname = dirname          # Regular instance attribute
        
s = Directory(@vault_path)
print(f'Objects in the init directory: {s.size}')
```


## Python data types:
There are different types of data types in Python. Some built-in Python data types are:

- **Numeric data types**: _int, float, complex_

- **String data types**: _str_

- **Sequence types**: _list, tuple, range_

- **Binary types**: _bytes, bytearray, memoryview_

- **Mapping data type**: _dict_

- **Boolean type**: _bool_

- **Set data types**: _set, frozenset_