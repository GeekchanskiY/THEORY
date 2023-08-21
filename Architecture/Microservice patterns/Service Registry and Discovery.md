source: https://blog.bitsrc.io/service-discovery-pattern-in-microservices-55d314fac509

The service discovery pattern is mainly used in microservices applications to find the network locations of microservices.

The service discovery pattern uses a centralized server named **“service registry”** to maintain a global view of microservices’ network locations. Microservices update their locations in the service registry at fixed intervals. Clients can connect to the service registry and fetch the locations of microservices.

There are 2 main service discovery patterns available to implement service discovery for microservices.

- **Client-side service discovery**
- **Server-side service discovery**

# How Does Service Discovery Work?

As mentioned, there are 3 participants in the service discovery pattern:

- **Service registry**
- **Client**
- **Service consumers (Microservices)**

The service registry keeps records of the network locations of the microservices. Microservice instances register themselves and provide their locations to the service registry. Then, clients can find the locations of microservices using the service registry and directly call them to fulfill its need.

To get a better understanding, let’s consider a simple microservice architecture with 2 services:
![[Service Registry and Discovery.png]]
Here, we can break the service discovery communication flow into 4 parts:

1. First, the service provider registers its location in the service registry.
2. The client looks for relevant service locations in the service registry.
3. The service registry returns the location of the required microservice.
4. The client directly calls the microservice.

As you can see, the service discovery pattern is pretty straightforward. However, there can be slight changes in the above-described process in its implementation.

# **The Client‑side Discovery Pattern**

In the Client-side service discovery pattern, the client is responsible for finding the network locations of microservices and loading balancing requests between them.

First, the client queries the service registry and retrieves the locations. Then, the client uses its dedicated load balancer to select a microservice and sends the request.

![[Service Registry on Client Side.png]]

## Advantages of Client-side Service Discovery

- It is straightforward and easy to understand.
- The service registry is the only moving part.
- The client knows the locations of microservices before sending the request.
- The client can make intelligent load balancing decisions with its dedicated load balancer.

## Disadvantages of Client-side Service Discovery

- The client is responsible for implementing service discovery logic.
- The client is coupled with the service registry.
- Need to implement service discovery logic for each language used by your clients.

# **The Server‑side Discovery Pattern**

The Server-side discovery pattern solves one of the significant issues in Client-side discovery by decoupling the client and the services registry. In this approach, the client does not have a dedicated load balancer. Instead, the load balancer acts as a middle man and is responsible for communicating with the service registry.

First, the client requests a microservice through the load balancer. Then, the load balancer queries the service registry and finds the location of the relevant microservice. Finally, the load balancer routes the request to the microservice.
![[Service registry on Server side.png]]
This pattern is widely used in modern applications since both clients and microservices are independent of the service registry. Most importantly, you don’t need to implement the Server-side discover load balancers from scratch since many deployment environments provide load balancers.

For example, you can use AWS Elastic Load Balancer or proxies on the Kubernetes environments as Server‑side discovery load balancers.

## Advantages of Server-side Service Discovery

- The service registry is decoupled from the client.
- There is no need to implement service discovery logic for each language your clients use.
- Can use load balancers provided by deployment environments.

## Disadvantages of Server-side Service Discovery

- If the deployment environment does not provide, developers need to create and manage load balancers.

# What is Service Registry?

Throughout the article, I have mentioned that the service registry is responsible for keeping the locations of each microservice. So, it is essential to know how the service registry works to understand the service discovery pattern completely.

==The service registry is a database containing all available microservices’ network locations.== Therefore, it should be highly available and continuously updated. So, it is essential to have a reliable mechanism to continuously update and maintain data consistency in a service registry.

In general, a microservice is registered in the service registry when the service starts up. Then, it continuously updates its registration using a heartbeat mechanism. Finally, when the microservice instance terminates, the registration is removed from the service registry.

There are 2 approaches to handling the registration process in the service registry:

- Self-registration.
- Third-party registration.

Both these approaches have several advantages and disadvantages. So, let’s discuss these 2 approaches in detail to understand them better.

In self-registration, the microservices are responsible for registering themselves in the service registry. Once the microservice is registered, it will keep sending heartbeats to ensure that the registration does not expire.

In Third-party registration, a new component named service registrar is responsible for registering and de-registering microservices. In addition, the service registrar tracks the location changes of microservices by polling the deployment environment or subscribing to the events.