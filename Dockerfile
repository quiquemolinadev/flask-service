# start by pulling the python image
FROM python:3.11.4-alpine

LABEL version="1.0"
LABEL description="Esta es una imagen personalizada de mi aplicación"
LABEL environment="Producción"

ENV MONGO_HOST="localhost"
ENV MONGO_USER="root"
ENV MONGO_PASSWORD="" 
ENV MONGO_DB="test"

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["view.py" ]
