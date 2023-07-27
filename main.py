from fastapi import FastAPI
from api.routing import router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the PERFUM.AR API"}


app.include_router(router)