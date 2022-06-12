FROM python:3.9-alpine

WORKDIR /app

EXPOSE 5005

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["flask", "run"]
