
### [[FastAPI clean architecture]]
### Fastapi Dependency injection
Warning: DI in Fastapi can cause deadlock if do not use them properly!
Example of nice usage:
```python 
from fastapi import APIRouter, Depends

from models.user import User
from models.db import get_db

# def get_db():
#     with SessionLocal() as session:
#         yield session

from schemas.user import User as UserSchema
from sqlalchemy.orm import Session



router: APIRouter = APIRouter()

@router.get("/users/", tags=["users"], response_model=list[UserSchema])
async def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users
```
