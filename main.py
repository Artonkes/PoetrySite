from fastapi import FastAPI
import uvicorn
from app.api.v1.APIUsers import router as UsersRouter
from app.api.v1.APIPoetry import router as PoetryRouter

app = FastAPI()

app.include_router(UsersRouter)
app.include_router(PoetryRouter)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)