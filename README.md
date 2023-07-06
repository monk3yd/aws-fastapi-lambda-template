[AWS FastAPI Lambda - Medium](https://medium.com/towards-data-science/fastapi-aws-robust-api-part-1-f67ae47390f9)
[AWS FastAPI Lambda Security - Medium](https://towardsdatascience.com/fastapi-aws-secure-api-part-2-1123bff28b55)

## Steps to follow for CICD setup:

1. Create a new lambda project github repository by using [aws-fastapi-lambda-template](https://github.com/monk3yd/aws-fastapi-lambda-template)

2. Clone new lambda project github repository into local machine (project name example: github-to-lambda)
```bash
git clone git@github.com:monk3yd/github-to-lambda.git
```

3. Create virtualenv
```bash
pip3 install virtualenv

# This will create a new directory called myenv in your current directory, which contains a new Python environment.
virtualenv myenv

# create venv dir with specific version of Python taken from conda
virtualenv -p ~/anaconda3/bin/python3.9 venv

# This will activate the virtual environment and change your shell's prompt to indicate that you're using the new environment.
source myenv/bin/activate 
```

4. Install required dependencies
```bash
pip3 install -r requirements.txt

# Useful for scripts configurations
export AWS_ACCOUNT_ID="134284459147"
export AWS_REGION_NAME="us-east-1"
export PROJECT_NAME="github-to-lambda"
export AWS_ACCESS_KEY_ID="aaabbcc0001122233"
export AWS_SECRET_ACCESS_KEY="aaabbcc0001122233"
```

5. Test API locally
```bash
uvicorn main:app --reload
```
See [docs](http://localhost:8000/docs)

6. Create ECR for new lambda project
```bash
bash scripts/create-ecr-repo.sh
```

7. Deploy init docker images (main/experimental) to ECR
```bash
bash scripts/deploy-images-to-ecr.sh
```

8. Create lambda functions (main/experimental) and link them to respective image within ECR
```bash
python3 scripts/create_lambdas.py
```

* NOTE: if the AWS account is new we need to first run:
```bash
python3 scripts/create_iam_lambda_execution.py
```

9. Define github actions secrets within project repository:
  - AWS_ACCOUNT_ID
  - AWS_ACCESS_KEY_ID
  - AWS_SECRET_ACCESS_KEY
  - REGION_NAME
  - PROJECT_NAME

10. Push to main or experimental branches within github, the lambda function will update accordingly

11. Create REST API in API Gateway through AWS console
> Now we need to configure the integration point for our request methods. To use a Lambda function as our integration point for ANY type of request (i.e., GET, POST, PATCH, DELETE, etc.), we will create a Method (to handle the root path) and a child Resource (to handle all child paths). We will configure them to handle any requests made to API Gateway by using the Lambda proxy integration [1].

  - Create method
  - Create resource

12. Configure lambda function as a proxy to forward requests from API Gateway to Amazon Lambda

13. Deploy API
> Since our Lambda is now configured, we can deploy the API. We can name it dev stage. The deployment is crucial to make the Lambda function integration active.

14. Configure methods & resources to require API key

15. Create API key

16. Create API usage plan

17. Redeploy

## Resources
See the [AWS SAM developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) for an introduction to SAM specification, the SAM CLI, and serverless application concepts.

Next, you can use AWS Serverless Application Repository to deploy ready to use Apps that go beyond hello world samples and learn how authors developed their applications: [AWS Serverless Application Repository main page](https://aws.amazon.com/serverless/serverlessrepo/)

