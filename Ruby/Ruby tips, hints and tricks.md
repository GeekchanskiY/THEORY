Docker compose for rails:

```docker-compose.yml
essearch_backend:

build:

# dockerfile: ./ressearch/Dockerfile

context: ./ressearch/

env_file:

- .env

image:

ressearch_backend:latest

restart: always

ports:

- "3000:3000"

depends_on:

- db-local
```
*Important*: need to change config/environments/(developments/production).rb and add the following:
config.hosts << "0.0.0.0"
and in Dockerfile CMD must be:
CMD ["./bin/rails", "server", "-b", "0.0.0.0"]
