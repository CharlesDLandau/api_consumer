FROM python:3.6.2-alpine3.6

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 8000