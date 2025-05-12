

PostgreSQL is a powerful, open source object-relational database system with over 35 years of active development that has earned it a strong reputation for reliability, feature robustness, and performance.

[[PG Data Types]]
[[PG CONSTRAINTS]]
[[PG MVCC]]
[[PG useful notes]]
[[Psql shell]]
## Indexes
In PostgreSQL, an index is a data structure that allows efficient access to specific rows within a table. There are several types of indexes that you can use in PostgreSQL, each with its own specific characteristics and use cases. Here is a brief overview of the different types of indexes available in PostgreSQL: 
1. B-tree index: This is the most common type of index in PostgreSQL and is used to index values that are sorted in an ascending or descending order. B-tree indexes are good for a wide range of queries, including those that use equal and range operators (e.g., WHERE column = value and WHERE column BETWEEN value1 AND value2). 
2. Hash index: This type of index uses a hash function to map values to index entries. Hash indexes are efficient for exact match queries (e.g., WHERE column = value) but are not good for range queries. 56 
3. GiST index: A generalized search tree (GiST) index is a multi-purpose index that can be used to index data of various types, including geometric data and text data. GiST indexes are good for full-text search and spatial queries. 
4. GIN index: A generalized inverted index (GIN) is similar to a GiST index, but it is optimized for indexing multi-valued attributes (e.g., arrays) and full-text search. 
5. SP-GiST index: A space-partitioned generalized search tree (SP-GiST) index is a variant of the GiST index that is optimized for indexing multi-dimensional data
## Replication and types
PostgreSQL supports several types of replication, each designed to address specific use cases and requirements. Here are the primary replication types in PostgreSQL:

1. **Physical Replication:**
    
    - **Streaming Replication (Synchronous and Asynchronous):** Streaming replication is a built-in feature of PostgreSQL that replicates the entire database cluster at the disk block level to one or more standby servers. Synchronous replication ensures that a transaction is not considered committed until it's replicated to at least one standby server, providing high data consistency. Asynchronous replication allows for more flexibility but may introduce some level of data lag. 
    - **File-Based Log Shipping:** This replication method involves copying transaction log (WAL) files from the primary server to standby servers. Standby servers apply these logs to maintain a copy of the primary database. While less efficient and slower than streaming replication, it's useful in certain scenarios. 
2. **Logical Replication:**
    - **Logical Replication:** Logical replication replicates data changes in a more granular manner, replicating individual changes (INSERTs, UPDATEs, DELETEs) at the logical level. This allows for more flexibility in selecting specific tables or columns for replication and can be used for data transformations, filtering, and integrating with external systems.
    - **Bi-Directional Replication (BDR):** BDR is an extension for PostgreSQL that enables multi-master replication. It allows two or more PostgreSQL databases to act as both primary and standby servers simultaneously, facilitating active-active replication for high availability and load balancing.
3. **Cascading Replication:**
    - **Cascading Replication:** In a cascading replication setup, you have a primary server replicating to one or more standby servers. These standby servers can, in turn, act as primaries and replicate to their own set of standby servers. This creates a cascading chain of replication, which can be used to distribute data to multiple locations or tiers of servers.
4. **Bucardo:**
    - **Bucardo:** Bucardo is a third-party replication system for PostgreSQL that supports multi-master replication. It's designed to handle complex replication scenarios and is particularly useful when dealing with heterogeneous PostgreSQL versions or non-standard replication needs.
5. **Slony-I:**
    - **Slony-I:** Slony-I is another third-party replication system for PostgreSQL. It offers asynchronous, master-to-multiple-standby replication, and it's known for its flexibility and extensibility.
6. **pglogical:**
    - **pglogical:** pglogical is a third-party logical replication solution for PostgreSQL. It allows you to replicate data between PostgreSQL databases efficiently, with features like conflict resolution and filtering.

The choice of replication type depends on your specific requirements, such as data consistency, read scaling, failover capabilities, and system complexity. PostgreSQL's flexibility and the availability of third-party tools provide a range of options for designing a replication solution tailored to your needs.

## Scans
1. **Sequential Scan (Table Scan):**
    
    - **Description:** A sequential scan is the most basic form of data retrieval in PostgreSQL. It involves scanning the entire table row by row to find the required data.
    - **When to Use:** Sequential scans are typically used when no indexes are available or when the query condition matches a large portion of the table, making it more efficient to read all rows sequentially.
    - **Example:** `SELECT * FROM customers WHERE age > 30;`
2. **Index Scan:**
    
    - **Description:** An index scan involves using an index structure (e.g., B-tree, GiST, GIN) to quickly locate and retrieve data rows that match the query condition.
    - **When to Use:** Index scans are efficient when querying for specific rows or ranges of data, especially for columns with high selectivity.
    - **Example:** `SELECT * FROM products WHERE product_id = 123;`
3. **Bitmap Index Scan:**
    
    - **Description:** Bitmap index scans use multiple indexes to create bitmaps for each index, and then perform a bitwise operation to combine the bitmaps to identify matching rows.
    - **When to Use:** Bitmap index scans are useful when multiple conditions need to be combined using logical operators (AND, OR) in a query.
    - **Example:** `SELECT * FROM employees WHERE department = 'HR' AND salary > 50000;`
4. **Index-Only Scan:**
    
    - **Description:** This scan type is similar to an index scan, but it retrieves data directly from the index without the need to access the table itself, resulting in improved performance.
    - **When to Use:** Index-only scans are suitable when all the columns needed in the query are included in the index.
    - **Example:** `SELECT employee_id, salary FROM employees WHERE department = 'IT';`
5. **Bitmap Heap Scan:**
    
    - **Description:** Bitmap heap scans are used in combination with bitmap index scans. They retrieve data from the table after identifying matching rows using bitmaps.
    - **When to Use:** When multiple conditions are combined using bitmap indexes, a bitmap heap scan may be used to access the corresponding table rows.
    - **Example:** Complex queries with multiple conditions and bitmap index scans.
6. **Sequential Bitmap Heap Scan:**
    
    - **Description:** This is similar to a bitmap heap scan but retrieves rows in the order they appear in the table. It is used when the order of retrieved rows matters.
    - **When to Use:** When the result set must be ordered in a specific way based on the bitmap index conditions.
    - **Example:** Queries with ORDER BY clauses that match indexed conditions.
7. **Index-Scan Types (e.g., Index-Only, Bitmap Index Scan):**
    
    - **Description:** These are variations of index scans optimized for specific use cases, such as index-only scans for retrieving data directly from the index.
    - **When to Use:** Use specialized index-scan types when they provide performance benefits for your specific query.
