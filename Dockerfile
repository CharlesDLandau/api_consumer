FROM python:3.6.2-alpine3.6
MAINTAINER Charles Landau charlesdlandau@gmail.com

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

CMD ["python", "main.py"]