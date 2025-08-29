Fast, flexible NoSQL database service for single-digit millisecond performance at any scale

In DynamoDB, tables, items, and attributes are the core components that you work with. A _table_ is a collection of _items_, and each item is a collection of _attributes_. DynamoDB uses primary keys to uniquely identify each item in a table and secondary indexes to provide more querying flexibility. You can use DynamoDB Streams to capture data modification events in DynamoDB tables.

## Tables, items, and attributes

The following are the basic DynamoDB components:

- **Tables** – Similar to other database systems, DynamoDB stores data in tables. A _table_ is a collection of data. For example, see the example table called _People_ that you could use to store personal contact information about friends, family, or anyone else of interest. You could also have a _Cars_ table to store information about vehicles that people drive.
    
- **Items** – Each table contains zero or more items. An _item_ is a group of attributes that is uniquely identifiable among all of the other items. In a _People_ table, each item represents a person. For a _Cars_ table, each item represents one vehicle. Items in DynamoDB are similar in many ways to rows, records, or tuples in other database systems. In DynamoDB, there is no limit to the number of items you can store in a table.
    
- **Attributes** – Each item is composed of one or more attributes. An _attribute_ is a fundamental data element, something that does not need to be broken down any further. For example, an item in a _People_ table contains attributes called _PersonID_, _LastName_, _FirstName_, and so on. For a _Department_ table, an item might have attributes such as _DepartmentID_, _Name_, _Manager_, and so on. Attributes in DynamoDB are similar in many ways to fields or columns in other database systems.

## Note:
- Each item in the table has a unique identifier, or primary key, that distinguishes the item from all of the others in the table. In the _People_ table, the primary key consists of one attribute.

- Other than the primary key, the _People_ table is schemaless, which means that neither the attributes nor their data types need to be defined beforehand. Each item can have its own distinct attributes.

- Most of the attributes are _scalar_, which means that they can have only one value. Strings and numbers are common examples of scalars.

- Some of the items have a nested attribute (_Address_). DynamoDB supports nested attributes up to 32 levels deep.


## Primary key

When you create a table, in addition to the table name, you must specify the primary key of the table. The primary key uniquely identifies each item in the table, so that no two items can have the same key.

DynamoDB supports two different kinds of primary keys:

- **Partition key** – A simple primary key, composed of one attribute known as the _partition key_.
    
    DynamoDB uses the partition key's value as input to an internal hash function. The output from the hash function determines the partition (physical storage internal to DynamoDB) in which the item will be stored.
    
    In a table that has only a partition key, no two items can have the same partition key value.

- **Partition key and sort key** – Referred to as a _composite primary key_, this type of key is composed of two attributes. The first attribute is the _partition key_, and the second attribute is the _sort key_.

    DynamoDB uses the partition key value as input to an internal hash function. The output from the hash function determines the partition (physical storage internal to DynamoDB) in which the item will be stored. All items with the same partition key value are stored together, in sorted order by sort key value.
    
    In a table that has a partition key and a sort key, it's possible for multiple items to have the same partition key value. However, those items must have different sort key values.
    
    The _Music_ table described in [Tables, items, and attributes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.TablesItemsAttributes) is an example of a table with a composite primary key (_Artist_ and _SongTitle_). You can access any item in the _Music_ table directly, if you provide the _Artist_ and _SongTitle_ values for that item.
    
    A composite primary key gives you additional flexibility when querying data. For example, if you provide only the value for _Artist_, DynamoDB retrieves all of the songs by that artist. To retrieve only a subset of songs by a particular artist, you can provide a value for _Artist_ along with a range of values for _SongTitle_.


## Secondary indexes

You can create one or more secondary indexes on a table. A _secondary index_ lets you query the data in the table using an alternate key, in addition to queries against the primary key. DynamoDB doesn't require that you use indexes, but they give your applications more flexibility when querying your data. After you create a secondary index on a table, you can read data from the index in much the same way as you do from the table.

DynamoDB supports two kinds of indexes:

- Global secondary index – An index with a partition key and sort key that can be different from those on the table.
    
- Local secondary index – An index that has the same partition key as the table, but a different sort key.


## DynamoDB Streams

DynamoDB Streams is an optional feature that captures data modification events in DynamoDB tables. The data about these events appear in the stream in near-real time, and in the order that the events occurred.

Each event is represented by a _stream record_. If you enable a stream on a table, DynamoDB Streams writes a stream record whenever one of the following events occurs:

- A new item is added to the table: The stream captures an image of the entire item, including all of its attributes.
    
- An item is updated: The stream captures the "before" and "after" image of any attributes that were modified in the item.
    
- An item is deleted from the table: The stream captures an image of the entire item before it was deleted.
    

Each stream record also contains the name of the table, the event timestamp, and other metadata. Stream records have a lifetime of 24 hours; after that, they are automatically removed from the stream.

You can use DynamoDB Streams together with AWS Lambda to create a _trigger_—code that runs automatically whenever an event of interest appears in a stream. For example, consider a _Customers_ table that contains customer information for a company. Suppose that you want to send a "welcome" email to each new customer. You could enable a stream on that table, and then associate the stream with a Lambda function. The Lambda function would run whenever a new stream record appears, but only process new items added to the _Customers_ table. For any item that has an `EmailAddress` attribute, the Lambda function would invoke Amazon Simple Email Service (Amazon SES) to send an email to that address.

![[Amazon DynamoDB streams.png]]

## Optimization
1. **Read/Write Capacity Units (RCUs/WCUs):** If you are using the provisioned throughput model, you need to consider the number of RCUs (Read Capacity Units) and WCUs (Write Capacity Units) that your query consumes. DynamoDB charges you based on the provisioned capacity, so understanding the capacity units used by your query is crucial. You can monitor this in the AWS Management Console or using AWS CloudWatch metrics.
    
2. **Data Model and Indexing:** The structure of your data and the use of secondary indexes impact query efficiency. Well-designed DynamoDB tables and indexes can reduce the query weight. Be mindful of how you model your data and which indexes you create to optimize query performance.
    
3. **Query Patterns:** The specific query pattern you use can have different query weights. For example, querying items by their primary key is more efficient and consumes fewer RCUs than scanning the entire table. You can use the `Query` operation for efficient key-based queries.
    
4. **Batching:** Consider using batch operations like `BatchGetItem` or `BatchWriteItem` to reduce the number of individual requests, which can help optimize cost and performance.
    
5. **Filter Expressions:** Be cautious when using filter expressions with queries. Filtering on non-key attributes can consume additional RCUs as DynamoDB has to read more data to apply the filter. It's often more efficient to design your data model to minimize the need for filtering.
    
6. **Projection Expressions:** Carefully select which attributes to retrieve from the database. If you only need specific attributes, use projection expressions to reduce the amount of data retrieved.
    
7. **On-Demand Capacity:** If you're using the on-demand capacity mode, you don't need to provision RCUs/WCUs explicitly. However, you should still monitor your query performance and cost.
    
8. **Monitoring and Optimization:** Use AWS CloudWatch and DynamoDB metrics to monitor query performance and capacity usage. Adjust your provisioned capacity or switch to on-demand as needed based on usage patterns.
    
9. **Throttling and Auto-Scaling:** Be aware of DynamoDB's throttling mechanisms. If your queries are being throttled, it's an indicator that your table may need more provisioned capacity. DynamoDB can also auto-scale provisioned capacity based on your configured settings.
10. **Cost Explorer:** AWS Cost Explorer can help you analyze the cost of your DynamoDB queries over time. It can provide insights into which queries are consuming the most resources and incurring the highest costs.