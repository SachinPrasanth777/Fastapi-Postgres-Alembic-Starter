import uuid
import bcrypt
import jwt
import datetime
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from utilities.database import Base
from config.config import get_settings


class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    posts = relationship("Post", back_populates="author")

    def hash_password(self, password: str):
        self.hashed_password = bcrypt.hashpw(
            password.encode("utf-8"), bcrypt.gensalt()
        ).decode("utf-8")

    def check_password(self, password: str):
        return bcrypt.checkpw(
            password.encode("utf-8"), self.hashed_password.encode("utf-8")
        )

    def generate_token(self):
        expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        payload = {"sub": str(self.email), "exp": expiration}
        return jwt.encode(payload, f"{get_settings().SECRET_KEY}", algorithm="HS256")


class Post(Base):
    __tablename__ = "posts"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, index=True)
    content = Column(String)
    author_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")
