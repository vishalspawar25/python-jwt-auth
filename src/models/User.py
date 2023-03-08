from pydantic import BaseModel,Field
from enum import Enum

# Using enum class create enumerations
class Roles(Enum):
   Admin = 'Admin'
   Developer = 'Developer'
   Auditor = 'Auditor'

class User(BaseModel):
    username: str
    hashed_password : str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None
    role:Roles | None=None

