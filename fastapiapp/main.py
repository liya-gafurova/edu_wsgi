import uvicorn
from fastapi import FastAPI

from fastapiapp.routers import router

app = FastAPI()

app.include_router(router, prefix='/posts', tags=['Posts'])

if __name__ == "__main__":
    uvicorn.run("main:app", port=8084, log_level='info')