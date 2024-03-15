[Documentation](https://docs.pytest.org)

The `pytest` framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.

`pytest` will run all files of the form test_*.py or *_test.py in the current directory and its subdirectories. More generally, it follows standard test discovery rules

## Conventions for Python test discovery
`pytest` implements the following standard test discovery:

- If no arguments are specified then collection starts from `testpaths` (if configured) or the current directory. Alternatively, command line arguments can be used in any combination of directories, file names or node ids.
    
- Recurse into directories, unless they match `norecursedirs`.
    
- In those directories, search for `test_*.py` or `*_test.py` files, imported by their test package name.
    
- From those files, collect test items:
    
    - `test` prefixed test functions or methods outside of class.
        
    - `test` prefixed test functions or methods inside `Test` prefixed test classes (without an `__init__` method). Methods decorated with `@staticmethod` and `@classmethods` are also considered.
        

For examples of how to customize your test discovery Changing standard (Python) test discovery.

Within Python modules, `pytest` also discovers tests using the standard unittest.TestCase subclassing technique.


Test layouts:
 - Outside the app code 
 ```python 
pyproject.toml
src/
    mypkg/
        __init__.py
        app.py
        view.py
tests/
    test_app.py
    test_view.py
 ```
  - As a part of application code
```python
pyproject.toml
[src/]mypkg/
    __init__.py
    app.py
    view.py
    tests/
        __init__.py
        test_app.py
        test_view.py
```