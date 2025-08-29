Uvicorn is an ASGI web server implementation for Python.

Until recently Python has lacked a minimal low-level server/application interface for async frameworks. The [ASGI specification](https://asgi.readthedocs.io/en/latest/) fills this gap, and means we're now able to start building a common set of tooling usable across all async frameworks.

Uvicorn currently supports **HTTP/1.1** and **WebSockets**.

Install using `pip`:

`pip install uvicorn`

This will install uvicorn with minimal (pure Python) dependencies.

`pip install 'uvicorn[standard]'`

This will install uvicorn with "Cython-based" dependencies (where possible) and other "optional extras".

In this context, "Cython-based" means the following:

- the event loop `uvloop` will be installed and used if possible.
- `uvloop` is a fast, drop-in replacement of the built-in asyncio event loop. It is implemented in Cython. Read more [here](https://uvloop.readthedocs.io/).
- The built-in asyncio event loop serves as an easy-to-read reference implementation and is there for easy debugging as it's pure-python based.
- the http protocol will be handled by `httptools` if possible.