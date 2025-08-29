
Both RabbitMQ and Kafka can be deployed on-premises or in the cloud, and both have tools and resources available for managing and monitoring deployments. However, Kafka may be more complex to set up and manage than RabbitMQ, due to its distributed architecture and the need to configure and manage multiple brokers and zookeeper nodes.

Nice rabbitMQ architecture overview
https://www.linkedin.com/pulse/rabbitmq-features-architecture-huzaifa-asif#:~:text=RabbitMQ%20Architecture,to%20the%20messages%20for%20processing.

Delivery Guarantees:
RabbitMQ provides at least once delivery guarantees by default, but also offers support for at most once delivery and exactly once delivery through the use of publisher confirms and transactions. RabbitMQ also provides configurable message persistence and durability, allowing developers to specify whether messages should be persisted to disk and how long to retain them before they are deleted.

[[rabbitMQ_queue_options]]