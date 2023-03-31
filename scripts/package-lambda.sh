#!/bin/bash

### Package app and venv (depedencies)

ROOT_DIR="${HOME}/GDrive/theLab/projects/microservices-aws/fastapi-lambda-aws/"
VENV_DIR="${ROOT_DIR}/venv/lib/python3.9/site-packages"

# zip venv depedencies
cd ${VENV_DIR} && zip -r9 "${ROOT_DIR}/lambda.zip" .

# zip app directory
cd "${ROOT_DIR}/app" && zip -g ../lambda.zip -r .

