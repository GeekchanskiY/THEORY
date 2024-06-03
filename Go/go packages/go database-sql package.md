Package sql provides a generic interface around SQL (or SQL-like) databases.

The sql package must be used in conjunction with a database driver.
See https://golang.org/s/sqldrivers for a list of drivers.

(Quick cast Postgres (pure Go): https://github.com/lib/pq )

Drivers that do not support context cancellation will not return until after the query is completed.

### Quickstart
To setup connection to database:
```go
psqlInfo := fmt.Sprintf("host=%s port=%d user=%s password=%s dbname=%s sslmode=disable", host, port, user, password, dbname)
db, err := sql.Open("postgres", psqlInfo)
```

