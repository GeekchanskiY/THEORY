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

### Howto: auto-migrate in docker-compose
Using makefile is the most optimal solution:
```Makefile
up-build:
	sudo docker-compose up --build -d \
	&& sudo docker-compose run container_name bin/rails db:migrate
```


### Howto: if __ name __ == "__ main __ "
```ruby
if $0 == __FILE__
	puts "articles is being run directly."
else
	puts "articles is being required as a module."
end
```
**Important:** it's not rubysh at all, better use modules