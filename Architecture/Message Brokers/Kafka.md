
Architecture:
Kafka is based on a publish-subscribe model, where producers send messages to topics, and consumers subscribe to one or more topics and receive messages from them

Scalability:
Kafka is designed to handle large volumes of data and is horizontally scalable, meaning it can handle increased load by adding more brokers to the cluster

Durability:
Kafka support message durability, meaning messages are persisted to disk and can survive server restarts. However, Kafka provides more options for configuring message durability, including the ability to specify how long to retain messages and how many copies of each message to keep.

Stream processing:
Kafka includes built-in support for stream processing, allowing developers to build real-time data pipelines and applications that process and analyze data as it is produced.

Kafka can be integrated with a variety of stream processing and data processing frameworks, and is often used in conjunction with tools such as Apache Spark, Apache Flink, and Apache Hadoop.

Kafka is a better fit for applications that need to handle high volumes of data in real time, such as those that involve stream processing or real-time analytics.

Both RabbitMQ and Kafka can be deployed on-premises or in the cloud, and both have tools and resources available for managing and monitoring deployments. However, Kafka may be more complex to set up and manage than RabbitMQ, due to its distributed architecture and the need to configure and manage multiple brokers and zookeeper nodes.

Delivery guarantees:
Kafka provides several delivery guarantees, including at least once delivery, at most once delivery, and exactly once delivery. The specific guarantee provided depends on the configuration of the Kafka producer and consumer, as well as the configuration of the Kafka cluster. Kafka also provides configurable retention periods for messages, allowing developers to specify how long to retain messages on the server before they are deleted.
1. **At Most Once**: Messages can be delivered "at most once." In this case, a message might be lost, but it won't be delivered more than once. This level is suitable for situations where losing some messages is acceptable.

2. **At Least Once**: Messages will be delivered "at least once." This means that messages might be delivered multiple times, but they won't be lost. This level provides higher reliability but can lead to message duplication.

3. **Exactly Once**: This level guarantees that messages will be delivered exactly once and won't be duplicated. It's the strictest level of delivery guarantee and provides the highest reliability but requires additional mechanisms and control.

## Kafka offsets
(source: chatgpt, prompt: kafka offsets)
In the context of Apache Kafka, "offsets" refer to the unique identifiers associated with each message in a Kafka topic partition. Kafka is a distributed streaming platform where messages are organized into topics, and each topic is divided into one or more partitions. Partitions allow messages to be distributed and processed in parallel, providing scalability and fault-tolerance.

Offsets are crucial for tracking the position of a consumer within a partition. Each message within a partition is assigned a sequential offset number. When a consumer reads messages from a partition, it keeps track of the last offset it has consumed. This offset acts as a bookmark, allowing the consumer to resume reading from the same position if it gets disconnected or starts processing the data again.

Key points about Kafka offsets:

1. Sequential numbering: Offsets are integers assigned to messages in a partition in the order they are produced. They start from 0 for the first message and increment by one for each subsequent message.

2. Immutable: Once an offset is assigned to a message, it cannot be changed. Kafka retains the messages and their offsets for a configurable retention period, allowing consumers to consume messages from the past if necessary.

3. Consumer responsibility: The responsibility for keeping track of offsets and managing the consumption progress lies with the consumers. Kafka itself does not manage or maintain the consumer's offset position.

4. Committing offsets: After processing a batch of messages, a consumer should commit its current offset to Kafka to mark the position up to which it has consumed the messages. This ensures that, in case of a consumer restart, it can resume reading from the last committed offset and avoid reprocessing messages.

5. Offsets storage: Consumers can store offsets in different ways. The two common approaches are:
   a. **Kafka Broker**: Kafka provides a built-in offset management mechanism called "consumer group offsets." Consumer offsets are committed to a Kafka topic named "__consumer_offsets" and are managed by Kafka itself. This option is convenient as it allows Kafka to handle offset management, but it might not be as flexible as other options.
   b. **Externally managed storage** : Consumers can choose to manage offsets externally in their own storage systems. This approach provides more flexibility and control over offset management but requires additional implementation effort.

Overall, Kafka offsets play a vital role in maintaining the state of consumers and ensuring reliable, fault-tolerant message processing in Kafka-based applications.


## Kafka Consumer Groups
n Apache Kafka, consumer groups are a fundamental concept used to achieve parallelism and scalability when consuming data from Kafka topics. Consumer groups allow multiple consumers to work together to process messages from one or more partitions of a topic. Each partition is only consumed by a single consumer within the group at any given time, ensuring efficient load distribution and fault tolerance.

Here's how consumer groups work:

1. **Partition Distribution**: Kafka topics are divided into one or more partitions. Each partition is a linearly ordered log of messages. When you create a consumer group, Kafka ensures that each partition is assigned to only one consumer within the group. This distribution allows multiple consumers to work on different partitions in parallel.

2. **Parallel Processing**: Within a consumer group, multiple consumer instances (or consumers) can be running concurrently. Each consumer reads messages from its assigned partitions independently. This enables parallel processing of messages, which is essential for achieving high throughput and performance.

3. **Load Balancing**: Kafka automatically manages the assignment of partitions to consumers in a way that balances the load across the group. If new consumers join or existing consumers leave the group, Kafka will reassign partitions accordingly to maintain load balance.
 
4. **Scaling and Fault Tolerance**: Consumer groups provide fault tolerance by allowing multiple instances of a consumer to be part of the same group. If one consumer instance fails, its partitions are automatically reassigned to other healthy consumers. This ensures that data processing continues smoothly even in the presence of failures.

5. **Offsets and State Tracking**: Each consumer group maintains its own offset per partition. An offset is the position of the last message consumed by the consumer. Kafka allows consumers to specify their starting offset, enabling them to begin reading messages from a specific point in a partition.

Consumer groups are widely used in scenarios where you need to process data from Kafka topics efficiently, distribute the workload across multiple consumers, and ensure fault tolerance. They are particularly valuable in scenarios such as real-time data processing, event-driven architectures, and log aggregation.

When designing your Kafka-based application, it's important to consider factors such as the number of partitions, the number of consumer instances, the processing logic, and the desired level of fault tolerance to effectively use consumer groups and achieve your data processing goals.

## Stuff
ZooKeeper
Kafka connections
DataLake

