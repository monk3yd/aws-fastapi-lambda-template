# https://medium.com/towards-data-science/fastapi-aws-robust-api-part-1-f67ae47390f9

# For local run: uvicorn main:app --reload
# Check: http://localhost:8000/docs

from pydantic import BaseModel
from fastapi import FastAPI
from mangum import Mangum

from loguru import logger


app = FastAPI(title="fastapi-lambda-template")


# Move to models.py or models/ dir as necessary
class User(BaseModel):
    id: int
    username: str

@app.get("/user/{id}")
def read_user_info(id: int):
    logger.debug(f"Read user ID: {id}")
    return {
        "statusCode": 200,
        "message": "User found",
    }


@app.post("/user")
def create_user(user: User):
    return {
        "statusCode": 200,
        "message": "User created",
        "user": user.dict()
    }


@app.get("/")
def root():
    return {
        "statusCode": 200,
        "message": "root GET method OK"
    }

handler = Mangum(app)
