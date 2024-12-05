import uvicorn
from fastapi import FastAPI
from utilities.database import engine, Base
from routes.user import user_router
from routes.blog import post_router

app = FastAPI()

app.include_router(user_router, prefix="/user")
app.include_router(post_router, prefix="/post")

Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True)
