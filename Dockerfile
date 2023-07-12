FROM python:3.10-slim

RUN apt-get update && apt-get install -y build-essential postgresql-server-dev-all

RUN pip install --upgrade pip
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
ENTRYPOINT [ "python3" ]

EXPOSE 5000

CMD ["-m", "flask", "run", "--host=0.0.0.0"]