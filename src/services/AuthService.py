from datetime import datetime, timedelta
from common import Util
from jose import  jwt
from models.User import User

def create_access_token(user: User):
    expire = datetime.utcnow() + timedelta(minutes=15)
    data={"sub": user.username,
         "scope":str(user.role.value),
         "exp": expire}
    
    encoded_jwt = jwt.encode(data.copy(), Util.SECRET_KEY, algorithm=Util.ALGORITHM)
    return encoded_jwt

