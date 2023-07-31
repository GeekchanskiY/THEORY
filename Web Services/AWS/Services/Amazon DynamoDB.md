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