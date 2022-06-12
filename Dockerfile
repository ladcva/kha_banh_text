FROM python:3.9-alpine

WORKDIR /app

COPY . .

EXPOSE 5006

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["flask", "run"]
