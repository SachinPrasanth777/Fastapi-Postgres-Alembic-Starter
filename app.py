import uvicorn
from fastapi import FastAPI
from utilities.database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True)
