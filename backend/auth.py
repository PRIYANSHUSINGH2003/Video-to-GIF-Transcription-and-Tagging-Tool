from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from backend.db import SessionLocal
from backend.models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    # Token validation logic, query the DB for the user
    user = SessionLocal.query(User).filter(User.token == token).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return user
