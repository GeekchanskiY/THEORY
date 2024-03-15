
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

### FastAPI jwt authorization
One way to achieve this:
https://www.starlette.io/authentication/
Another is using DI:
```python
class JWTCredentials(HTTPAuthorizationCredentials):
    username: str



class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> JWTCredentials:
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            
            is_verified, username = self.verify_jwt(credentials.credentials)
            if not is_verified:
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            
            
            return JWTCredentials(
                credentials=credentials.credentials,
                scheme=credentials.scheme,
                username=username
            )
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> Tuple[bool, str | None]:
        
        try:
            payload = decodeJWT(jwtoken)
        except:
            payload = None
        
        if payload:
            return True, payload.get('username')
        else:
            return False, None

```
using this call in route you can do `credentials: JWTCredentials = Depends(JWTBearer())`


[[FastAPI lifespan]]