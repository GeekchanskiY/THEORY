
## General theory:

### CAP theorem
In theoretical computer science, the **CAP theorem**, also named **Brewer's theorem** after computer scientist Eric Brewer, states that any distributed data store can provide only two of the following three guarantees:

- Consistency
 Every read receives the most recent write or an error.

- Availability
 Every request receives a (non-error) response, without the guarantee that it contains the most recent write.

- Partition tolerance
 The system continues to operate despite an arbitrary number of messages being dropped (or delayed) by the network between nodes.


### ACID

ACID is a set of properties that are designed to guarantee the reliability and consistency of a database. The acronym ACID stands for: 
	● Atomicity: All transactions in a database are atomic, which means that they are either completed in their entirety, or not completed at all. This ensures that if a transaction fails, the database is left in a consistent state. 
	● Consistency: A transaction is only committed if it leaves the database in a consistent state. This means that all data integrity constraints are maintained after the transaction is completed. 
	● Isolation: Transactions are isolated from each other, which means that the effects of one transaction are not visible to other transactions until the transaction has been committed. This prevents data inconsistencies that could occur if multiple transactions were allowed to read and write to the same data simultaneously. 
	● Durability: Once a transaction has been committed, it is durable and will not be lost even if the database experiences a power failure or other failure. 


### Scaling
There are several ways to scale a database to accommodate more users or a larger volume of data: 
1. Vertical scaling: This involves adding more resources (such as CPU, memory, or storage) to the existing database server to increase its capacity. This can be done by upgrading the hardware or by deploying the database on a larger, more powerful server. 
2. Horizontal scaling: This involves adding more database servers to the system and distributing the load across them. This can be done using techniques such as database sharding, in which the data is partitioned across multiple servers, or by using a database cluster, in which multiple servers work together to provide a single logical database. 
3. Caching: A cache is a temporary storage area that is used to store frequently accessed data. By using a cache, you can reduce the number of queries that need to be sent to the database, which can improve the performance of the system. 
4. Replication: By replicating the data across multiple servers, you can increase the availability and fault tolerance of the system. This can be done using techniques such as master-slave replication, in which one server acts as the master and the others act as slaves, or using peer-to-peer replication, in which all servers are equal. 
5. Partitioning: By partitioning the data across multiple servers or tables, you can distribute the load and improve the scalability of the system. This can be done using techniques such as range partitioning or hash partitioning.

### Design
There are several principles that are important to consider when designing a database: 
1. Normalization: This involves breaking down the data into smaller, more atomic pieces and organizing it into tables. This can help to eliminate redundancy and improve the efficiency of the database. 
2. Entity-relationship modeling: This involves creating a diagram that shows the relationships between different entities (such as customers, orders, and products) in the database. This can help to identify the data that needs to be stored and the relationships between the data. 
3. Indexing: Indexes are used to speed up the performance of the database by allowing faster lookups of data. It is important to carefully consider which columns should be indexed, as adding too many indexes can slow down the performance of the database. 
4. Data types: It is important to choose appropriate data types for each column in the database, as this can affect the performance and efficiency of the database.

### Transaction Isolation
1. Read uncommitted: This is the lowest isolation level, and it allows transactions to read data that has been modified by other transactions, but not yet committed. This can result in dirty reads, where a transaction reads data that is later rolled back by another transaction. 
2. Read committed: This isolation level guarantees that transactions will only be able to read data that has been committed by other transactions. This prevents dirty reads, but it does not prevent non-repeatable reads or phantom reads (described below). 
3. Repeatable read: This isolation level guarantees that a transaction will see the same data every time it reads a row, even if the data is modified by other transactions. This prevents dirty reads and non-repeatable reads, but it does not prevent phantom reads. 
4. Serializable: This is the highest isolation level, and it guarantees that transactions will be executed in a serializable order, as if they had been executed one at a time. This prevents dirty reads, non-repeatable reads, and phantom reads.

### WAL
WAL stands for "Write-Ahead Log," and it's a concept used in computer science and databases to ensure data durability and consistency, particularly in systems that manage persistent data.

Here's how it works:

1. **Logging Changes:** When data is modified in a system, instead of immediately writing the changes directly to the main data store (like a database file), the changes are first recorded in a separate log called the Write-Ahead Log. This log contains a record of the changes that need to be applied to the data.

2. **Sequential Write:** The Write-Ahead Log is designed for sequential writes, which are typically faster and more efficient than random writes to the main data store. This helps improve performance and reduces the impact of disk fragmentation.

3. **Durability:** The Write-Ahead Log provides durability guarantees. Before acknowledging a write operation as complete, the system ensures that the corresponding log entry has been successfully written to disk. This ensures that even if a system crashes or loses power, the changes recorded in the log can be replayed to recover the data to a consistent state.

4. **Atomicity and Recovery:** In case of system failure, the Write-Ahead Log plays a crucial role in recovery. The system can replay the log entries and apply the changes to the main data store to bring it back to the state it was in just before the failure occurred. This ensures that the system maintains the ACID properties (Atomicity, Consistency, Isolation, Durability) even in the face of failures.


Write-Ahead Logs are used in various systems, including databases, file systems, and distributed data stores. They are essential for maintaining data integrity and consistency, especially in environments where failures can occur at any time.


### Different topics

[[NoSQL]]

[[SQL]]

[[SQL vs NoSQL]]