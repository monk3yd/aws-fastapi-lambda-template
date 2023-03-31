#!/bin/bash

ROOT_DIR="${HOME}/GDrive/theLab/projects/microservices-aws/fastapi-lambda-aws/"
VENV_DIR="${ROOT_DIR}/venv/lib/python3.9/site-packages"

BUCKET_NAME="fastapi-lambda-sandbox/code"


### Package app and venv (depedencies)

# zip venv depedencies
cd ${VENV_DIR} && zip -r9 "${ROOT_DIR}/lambda.zip" .

# zip app directory
cd "${ROOT_DIR}/app" && zip -g ../lambda.zip -r .


### Upload zip file to S3 for preparing lambda deploy 
cd ${ROOT_DIR}
aws s3 cp lambda.zip s3://${BUCKET_NAME}/lambda.zip

