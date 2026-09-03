# What is an image?
 
 A container image is a standardized package that includes all of the files, binaries, libraries, and configurations to run a container.

Rules of containers:
1. Images are immutable. Once an image is created, it can't be modified. You can only make a new image or add changes on top of it.
2. Container images are composed of layers. Each layer represents a set of file system changes that add, remove, or modify files.

# Where are images stored?
You can store your images on your computer system, and also in an image registry. An image registry is a centralized location for storing and sharing your container images. It can be either public or private.

[Docker Hub](https://hub.docker.com/) is the default global marketplace for storing and distributing images.
Docker Hub provides a variety of Docker-supported and endorsed images known as Docker Trusted Content. These provide fully managed services or great starters for your own images. These include:
- [Docker Official Images](https://hub.docker.com/search?badges=official) - a curated set of Docker repositories, serve as the starting point for the majority of users, and are some of the most secure on Docker Hub
- [Docker Hardened Images](https://hub.docker.com/hardened-images/catalog) - minimal, secure, production-ready images with near-zero CVEs, designed to reduce attack surface and simplify compliance. Free and open source under Apache 2.0
- [Docker Verified Publishers](https://hub.docker.com/search?badges=verified_publisher) - high-quality images from commercial publishers verified by Docker
- [Docker-Sponsored Open Source](https://hub.docker.com/search?badges=open_source) - images published and maintained by open-source projects sponsored by Docker through Docker's open source program

To push image to docker hub:
```shell
docker tag <YOUR_DOCKER_USERNAME>/docker-quickstart <YOUR_DOCKER_USERNAME>/docker-quickstart:1.0

docker push YOUR_DOCKER_USERNAME/docker-quickstart:1.0
```
## Registry vs. repository

While you're working with registries, you might hear the terms _registry_ and _repository_ as if they're interchangeable. Even though they're related, they're not quite the same thing.

A _registry_ is a centralized location that stores and manages container images, whereas a _repository_ is a collection of related container images within a registry. Think of it as a folder where you organize your images based on projects. Each repository contains one or more container images.

#devops #TODO #docker