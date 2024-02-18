**NAT** **(from English** **Network** **Address** **Translation** **— “network address translation”)** is a mechanism in TCP/IP networks that allows you to convert IP addresses of transit packets.

The NAT mechanism is defined in RFC 1631, RFC 3022.

Address translation using the NAT method can be performed by almost any routing device - router, access server, firewall. The most popular is SNAT, the essence of the mechanism of which is to replace the source address when a packet passes in one direction and reversely replace the destination address in the response packet. Along with the source/destination addresses, the source and destination port numbers can also be replaced.

Your computer can be connected to the Internet directly. Then they say that it has an external IP address. This usually means that the computer is connected directly to a modem (DSL, cable or regular analog).

Behind NAT means that your computer is not connected to the Internet, but to a local network. Then he has an internal IP address, which itself is inaccessible from the Internet.

Your computer accesses the Internet through NAT - the process of translating internal addresses to external ones and vice versa. A NAT device is usually called a router.

NAT allows intranet hosts to transparently access hosts in the public domain without requiring internal hosts to have registered (and most scarce) Internet network addresses.

The Internet Engineering Task Force has been warning for nearly a decade about a coming address shortage in the current IPv4 address space. Although it appears that the new version of IPv6 will be able to meet the demands of the ever-growing Internet for quite some time, measures proposed over the past few years have already received legal status.

One such proposal is the 1994 standard RFC 1631, The IP Network Address Translator. During the early days of the Internet, consumers were forced to use globally unique network addresses, regardless of whether they planned to connect to the global Internet or not. The idea was to avoid potential conflicts if a formerly private network eventually joined the public Internet.

The simplest NAT device has two network connections: one to the Internet and one to a private network. Hosts on a private network using private IP addresses (sometimes also called Network 10 addresses, which begin with 10.0.0.0 in a range allocated for private use) communicate with the Internet by passing packets directly to the NAT device. Unlike regular routers, which simply read the source and destination addresses of each packet before forwarding them to their destination, NAT devices modify packet headers to replace the source address on the private network with their own Internet address.

Now let's look at the process of establishing a session when using a NAT router at the border of the internal network and the Internet.

When an internal network client establishes a connection with an external network server, then, as in the case of establishing a connection between two PCs, a socket is opened, determined by the source IP address, source port, destination IP address, destination port, and network protocol. When an application transmits data over this socket, the source IP address and source port are inserted into the packet in the source options fields. The destination options fields will contain the server IP address and server port. For example, a computer on the internal network with an IP address of 192.168.0.1 can access a WAN Web server with an IP address of 64.233.188.104. In this case, the client operating system can assign port 1251 (source port) to the established session, and the destination port is the Web service port, that is, 80.

Source IP: 192.168.0.1;

source port: 1251;

Recipient IP address: 64.233.183.104;

destination port: 80;

protocol: TCP.

  
  

The NAT device (router) intercepts the packet coming from the internal network and enters into its internal table a mapping of the source and destination ports of the packet using the destination IP address, destination port, external IP address of the NAT device, external port, network protocol, and internal IPs - client address and port.

Thanks to a NAT router, any PC on the internal network is able to transfer data to the Global Network using the external IP address and port of the router. In this case, the IP addresses of the internal network, as ports assigned to sessions, remain invisible from the external network.

In addition to source NAT (providing users of a local network with internal addresses with access to the Internet), destination NAT is also often used, when calls from outside are translated by a firewall to a server on the local network that has an internal address and is therefore inaccessible directly from outside the network (without NAT).

There are 3 basic concepts of address translation: static (Static Network Address Translation), dynamic (Dynamic Address Translation), masquerade (NAPT, NAT Overload, PAT).

Static NAT - Mapping an unregistered IP address to a registered IP address on a one-to-one basis. Particularly useful when the device must be accessible from outside the network.

Dynamic NAT - Maps an unregistered IP address to a registered address from a group of registered IP addresses. Dynamic NAT also establishes a direct mapping between an unregistered address and a registered address, but the mapping may change depending on the registered address available in the address pool during communication.

Overload NAT (NAPT, NAT Overload, PAT, masquerading) is a form of dynamic NAT that maps multiple unregistered addresses to a single registered IP address using different ports. Also known as PAT (Port Address Translation)

When overloaded, every computer on the private network is translated to the same address, but with a different port number.

Masquerading is a type of network address translation in which the sender's address is dynamically substituted, depending on the address assigned to the interface. The separation of SNAT (source NAT) and masquerading is typical for iptables; in Cisco routers, the translation operation (ip nat source) can work with both given addresses and interfaces (using the address automatically assigned to the interface).

Another feature of masquerading (in iptables) is “forgetting” about installed broadcasts when the interface is stopped. This is due to the fact that after the interface is raised, its address will most likely (in the case of DHCP/Dialup) be different, and records of previously performed translations will not be meaningful.

**NAT** **performs three important functions.**

Allows you to save IP addresses (only if NAT is used in PAT mode) by translating several internal IP addresses into one external public IP address (or into several, but in fewer numbers than internal ones). Most networks in the world are built according to this principle: 1 “white” (that is, external) IP address is allocated to a small area of the home network of a local provider or to an office, behind which all “gray” (that is, internal) IPs work and gain access to the outside. -addresses.

Allows you to prevent or limit access from the outside to internal hosts, leaving the possibility of access from the inside to the outside. When a connection is initiated from within the network, a broadcast is created. Response packets arriving from outside match the generated broadcast and are therefore passed through. If there is no corresponding translation for packets arriving from outside (and it can be created when the connection is initiated or static), they are not allowed through.

Allows you to hide certain internal services of internal hosts/servers. Essentially, the same broadcast above is performed on a specific port, but it is possible to replace the internal port of an officially registered service (for example, TCP port 80 (HTTP server) with external port 54055). Thus, from the outside, on the external IP address, after broadcasting the addresses to the site (or forum), it will be possible for knowledgeable visitors to get to the address, but on the internal server, located behind NAT, it will work on the usual port 80. Increased security and hiding of “non-public” resources.

**Flaws**

With NAT, Internet hosts communicate directly with the NAT device rather than with the actual host on the private network. Incoming packets are sent to the NAT device's IP address, and the device changes the destination address in the packet header from its own Internet address to the private network address of the actual destination host.

As a result - in theory - a single globally unique IP address can hide hundreds, thousands or even millions of hosts whose addresses are defined on a private network. In practice, however, this approach has a number of disadvantages. For example, many Internet protocols and applications rely heavily on the fact that the network actually maintains an end-to-end connection, where packets are transmitted without any modification from the sender to the recipient. An IP security architecture, for example, cannot support operation through a NAT device because the original headers, which contain the original IP addresses of the senders, are digitally signed. Change the source address and the digital signature will lose its integrity.

Using NAT also complicates the work of administrators. Of course, NAT is an excellent solution for an organization, branch, or even department that cannot obtain enough unique Internet addresses. However, when reorganizing, merging or being acquired by another company, where two or more private networks need to be combined, great complexity arises. Even if an organization's structure remains fairly stable, NAT systems can accidentally end up nested, making routing a nightmare.

Not all protocols can "traverse" NAT. Some fail if there is address translation on the path between communicating hosts. Some IP address translation firewalls can correct this shortcoming by replacing IP addresses appropriately not only in the IP headers, but also at higher levels (for example, in FTP protocol commands).

Due to multi-to-one address translation, additional difficulties arise with identifying users and the need to store complete translation logs.

DoS by the host performing NAT - If NAT is used to connect many users to the same service, it can create the illusion of a DoS attack on the service (multiple successes and failures). For example, an excessive number of messenger users behind NAT leads to problems with connecting to the server for some users due to exceeding the permissible connection speed. A partial solution to the problem is to use a pool of addresses (groups of addresses) for which translation is carried out.

In some cases, additional configuration is necessary when working with peer-to-peer networks and some other programs (Battle.net games), in which it is necessary not only to initiate outgoing connections, but also to accept incoming ones. However, if the NAT device and software that requires additional configuration supports Universal Plug and Play technology, then in this case the configuration will occur completely automatically and transparently to the user.