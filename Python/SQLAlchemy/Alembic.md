 [Alembic](https://alembic.sqlalchemy.org/) is a lightweight database migration tool for usage with the [SQLAlchemy](https://www.sqlalchemy.org/) Database Toolkit for Python.
#### Quickstart:
```bash 
alembic init alembic
```
In alembic.ini change sqlalchemy.url to db connection string
In alembic/env.py
```python
# Import Metadata or Base from SQLAlchemy database settings
from database import Base

# Apply metadata to alembic (replace stock target_metadata with this)
target_metadata = Base.metadata
```

useful commands:
```bash
echo "Generade migration"
alembic revision --autogenerate -m "$(m)"

echo "Upgrade to latest version"
alembic upgrade head

echo "Downgrade to previous version"
alembic downgrade -1
```


Alembic available templates:
 - generic - Generic single-database configuration.
 - async - Generic single-database configuration with an async dbapi.
 - multidb - Rudimentary multi-database configuration.

### FAQ
#### Alembic does not imports models
I've faced this solution, and the goal was to import all of the models into the alembic's .env file. To make it a little bit more comfortable, you can make a `__init__.py` file inside models folder, and do something like this:
```python 
from .db import Base
from .microserviceModel import Service, ServiceLog
from .userModel import User
__all__ = ['Base', 'User', 'Service', 'ServiceLog']
```
A little description:
Writing `from repositories.models import *` inside the env.py allows access all the models and Base (which we need for metadata), and do not update .env file all the time. IMHO best practice for this shit, but probably there's a better solution, idk. Obviously, you need to update `__init__.py` file each time you create a new model.