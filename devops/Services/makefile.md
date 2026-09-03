
Makefiles are used to help decide which parts of a large program need to be recompiled. In the vast majority of cases, C or C++ files are compiled. Other languages typically have their own tools that serve a similar purpose as Make. Make can also be used beyond compilation too, when you need a series of instructions to run depending on what files have changed.
Example:
```Makefile
restart:
	sudo docker compose down && \
	sudo docker compose up --build -d \
	&& sudo docker-compose run ressearch_backend bin/rails db:migrate

  
  

.PHONY: create-migrations
create-migrations: # Create an alembic migration
	sudo docker compose exec backend alembic revision --autogenerate -m "$(m)"
```

To call in shell:
```shell
make restart
make create-migrations
```
### Phony
However, sometimes you want your Makefile to run commands that do not represent physical files in the file system. Good examples for this are the common targets "clean" and "all". Chances are this isn't the case, but you _may_ potentially have a file named `clean` in your main directory. In such a case Make will be confused because by default the `clean` target would be associated with this file and Make will only run it when the file doesn't appear to be up-to-date with regards to its dependencies.

These special targets are called _phony_ and you can explicitly tell Make they're not associated with files