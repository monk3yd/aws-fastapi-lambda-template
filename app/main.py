# https://medium.com/towards-data-science/fastapi-aws-robust-api-part-1-f67ae47390f9

# For local run: uvicorn main:app --reload
# Check: http://localhost:8000/docs

import json
import sys

from fastapi import FastAPI
from mangum import Mangum


app = FastAPI(title="fastapi-lambda-template")


@app.get("/")
def get_root():
    return {
        "statusCode": 200,
        "message": "root GET method is working",
    }


@app.post("/")
def post_to_root():
    return {
        "statusCode": 200,
        "message": "root POST method is working"
    }


@app.get("/{var}")
def search_var(var: str = None):
    if var is None:
        return {
            "statusCode": 400,
            "message": "Please enter var."
        }

    # TODO: Validate var

    return {
        "statusCode": 200,
        "message": "200OK",
        "data": json.dumps({})
    }


handler = Mangum(app)
