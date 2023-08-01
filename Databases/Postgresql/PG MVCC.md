Multi-Version Concurrency Control (MVCC) is an advanced technique for improving database performance in a multi-user environment.Unlike most other database systems which use locks for concurrency control, Postgres maintains data consistency by using a multiversion model. This means that while querying a database each transaction sees a snapshot of data (a _database version_) as it was some time ago, regardless of the current state of the underlying data. This protects the transaction from viewing inconsistent data that could be caused by (other) concurrent transaction updates on the same data rows, providing _transaction isolation_ for each database session.

The main difference between multiversion and lock models is that in MVCC locks acquired for querying (reading) data don't conflict with locks acquired for writing data and so reading never blocks writing and writing never blocks reading.

The ANSI/ISO SQL standard defines four levels of transaction isolation in terms of three phenomena that must be prevented between concurrent transactions. These undesirable phenomena are:
1. **dirty reads**
 - A transaction reads data written by concurrent uncommitted transaction.
2. **non-repeatable reads**
 - A transaction re-reads data it has previously read and finds that data has been modified by another transaction (that committed since the initial read).
3. **phantom read**
 - A transaction re-executes a query returning a set of rows that satisfy a search condition and finds that the set of rows satisfying the condition has changed due to another recently-committed transaction.

## The four isolation levels and the corresponding behaviors

<table border="1" class="CALSTABLE">
      <thead>
        <tr>
          <th align="left" valign="top">Isolation Level</th>

          <th align="left" valign="top">Dirty Read</th>

          <th align="left" valign="top">Non-Repeatable Read</th>

          <th align="left" valign="top">Phantom Read</th>
        </tr>
      </thead>

      <tbody>
        <tr>
          <td align="left" valign="top">Read uncommitted</td>

          <td align="left" valign="top">Possible</td>

          <td align="left" valign="top">Possible</td>

          <td align="left" valign="top">Possible</td>
        </tr>

        <tr>
          <td align="left" valign="top">Read committed</td>

          <td align="left" valign="top">Not possible</td>

          <td align="left" valign="top">Possible</td>

          <td align="left" valign="top">Possible</td>
        </tr>

        <tr>
          <td align="left" valign="top">Repeatable read</td>

          <td align="left" valign="top">Not possible</td>

          <td align="left" valign="top">Not possible</td>

          <td align="left" valign="top">Possible</td>
        </tr>

        <tr>
          <td align="left" valign="top">Serializable</td>

          <td align="left" valign="top">Not possible</td>

          <td align="left" valign="top">Not possible</td>

          <td align="left" valign="top">Not possible</td>
        </tr>
      </tbody>
    </table>



## How MVCC works

(Source: [Heroku DevCenter](https://devcenter.heroku.com/articles/postgresql-concurrency))

Every transaction in Postgres gets a transaction ID called XID. This includes single one statement transactions such as an insert, update, or delete, as well as explicitly wrapping a group of statements together via `BEGIN` - `COMMIT`. When a transaction starts, Postgres increments an XID and assigns it to the current transaction. Postgres also stores transaction information on every row in the system, which is used to determine whether a row is visible to the transaction or not.

For example, when you insert a row, Postgres stores the XID in the row and calls it `xmin`. Every row that has been committed and has an `xmin` that is less than the current transaction’s XID is visible to the transaction. This means that you can start a transaction and insert a row, and until that transaction `COMMIT`s that row isn’t visible to other transactions. After it commits and other transactions get created, they’re able to view the new row because they satisfy the `xmin < XID` condition – and the transaction that created the row has completed.

A similar mechanism occurs for `DELETE`s and `UPDATE`s, only in these cases Postgres stores an `xmax` value on each row in order to determine visibility. This diagram shows two concurrent transactions inserting and reading rows, and how MVCC comes into play in terms of transaction isolation.

## Disadvantages of MVCC

(Source: [Heroku DevCenter](https://devcenter.heroku.com/articles/postgresql-concurrency))

Now that you know how MVCC and transaction isolation actually works, you’ve added another tool for solving the kinds of problems where a `SERIALIZABLE` isolation level comes in handy. While the advantages of MVCC are clear it also has some disadvantages.

Because different transactions have visibility to a different set of rows, Postgres must maintain potentially obsolete records. This is why an `UPDATE` actually creates a new row and why `DELETE` doesn’t _really_ remove the row: it merely marks it as deleted and sets the XID values appropriately. As transactions complete, there will be rows in the database that can’t possibly be visible to any future transactions. These are called dead rows. Another problem that comes from MVCC is that transaction IDs can only ever grow so much – they’re 32 bits and can “only” support around 4 billion transactions. When the XID reaches its max, it wraps around and starts back at zero. Suddenly _all_ rows appear to be in future transactions, and no new transactions would have visibility into those rows.

Both dead rows and the transaction XID wraparound problem are solved with `VACUUM`. This is routine maintenance, but thankfully Postgres comes with an auto_vacuum daemon that runs at a configurable frequency. It’s important to keep an eye on this because different deployments have different needs when it comes to vacuum frequency. You can read more about what `VACUUM` actually does on the [Postgres docs](http://www.postgresql.org/docs/current/static/routine-vacuuming.html) and how [Heroku handles it](https://devcenter.heroku.com/articles/heroku-postgres-database-tuning).