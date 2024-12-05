from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from utilities.bearer import JWTBearer
from models.models import User
from config.config import Settings
from utilities.database import SessionLocal
from models.models import Post
import jwt

settings = Settings()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(token: str = Depends(JWTBearer())) -> User:
    try:
        payload = jwt.decode(token, f"{settings.SECRET_KEY}", algorithms=["HS256"])
        user_id = payload.get("sub")
        db = SessionLocal()
        return db.query(User).filter(User.email == user_id).first()
    except (jwt.PyJWTError, AttributeError):
        return HTTPException(status_code="Invalid token")


def get_post_for_user(
    post_id: str, db: Session = Depends(get_db), user: User = Depends(get_current_user)
) -> Post:
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    if post.author.id != user.id:
        raise HTTPException(
            status_code=403, detail="You don't have permissions to modify this post"
        )

    return post
