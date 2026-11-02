# What is docker
Docker is an open platform for developing, shipping, and running applications. It provides the ability to package and run an application in a loosely isolated environment called a **container**. 

The isolation and security let you *run many containers simultaneously on a given host*.

Containers are lightweight and contain everything needed to run the application, so you don't need to rely on what's installed on the host. 

You can share containers while you work, and be sure that everyone you share with gets the same container that works in the same way.

Docker is written in the Go programming language and takes advantage of several features of the Linux kernel to deliver its functionality. Docker uses a technology called namespaces to provide the isolated workspace called the container. When you run a container, Docker creates a set of namespaces for that container.

These namespaces provide a layer of isolation. Each aspect of a container runs in a separate namespace and its access is limited to that namespace.

---
# What is container
Containers are isolated processes for each of app's components, runs in its own isolated environment, completely isolated from everything else on machine.

Containers are:
- **Self-contained**. Each container has everything it needs to function with no reliance on any pre-installed dependencies on the host machine.
- **Isolated**. Since containers run in isolation, they have minimal influence on the host and other containers, increasing the security of your applications.
- **Independent**. Each container is independently managed. Deleting one container won't affect any others.
- **Portable**. Containers can run anywhere! The container that runs on your development machine will work the same way in a data center or anywhere in the cloud!

---
## Container vs Virtual machines
Comparing to Virtual Machine, VM is an entire operating system with its own kernel, hardware drivers, programs, and applications. Spinning up a VM only to isolate a single application is a lot of overhead.

A container is simply an isolated process with all of the files it needs to run. If you run multiple containers, they all share the same kernel, allowing you to run more applications on less infrastructure.

---
# Docker architecture
Docker uses a client-server architecture. The Docker client talks to the Docker daemon, which does the heavy lifting of building, running, and distributing your Docker containers. The Docker client and daemon can run on the same system, or you can connect a Docker client to a remote Docker daemon. The Docker client and daemon communicate using a REST API, over UNIX sockets or a network interface. Another Docker client is Docker Compose, that lets you work with applications consisting of a set of containers.

---
## Docker daemon
The Docker daemon (`dockerd`) listens for Docker API requests and manages Docker objects such as images, containers, networks, and volumes. A daemon can also communicate with other daemons to manage Docker services.

---
## Docker client
The Docker client (docker) is the primary way that many Docker users interact with Docker. When you use commands such as docker run, the client sends these commands to dockerd, which carries them out. The docker command uses the Docker API. The Docker client can communicate with more than one daemon.

---
## Docker desktop
Docker Desktop includes the Docker daemon (dockerd), the Docker client (docker), Docker Compose, Docker Content Trust, Kubernetes, and Credential Helper.

---
## Docker registries
A Docker registry stores Docker images. Docker Hub is a public registry that anyone can use, and Docker looks for images on Docker Hub by default. You can run your own private registry.

---
## Docker objects
When you use Docker, you are creating and using:
- [[Images|Images]]
- [[Containers|Containers]]
- [[Networks|Networks]]
- [[Volumes|Volumes]]
- [[Plugins|Plugins]]

and other objects.

---
## Docker compose
Docker compose is a docker client, that lets you work with applications consisting of a set of containers.

[[Docker compose]]

#devops #TODO #docker