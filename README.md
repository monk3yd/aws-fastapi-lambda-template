[AWS FastAPI Lambda - Medium](https://medium.com/towards-data-science/fastapi-aws-robust-api-part-1-f67ae47390f9)

1. Create virtualenv

2. Install required dependencies

```bash
cd app
pip3 install -r requirements.txt
```

3. Test API locally
```bash
uvicorn main:app --reload
```
See [docs](http://localhost:8000/docs)

4. Package code

```bash
#!/bin/bash

ROOT_DIR="${HOME}/GDrive/theLab/projects/microservices-aws/fastapi-lambda-aws/"
VENV_DIR="${ROOT_DIR}/venv/lib/python3.9/site-packages"


### Package app and venv (depedencies)

# zip venv depedencies
cd ${VENV_DIR} && zip -r9 "${ROOT_DIR}/lambda.zip" .

# zip app directory
cd "${ROOT_DIR}/app" && zip -g ../lambda.zip -r .
```

5. Upload code to S3

```bash
#!/bin/bash

ROOT_DIR="${HOME}/GDrive/theLab/projects/microservices-aws/fastapi-lambda-aws/"
BUCKET_NAME="fastapi-lambda-sandbox/code"

### Upload zip file to S3 for preparing lambda deploy 

cd ${ROOT_DIR}
aws s3 cp lambda.zip s3://${BUCKET_NAME}/lambda.zip
```

6. Create lambda function through AWS console, set handler as main.handler and set new role with basic lambda permissions.

7. Update the lambda function to make sure it uses the packaged code from S3
```bash

#!/bin/bash
LAMBDA_NAME="fastapi-lambda"
BUCKET_NAME="fastapi-lambda-sandbox"
S3_KEY="code/lambda.zip"

aws lambda update-function-code --function-name ${LAMBDA_NAME} \
--s3-bucket ${BUCKET_NAME} --s3-key ${S3_KEY}
```

8. Create REST API in API Gateway through AWS console
> Now we need to configure the integration point for our request methods. To use a Lambda function as our integration point for ANY type of request (i.e., GET, POST, PATCH, DELETE, etc.), we will create a Method (to handle the root path) and a child Resource (to handle all child paths). We will configure them to handle any requests made to API Gateway by using the Lambda proxy integration [1].

  - Create method
  - Create resource

9. Configure lambda function as a proxy to forward requests from API Gateway to Amazon Lambda

10. Deploy API
> Since our Lambda is now configured, we can deploy the API. We can name it dev stage. The deployment is crucial to make the Lambda function integration active.


## Resources
See the [AWS SAM developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) for an introduction to SAM specification, the SAM CLI, and serverless application concepts.

Next, you can use AWS Serverless Application Repository to deploy ready to use Apps that go beyond hello world samples and learn how authors developed their applications: [AWS Serverless Application Repository main page](https://aws.amazon.com/serverless/serverlessrepo/)

