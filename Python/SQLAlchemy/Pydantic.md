Pydantic is the most widely used data validation library for Python.

Fast and extensible, Pydantic plays nicely with your linters/IDE/brain. Define how data should be in pure, canonical Python 3.8+; validate it with Pydantic.

```python
# Sample usage
from pydantic import BaseModel, ConfigDict, validator

class User(BaseModel):
    model_config: ConfigDict = ConfigDict(from_attributes=True)

    id: int | None = None
    name: str
    email: str
    
    is_staff: bool
    ip_adress: str


class LoginUser(BaseModel):
    model_config: ConfigDict = ConfigDict(from_attributes=True)

    email: str = "SampleUserEmail"
    password: str = "SampleStrongPassword"

    @validator('password')
    def validate_password(cls, v: str, values: dict, **kwargs):
        if len(v) <= 8:
            raise ValueError('Password is too short!')
        
        return v


class UserPrivate(User):
    password: str

```

Note:
UserPrivate extends User model, and adds some fields to it

@validator decorator used to create some custom validations for fields