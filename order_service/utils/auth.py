from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session
from models.user import User, Base
from models.order import get_db

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return {"id": payload.get("sub")}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

class LoginRequest(BaseModel):
    username: str
    password: str

def jwt_manager(app):
    router = APIRouter()

    @router.post("/login")
    def login(request: LoginRequest, db: Session = Depends(get_db)):
        user = db.query(User).filter(User.username == request.username).first()
        if not user or user.hashed_password != request.password:
            raise HTTPException(status_code=401, detail="Invalid username or password")
        token = jwt.encode({"sub": str(user.id)}, SECRET_KEY, algorithm=ALGORITHM)
        return {"access_token": token, "user": user, "token_type": "bearer"}

    app.include_router(router, prefix="/auth", tags=["auth"])