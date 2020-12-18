FROM python:3.8.1-buster

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip3 install -r requirements.txt

COPY . /usr/src/app
RUN chmod +x /usr/src/app/run.sh

ENV PYTHONPATH /usr/src/app




CMD ["sh", "/usr/src/app/run.sh"]


