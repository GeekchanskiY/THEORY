
### Config definition
To define different services for easier connection - we can use `.pg_service.conf` located in `$HOME` directory
Example structure of this file:
```.pg_service.conf
# Comment
[service_name]
host=localhost
port=5410
dbname=postgres
user=postgres
```

and then we can `export PGSERVICE=service_name` and simply run psql with this connection