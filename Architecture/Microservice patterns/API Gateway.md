An API Gateway accepts API requests from a client, processes them based on defined policies, directs them to the appropriate services, and combines the responses for a simplified user experience. Typically, it handles a request by invoking multiple microservices and aggregating the results. It can also translate between protocols in legacy deployments.

## API Gateway Capabilities

API gateways commonly implement capabilities that include:

- **Security policy** – Authentication, authorization, access control, and encryption
- **Routing policy** – Routing, rate limiting, request/response manipulation, circuit breaker, blue-green and canary deployments, A/B testing, load balancing, health checks, and custom error handling
- **Observability policy** – Real-time and historical metrics, logging, and tracing

For additional app- and API-level security, API gateways can be augmented with web application firewall (WAF) and denial of service (DoS) protection.

## API Gateway Benefits

Deploying an API gateway for app delivery can help:

- **Reduce complexity and speed up app releases** by encapsulating the internal application architecture and providing APIs tailored for each client type
- **Streamline and simplify request processing and policy enforcement** by centralizing the point of control and offloading non-functional requirements to the infrastructure layer
- **Simplify troubleshooting** with granular real-time and historical metrics and dashboards