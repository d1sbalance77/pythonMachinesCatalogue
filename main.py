from fastapi import FastAPI
from machines.machines_api import machine_router
from database import Base, engine

Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(machine_router)