# Container networking
Container networking refers to the ability for containers to connect to and communicate with each other, and with non-Docker network services.

Containers have networking enabled by default, and they can make outgoing connections. A container has no information about what kind of network it's attached to, or whether its network peers are also Docker containers. A container only sees a network interface with an IP address, a gateway, a routing table, DNS services, and other networking details.

When Docker Engine on Linux starts for the first time, it has a single built-in network called the "default bridge" network. When you run a container without the `--network` option, it is connected to the default bridge.

Containers attached to the default bridge have access to network services outside the Docker host. They use "masquerading" which means, if the Docker host has Internet access, no additional configuration is needed for the container to have Internet access.

# User-defined networks
With the default configuration, containers attached to the default bridge network have unrestricted network access to each other using container IP addresses. They cannot refer to each other by name.

It can be useful to separate groups of containers that should have full access to each other, but restricted access to containers in other groups.

You can create custom, user-defined networks, and connect groups of containers to the same network. Once connected to a user-defined network, containers can communicate with each other using container IP addresses or container names.

## Drivers
Docker Engine has a number of network drivers, as well as the default "bridge". On Linux, the following built-in network drivers are available:
- bridge - The default network driver.
- host - Remove network isolation between the container and the Docker host.
- none - Completely isolate a container from the host and other containers.
- overlay - Swarm Overlay networks connect multiple Docker daemons together.
- ipvlan - Connect containers to external VLANs.
- macvlan - Containers appear as devices on the host's network.

To create a network:
```shell
docker network create -d bridge my-net
```

To connect container to a network:
```shell
docker run --network=my-net -it busybox
```

Docker container can be connected to several networks. The default gateway is selected by Docker, and may change whenever a container's network connections change. To make Docker choose a specific default gateway when creating the container or connecting a new network, set a gateway priority. You can change it with option `gw-priority`. The default `gw-priority` is `0` and the gateway in the network with the highest priority is the default gateway. So, when a network should always be the default gateway, it is enough to set its `gw-priority` to `1`:
```shell
docker run --network name=gwnet,gw-priority=1 --network anet1 --name myctr myimage
docker network connect anet2 myctr
```

# Published ports
By default, for both IPv4 and IPv6, the Docker daemon blocks access to ports that have not been published. Published container ports are mapped to host IP addresses. To do this, it uses firewall rules to perform Network Address Translation (NAT), Port Address Translation (PAT), and masquerading.

For example, `docker run -p 8080:80 [...]` creates a mapping between port 8080 on any address on the Docker host, and the container's port 80. Outgoing connections from the container will masquerade, using the Docker host's IP address.

#devops #TODO #docker