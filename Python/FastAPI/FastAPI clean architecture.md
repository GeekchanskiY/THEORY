
Basic project structure should be divided on these layers:
- Routing
- Service
- Repositoty

Repository should work with database
Service is a business logic
Routing is... routing

Average project structure for fastapi:
```
- app/
	- env/
	- src/
		- alembic/
		- routers/
			- modelRouter.py
		- services/
			- modelService.py
		- schemas/
			- modelSchema.py
		- repositories/
			- models/
				- model.py
			- modelRepository.py
	- Dockerfile
	- .dockerignore
	- requirements.txt
	- README.md
```
