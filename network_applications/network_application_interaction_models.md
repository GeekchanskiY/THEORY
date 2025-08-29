
[[packet(datagram)]]

# ISO/OSI

OSI stands for **Open Systems Interconnection**. It has been developed by ISO – ‘**International Organization for Standardization**‘, in the year 1984. It is a 7-layer architecture with each layer having specific functionality to perform. All these 7 layers work collaboratively to transmit the data from one person to another across the globe.

![[ISO_OSI+TCP_IP.png]]

Consists of 7 primary levels:

## **Physical level.**

Let's start from the lowest level. It is responsible for the exchange of physical signals between physical devices, hardware. Computer hardware does not understand what a picture is or what is depicted on it; the hardware understands the picture only in the form of a set of zeros and ones, that is, bits.
Physical layer devices operate on bits. They are transmitted over cables (for example, through optical fiber) or without - for example, through Bluetooth or IRDA, Wi-Fi, GSM, 4G and so on.
The physical layer defines the properties of the data transmission medium (coaxial cable, twisted pair, fiber optic channel, etc.) and methods of its connection
cable adapters: cable specifications (resistance, capacitance,
isolation, etc.), a list of valid connectors, signal processing methods, etc.

## **Link layer.**

At the link level of the model, two sublevels are considered:
a sublevel of access control to the data transmission medium and a sublevel of control of the logical channel. Access control to the data transmission medium defines the methods of the use of network adapters of the data transmission medium. Control sublayer
logical link defines the concept of a channel between two network adapters, as well as
methods for detecting and correcting data transmission errors. The main purpose of the process fools the link layer to prepare a block of data (commonly called a frame) for the next
general network layer.
There are two points to note here:
1) starting from the logical link control sublayer and above, the protocols do not
depend on the data transmission medium;
2) to organize a local network, only physical and channel levels, but such a network will not be scalable (cannot expand), because has a limited specific addressing capabilities and does not have routing functions.

When two users are on the same network, consisting of only two devices, this is the ideal case. But what if there are more of these devices?

The second level solves the problem of addressing when transmitting information. The link layer receives bits and turns them into frames (frames). The task here is to generate frames with the address of the sender and recipient, and then send them over the network.

The link layer has two sublayers: MAC and LLC. MAC (Media Access Control) is responsible for assigning physical MAC addresses, and LLC (Logical Link Control) checks and corrects data and controls its transmission. To simplify, we indicate LLC at the second level of the model, but, to be precise, LLC cannot be completely attributed to either the first or second level - it is in between.

Switches operate at the second OSI level; their task is to transmit generated frames from one device to another, using only physical MAC addresses as addresses.

At the data link layer, the ARP protocol (Address Resolution Protocol) is actively used. It maps 64-bit MAC addresses to 32-bit IP addresses and vice versa, thereby encapsulating and decapsulating data.

## **Network layer.**

The network layer defines addressing and routing methods for the computers on the network. Unlike the link layer, the network layer defines a single addressing method for all computers on the network regardless of the method of data transmission. This level defines how computer networks are connected. The result of the procedures of the network layer is the packet that is processed by the transport layer procedures.

At the third level, a new concept appears - routing. For this task, third-level devices were created - routers (they are also called routers). Routers receive a MAC address from switches from the previous layer and are engaged in building a route from one device to another, taking into account all potential problems in the network.
Above the data link layer is the next one - the network layer. At this stage, the concepts of “routing” and “IP address” are introduced. The ARP protocol is used to transform MAC addresses into IP.

This is where traffic is routed. When a user, for example, wants to go to a website and enters its address, a DNS query is sent. The response to it will be the IP address that is inserted into the packet. Data packet is a new term that appears at Layer 3 of the network.

The devices here are a router or router.

## **Transport layer.**

The main purpose of the transport layer procedures is
preparation and delivery of data packets between endpoints without errors and in the right
random sequence. The transport layer procedures generate files for the session
layer from packets received from the network layer.

All seven layers of the OSI model can be divided into two groups:

- Media layers (environment levels),
- Host layers.

The levels of the Media Layers group (L1, L2, L3) are responsible for transmitting information (via cable or wireless network) and are used by network devices such as switches, routers, etc. The levels of the Host Layers group (L4, L5, L6, L7) are used directly on devices, be they desktop computers or mobile devices.

The fourth level is an intermediary between Host Layers and Media Layers, related more to the former than to the latter. Its main task is to transport packages. Naturally, losses may occur during transit, but some types of data are more susceptible to loss than others. For example, if vowels are lost in the text, it will be difficult to understand the meaning, and if a couple of frames disappear from the video stream, this will have virtually no effect on the end user. Therefore, when transmitting data that is most sensitive to losses at the transport level, the TCP protocol is used, which monitors the integrity of the delivered information.

For multimedia files, small losses are not so important; the delay will be much more critical. To transmit such data, which is most sensitive to delays, the UDP protocol is used, which allows communication without establishing a connection.

When transmitted over TCP, data is divided into segments. A segment is a part of a package. When a data packet arrives that exceeds the network capacity, the packet is divided into segments of acceptable size. Packet segmentation is also required on unreliable networks when there is a high probability that a large packet will be lost. When transmitting data via the UDP protocol, data packets are divided into datagrams. A datagram is also part of a packet, but should not be confused with a segment.

The main difference between datagrams is their autonomy. Each datagram contains all the necessary headers to reach the final destination, so they are independent of the network and can be delivered by different routes and in different orders. When datagrams or segments are lost, you end up with “broken” pieces of data that cannot be processed correctly.

The first four levels are the specialization of network engineers. They don't encounter the last three as often, because the fifth, sixth and seventh are handled by developers.

## **Session level.** 

The session layer will determine how to set up and tear down
connections (called sessions) between two applications running on a network.
It should be noted that the session layer is the point of interaction between programs and computer network.

The fifth level operates with pure data. In addition to the fifth, clean data is also used at the sixth and seventh levels. The session layer is responsible for maintaining a session or communication session. The fifth level provides the following services: it manages the interaction between applications, opens up the possibility of synchronizing tasks, ending a session, and exchanging information.

Session-level services are often used in application environments that require remote procedure calls, i.e. to request actions to be performed on remote computers or independent systems on the same device (if there is multiple OS).

An example of how the fifth level works is a video call over a network. During a video call, it is necessary that two data streams (audio and video) flow synchronously. When a third person is added to a conversation between two people, it becomes a conference. The task of the fifth level is to make sure that the interlocutors can understand who is speaking now.


## **Presentation level.** 

At the representative level, the data format is defined by applications. The procedures at this level describe how to encrypt, compress and transform of data character sets.

The tasks of the presentation layer are again indicated by its name. The sixth level is responsible for protocol conversion and data encoding/decoding. The sixth level also deals with the presentation of pictures (in JPEG, GIF, etc.), as well as video and audio (in MPEG, QuickTime). And in addition to this → data encryption, when it needs to be protected during transmission.

## **Application level.**

The main purpose of the level: to determine the ways of interaction
actions of users with the system (define the interface).

Protocols: HTTP, SMTP, POP3, TelNet, etc.

The seventh level is sometimes also called the application layer, but to avoid confusion, you can use the original name - application layer. The application layer is what users interact with, a kind of graphical interface for the entire OSI model; it interacts with others to a minimum.

All services received by the seventh layer from others are used to deliver data to the user. Layer seven protocols do not need to provide routing or guarantee data delivery when the previous six have already taken care of this. The task of the seventh level is to use its protocols so that the user sees the data in a form that is understandable to him.



# TCP/IP

![[OSI-_TCP_IP.png]]


## Difference between TCP/IP and OSI Model

1. TCP refers to Transmission Control Protocol. OSI refers to Open Systems Interconnection.
2. TCP/IP uses both the session and presentation layer in the application layer itself.OSI uses different session and presentation layers.
3. TCP/IP follows connectionless a horizontal approach. OSI follows a vertical approach.
4. The Transport layer in TCP/IP does not provide assurance delivery of packets. In the OSI model, the transport layer provides assurance delivery of packets.
5. Protocols cannot be replaced easily in TCP/IP model. While in the OSI model, Protocols are better covered and are easy to replace with the technology change.
6. TCP/IP model network layer only provides connectionless services. Connectionless and connection-oriented services are provided by the network layer in the OSI model.