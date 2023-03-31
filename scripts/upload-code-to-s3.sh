#!/bin/bash

BUCKET_NAME="medium-aws"
ROOT_DIR="${HOME}/GDrive/theLab/projects/microservices-aws/fastapi-lambda-aws/"

cd ${ROOT_DIR}

aws s3 cp lambda.zip s3://${BUCKET_NAME}/lambda.zip
