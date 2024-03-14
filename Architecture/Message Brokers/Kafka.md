Kafka's fundamental difference from different brokers, is that message is not being deleted after consumers recieved them. Data can be stored for a long time, and the message can be consumed for many times by different consumers in different context.


Kafka's message (event) structure:
 - Key: "alice"
 - Value: "registered"
 - Timestamp: "Mar, 14, 2024 at 4:16 AM"
 - Headers: [{"x-generated-by":"GeekchanskiY.com"}]
 
Messages are being stored inside a named **Topics**, and each of them has one or more **Partition**, which are being stored between brokers in one cluster. It's important for horizontal scaling.

When the message is being publushed, it's being recorded into one of the topic's partitions. **Messages with the same keys are always recording into the same partition**, which allows to follow the order of messages.

To ensure the data safety, partition may be replicated n times, where n is a replication factor. Each partition has a **leader** broker, which works with clients. Leader works with producers, and in general case sends the data to consumers. Leader is being requested by **follower** brokers, which store replicas of all partition data.

Partition is a distributed and replicated log. Each message recieved is being saved to the head of the partition, and gets its unique offset (64-bit number)

Consumer Groups
Each consumer is a part of consumer group. Each group has unique name and registers by the broker inside a kafka cluster. Data can be consumed by different consumer groups from the same topic simultaneously. If the message is being consumed several times by the same consumer group, consumers read them from different partitions, balancing the load.

How does the consumer remembers it's own consumed messages?
He uses own consumer-offsets. He makes offset-commit request to the broker, sending the group, topic-partition id and offset, which should be marked as consumed. Broker saves this data in his own special topic. Due restart, consumer asks for the last commited offset in the topic-partition, and continues reading from this position.




## Stuff
ZooKeeper

Zookeeper - stores metadata and distributed log service, and he tells if the brokers are alive, and which of them is a controller, and allows to check states of leader partitions and their replicas.

Kafka connections
DataLake

