MQTT is an OASIS standard messaging protocol for the Internet of Things (IoT). It is designed as an extremely lightweight publish/subscribe messaging transport that is ideal for connecting remote devices with a small code footprint and minimal network bandwidth. MQTT today is used in a wide variety of industries, such as automotive, manufacturing, telecommunications, oil and gas, etc

The MQTT broker is **the backend system which coordinates messages between the different clients**. Responsibilities of the broker include receiving and filtering messages, identifying clients subscribed to each message, and sending them the messages.

Several message brokers support MQTT. Some of the popular message brokers that support MQTT include:

1. **Mosquitto**: An open-source MQTT broker that is lightweight and widely used in various IoT applications. It's developed by the Eclipse Foundation.
    
2. **HiveMQ**: A MQTT broker designed for enterprise-level deployments with features like clustering, high availability, and advanced security options.
    
3. **EMQ X Broker**: An open-source MQTT broker that supports MQTT, MQTT-SN, CoAP, and LwM2M protocols. It's scalable and designed for IoT applications.
    
4. **VerneMQ**: Another open-source MQTT broker built on the Erlang platform. It's scalable and supports clustering for high availability and scalability.
    
5. **RabbitMQ**: While not solely dedicated to MQTT, RabbitMQ, an open-source message broker, has a plugin for MQTT support. RabbitMQ is highly extensible and widely used in various messaging scenarios.
    
6. **ActiveMQ**: Another popular message broker that supports MQTT among other messaging protocols. It's a Java-based broker with support for a wide range of messaging features and protocols.
    
7. **IBM MQ**: IBM MQ supports MQTT alongside its traditional messaging capabilities. It's often used in enterprise-level deployments where reliability and scalability are crucial.

Note:
There is MQTT-SN (for sensor networks), which fits better if there is low resource network,
MQTT over WebSockets for 2-directional message queue, MQTT-TLS - adds Transport Layer Security protocol to ensure safety