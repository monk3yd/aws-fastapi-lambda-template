### Create IAM Lambda execution role using boto3

import boto3
import json
import os

from datetime import datetime
from loguru import logger

# ------------- AWS Settings ----------------

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
PROJECT_NAME = os.getenv("PROJECT_NAME")

# ======================================


def main():

    iam = boto3.client(
        "iam",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name="us-east-1",
    )

    role_name = generate_role_name(PROJECT_NAME)
    role_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "",
                "Effect": "Allow",
                "Principal": {"Service": "lambda.amazonaws.com"},
                "Action": "sts:AssumeRole",
            }
        ]
    }

    response = iam.create_role(
        RoleName=f"LambdaBasicExecution{role_name}",
        AssumeRolePolicyDocument=json.dumps(role_policy),
    )
    logger.info(f"IAM create role response: {response}")

    # Save role data
    with open("scripts/data/iam_role.json", "w") as file:
        file.write(json.dumps(response, default=serialize_datetime))

def generate_role_name(project_name):
    """Generate automatic role name from project name"""
    role_names = [] 
    names = project_name.split("-")
    for name in names:
        name_part = name.capitalize()
        role_names.append(name_part)

    # Role name
    return "".join(role_names)


def serialize_datetime(obj):
    """Serialize datetime objects for JSON compatibility"""
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError("Type not serializable")


if __name__ == "__main__":
    main()
