### Broker query models:
 - Pull model: consumers are querying server once in n seconds to get new messages. Pull model allows to group messages into a batches, which achieves better capacity, but this model can ruin load balance between consumers.
 - Push model: server requests client, and sending a new data to it. This model is the one that rabbitMQ uses. 

### Typical lifecycle
1. Producer sends message to server
2. Consumer fetches message
3. Server marks message as in-flight. Messages with these flags are not being delivered to other consumers, but still store in the server.
4. Consumer checks the message, using the business logic, and sends ack or nack request back to server, using the unique id which it recieved earlier, signaling if the message was consumed, or there was an error.
5. If the consumer responded with ack, message is being deleted forever. Due nack or timeout, it's being re-send.


Most popular ones are:

[[RabbitMQ]]
[[Kafka]]
[[Redis as MB]]
[[SQS]]

Features:
[[Dead letter queue]]
[[Routing key]]