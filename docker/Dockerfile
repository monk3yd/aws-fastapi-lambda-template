ARG FUNCTION_DIR="/home/app"

FROM public.ecr.aws/lambda/python:3.9

ARG FUNCTION_DIR

# Create function directory
RUN mkdir -p ${FUNCTION_DIR}
WORKDIR ${FUNCTION_DIR} 

COPY ./requirements.txt ${FUNCTION_DIR} 
RUN pip3 install -r ${FUNCTION_DIR}/requirements.txt

COPY ./app/main.py ${FUNCTION_DIR} 

CMD ["app.handler"]
