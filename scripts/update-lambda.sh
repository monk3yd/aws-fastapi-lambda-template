#!/bin/bash

LAMBDA_NAME="fastapi-lambda"
BUCKET_NAME="fastapi-lambda-sandbox"
KEY="code/lambda.zip"

aws lambda update-function-code --function-name ${LAMBDA_NAME} --s3-bucket ${BUCKET_NAME} --s3-key ${KEY}
