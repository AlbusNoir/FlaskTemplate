# This is a basic docker file to get a flask app running. Change it as needed. 
# Reference: https://docs.docker.com/reference/dockerfile/
FROM python:3.12

# Copy local reqs to app and set app's work directory
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app

# Install requirements
RUN pip install -r requirements.txt

# Copy local files to app
COPY . /app

# Default exec run on start
ENTRYPOINT ["python"]

# Command params passed to the entrypoint
CMD ["app.py"]