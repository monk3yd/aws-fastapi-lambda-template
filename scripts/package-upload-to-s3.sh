#!/bin/bash

### Upload zip file to S3 for preparing lambda deploy 

ROOT_DIR="${HOME}/GDrive/theLab/projects/microservices-aws/fastapi-lambda-aws/"
BUCKET_NAME="fastapi-lambda-sandbox/code"

cd ${ROOT_DIR}
aws s3 cp lambda.zip s3://${BUCKET_NAME}/lambda.zip
