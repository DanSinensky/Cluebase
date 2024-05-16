# base image
FROM python:3.7.2-alpine

# install dependencies
RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev libffi-dev openssl-dev && \
    apk add postgresql-dev && \
    apk add netcat-openbsd

# set working directory
WORKDIR /usr/src/app

# Copy the requirements file into the container at /app
COPY requirements.txt /usr/src/app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# add entrypoint.sh
COPY entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# add app
COPY . /usr/src/app

# run server
CMD ["/usr/src/app/entrypoint.sh"]
