

PostgreSQL is a powerful, open source object-relational database system with over 35 years of active development that has earned it a strong reputation for reliability, feature robustness, and performance.

[[PG Data Types]]
[[PG CONSTRAINTS]]


## Indexes
In PostgreSQL, an index is a data structure that allows efficient access to specific rows within a table. There are several types of indexes that you can use in PostgreSQL, each with its own specific characteristics and use cases. Here is a brief overview of the different types of indexes available in PostgreSQL: 
1. B-tree index: This is the most common type of index in PostgreSQL and is used to index values that are sorted in an ascending or descending order. B-tree indexes are good for a wide range of queries, including those that use equal and range operators (e.g., WHERE column = value and WHERE column BETWEEN value1 AND value2). 
2. Hash index: This type of index uses a hash function to map values to index entries. Hash indexes are efficient for exact match queries (e.g., WHERE column = value) but are not good for range queries. 56 
3. GiST index: A generalized search tree (GiST) index is a multi-purpose index that can be used to index data of various types, including geometric data and text data. GiST indexes are good for full-text search and spatial queries. 
4. GIN index: A generalized inverted index (GIN) is similar to a GiST index, but it is optimized for indexing multi-valued attributes (e.g., arrays) and full-text search. 
5. SP-GiST index: A space-partitioned generalized search tree (SP-GiST) index is a variant of the GiST index that is optimized for indexing multi-dimensional data
## MVCC
Multi-Version Concurrency Control (MVCC) is an advanced technique for improving database performance in a multi-user environment.Unlike most other database systems which use locks for concurrency control, Postgres maintains data consistency by using a multiversion model. This means that while querying a database each transaction sees a snapshot of data (a _database version_) as it was some time ago, regardless of the current state of the underlying data. This protects the transaction from viewing inconsistent data that could be caused by (other) concurrent transaction updates on the same data rows, providing _transaction isolation_ for each database session.

The main difference between multiversion and lock models is that in MVCC locks acquired for querying (reading) data don't conflict with locks acquired for writing data and so reading never blocks writing and writing never blocks reading.

The ANSI/ISO SQL standard defines four levels of transaction isolation in terms of three phenomena that must be prevented between concurrent transactions. These undesirable phenomena are:
1. **dirty reads**
 - A transaction reads data written by concurrent uncommitted transaction.
2. **non-repeatable reads**
 - A transaction re-reads data it has previously read and finds that data has been modified by another transaction (that committed since the initial read).
3. **phantom read**
 - A transaction re-executes a query returning a set of rows that satisfy a search condition and finds that the set of rows satisfying the condition has changed due to another recently-committed transaction.

The four isolation levels and the corresponding behaviors are described below.
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
