# https://medium.com/towards-data-science/fastapi-aws-robust-api-part-1-f67ae47390f9

# For local run: uvicorn main:app --reload
# Check: http://localhost:8000/docs

import os
import uvicorn

from pydantic import BaseModel
from fastapi import FastAPI
from mangum import Mangum

from loguru import logger


app = FastAPI(title="fastapi-lambda-template")

# TODO: CORS configuration (see: autotramite)

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
        "message": "root GET method OK",
        "env": os.getenv("KEY")
    }


# See: cotizador-seguros

# TODO: invoke lambda (sync)

# TODO: invoke lambda (async)

# TODO: EC2 server

# TODO: batch payload

# TODO: stepfunctions


handler = Mangum(app)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="debug", reload=True)
