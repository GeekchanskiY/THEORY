

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