
Commands hints:
	- Inspect routes: bin/rails routes
	- Run server: bin/rails server
	- Console: bin/rails console
	- Create model: bin/rails generate model Article title:string body:text
	- Migrate: bin/rails db:migrate

#### **[[Rails project structure]]**
### ActiveRecord
Active Record is the M in [MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) - the model - which is the layer of the system responsible for representing business data and logic. Active Record facilitates the creation and use of business objects whose data requires persistent storage to a database. It is an implementation of the Active Record pattern which itself is a description of an Object Relational Mapping system.




### useful stuff

config/environments:
```ruby
config.hosts << /.*/ # allow any hosts
```


#TODO: n+1 problem (bullet)
factorybot
pry (gem pry)
asset compile
active admin
tests 
especially