import json

from fastapi import FastAPI
from mangum import Mangum


app = FastAPI(title="api-manager-template")


@app.get("/")
def get_root():
    return {
        "statusCode": 200,
        "message": "root is working",
        "data": json.loads({})
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
