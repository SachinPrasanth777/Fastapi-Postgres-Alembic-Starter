from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from config.dependencies import get_db
from models.models import User
from schema.schema import UserLogin, UserSignUp

user_router = APIRouter()


@user_router.post("/signup")
async def signup(user_data: UserSignUp, db: Session = Depends(get_db)):
    user = User(username=user_data.username, email=user_data.email)
    user.hash_password(user_data.password)
    db.add(user)
    db.commit()
    return JSONResponse(content={"message": "User created successfully"})


@user_router.post("/login")
async def login(user_data: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == user_data.username).first()
    if user is None or not user.check_password(user_data.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    token = user.generate_token()
    return JSONResponse(content={"access_token": token, "token_type": "bearer"})
