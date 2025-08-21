from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from fastapi import APIRouter

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

def jwt_manager(app):
    router = APIRouter()

    @router.post("/login")
    def login():
        token = jwt.encode({"sub": "2223"}, SECRET_KEY, algorithm=ALGORITHM)
        return {"access_token": token, "token_type": "bearer"}

    app.include_router(router, prefix="/auth", tags=["auth"])
