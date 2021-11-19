# Dockerfile

# pull the official docker image
FROM python:3.10

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copy project
COPY . .

#CMD uvicorn main:app 0.0.0.0:8000
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

# If running behind a proxy like Nginx or Traefik add --proxy-headers
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers"]