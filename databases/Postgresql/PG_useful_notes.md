


### Explain vs Explain Analyze

EXPLAIN — show the execution plan of a statement

Analyze - Carry out the command and show actual run times and other statistics. This parameter defaults to `FALSE`.

Keep in mind that the statement is actually executed when the ANALYZE option is used. Although EXPLAIN will discard any output that a SELECT would return, other side effects of the statement will happen as usual. If you wish to use EXPLAIN ANALYZE on an INSERT, UPDATE, DELETE, MERGE, CREATE TABLE AS, or EXECUTE statement without letting the command affect your data, use this approach:

```sql
BEGIN;
EXPLAIN ANALYZE ...;
ROLLBACK;
```

Source: Postgres documentation