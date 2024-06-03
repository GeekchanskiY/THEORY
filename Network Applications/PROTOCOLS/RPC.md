RPC (Remote Procedure Call) is a mechanism that allows one computer process to call functions or procedures on a remote machine as if they were local. It is an abstraction that facilitates remote communication between software components on a network. Here are the main characteristics and functions of RPC:

1. **Remote Procedure Calls:** The basic idea of RPC is that a client process can call functions or methods residing on a remote machine just as if they were residing on a local machine. To the client, this looks like a local procedure call, although in fact it is a remote call.

2. **Transparency:** RPC is committed to providing transparency to the client. This means that the client does not have to worry about the details of the remote call, such as transferring data over the network, serializing and deserializing data, etc.

3. **Interface and Stubs:** RPC usually uses an interface to define remote procedures and their parameters. Then stubs are generated for the client and server sides, which ensure the conversion of local calls to network requests and vice versa.

4. **Protocols and Transports:** RPC can use a variety of network protocols and transports to transmit data, including TCP/IP, HTTP, CORBA, and others.

5. **Examples:** Examples of RPC technologies are gRPC, Apache Thrift, Java RMI (Remote Method Invocation), XML-RPC and many others.

6. **Data Serialization:** Data transfer between client and server requires serialization (conversion into a byte stream) of function parameters and results. This is necessary for transmitting data over the network.

RPC is widely used in distributed systems, web services, and many other applications that require remote communication between software components. This makes it easy to create applications that can run on different machines and share data and functionality.