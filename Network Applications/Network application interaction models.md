<p style='font-size: 32px; font-weight: bold;'>ISO/OSI</p>
![[ISO_OSI+TCP_IP.png]]

Consists of 7 primary levels:

**Physical level.**

The physical layer defines the properties of the data transmission medium (coaxial cable, twisted pair, fiber optic channel, etc.) and methods of its connection
cable adapters: cable specifications (resistance, capacitance,
isolation, etc.), a list of valid connectors, signal processing methods, etc.

**Link level.**

At the link level of the model, two sublevels are considered:
a sublevel of access control to the data transmission medium and a sublevel of control of the logical channel. Access control to the data transmission medium defines the methods of the use of network adapters of the data transmission medium. Control sublayer
logical link defines the concept of a channel between two network adapters, as well as
methods for detecting and correcting data transmission errors. The main purpose of the process fools the link layer to prepare a block of data (commonly called a frame) for the next
general network layer.
There are two points to note here:
1) starting from the logical link control sublayer and above, the protocols do not
depend on the data transmission medium;
2) to organize a local network, only physical and channel levels, but such a network will not be scalable (cannot expand), because has a limited specific addressing capabilities and does not have routing functions.

**Network layer.**

The network layer defines addressing and routing methods for the computers on the network. Unlike the link layer, the network layer defines a single addressing method for all computers on the network regardless of the method of data transmission. This level defines how computer networks are connected. The result of the procedures of the network layer is the packet that is processed by the transport layer procedures.

**Transport layer.**

The main purpose of the transport layer procedures is
preparation and delivery of data packets between endpoints without errors and in the right
random sequence. The transport layer procedures generate files for the session
layer from packets received from the network layer.

**Session level.** 

The session layer will determine how to set up and tear down
connections (called sessions) between two applications running on a network.
It should be noted that the session layer is the point of interaction between programs and computer network.

**Presentation level.** 

At the representative level, the data format is defined by applications. The procedures at this level describe how to encrypt, compress and transform of data character sets.

**Application level.**

The main purpose of the level: to determine the ways of interaction
actions of users with the system (define the interface).

<p style='font-size: 32px; font-weight: bold;'>TCP/IP</p>