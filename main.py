from fastapi import FastAPI
from database import engine
import models
from app.routers import user,bottle,auth


app = FastAPI()
models.Base.metadata.create_all(bind=engine)


app.include_router(user.router)
app.include_router(bottle.router)
app.include_router(auth.router)