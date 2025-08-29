

### Must-have feature

**psycopg2.errors.InFailedSqlTransaction**: current transaction is aborted, commands ignored until end of transaction block

The error message means that one of the preceding SQL statements has resulted in an error. If an exception occurs while executing an SQL statement you need to call the connection's rollback method (`conn.rollback()`) to reset the transaction's state. PostgreSQL will not permit further statement execution otherwise.

to fix:
```python
try:
    cursor.execute(sql, values)
    conn.commit()
except Exception as e:
    print(f'Error {e}')
    print('Anything else that you feel is useful')
    conn.rollback()
```