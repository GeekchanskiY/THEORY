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