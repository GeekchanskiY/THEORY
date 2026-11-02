# What is container
Containers are isolated processes for each of app's components. They run in their own isolated environment, completely isolated from everything else on machine.

Containers are:
- **Self-contained**. Each container has everything it needs to function with no reliance on any pre-installed dependencies on the host machine.
- **Isolated**. Since containers run in isolation, they have minimal influence on the host and other containers, increasing the security of your applications.
- **Independent**. Each container is independently managed. Deleting one container won't affect any others.
- **Portable**. Containers can run anywhere! The container that runs on your development machine will work the same way in a data center or anywhere in the cloud!

## Container vs Virtual machines
Comparing to Virtual Machine, VM is an entire operating system with its own kernel, hardware drivers, programs, and applications. Spinning up a VM only to isolate a single application is a lot of overhead.

A container is simply an isolated process with all of the files it needs to run. If you run multiple containers, they all share the same kernel, allowing you to run more applications on less infrastructure.

#devops #TODO #docker