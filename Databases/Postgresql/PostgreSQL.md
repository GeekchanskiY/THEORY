

PostgreSQL is a powerful, open source object-relational database system with over 35 years of active development that has earned it a strong reputation for reliability, feature robustness, and performance.

[[PG Data Types]]
[[PG CONSTRAINTS]]
[[PG MVCC]]

## Indexes
In PostgreSQL, an index is a data structure that allows efficient access to specific rows within a table. There are several types of indexes that you can use in PostgreSQL, each with its own specific characteristics and use cases. Here is a brief overview of the different types of indexes available in PostgreSQL: 
1. B-tree index: This is the most common type of index in PostgreSQL and is used to index values that are sorted in an ascending or descending order. B-tree indexes are good for a wide range of queries, including those that use equal and range operators (e.g., WHERE column = value and WHERE column BETWEEN value1 AND value2). 
2. Hash index: This type of index uses a hash function to map values to index entries. Hash indexes are efficient for exact match queries (e.g., WHERE column = value) but are not good for range queries. 56 
3. GiST index: A generalized search tree (GiST) index is a multi-purpose index that can be used to index data of various types, including geometric data and text data. GiST indexes are good for full-text search and spatial queries. 
4. GIN index: A generalized inverted index (GIN) is similar to a GiST index, but it is optimized for indexing multi-valued attributes (e.g., arrays) and full-text search. 
5. SP-GiST index: A space-partitioned generalized search tree (SP-GiST) index is a variant of the GiST index that is optimized for indexing multi-dimensional data
