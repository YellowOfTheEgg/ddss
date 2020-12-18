FROM python:3.7.3

# Fix psutil installation problem
#RUN apt-install -y --update bash gcc libffi-dev libc-dev openssl-dev fortify-headers linux-headers libxml2-dev libxslt-dev python-dev libpq-dev && rm -rf /var/cache/apk/*
#RUN apk add --no-cache --virtual .build-deps gcc libc-dev make 

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add requirements
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt

# install requirements
RUN pip install -r requirements.txt

# add app
COPY . /usr/src/app
RUN chmod +x /usr/src/app/run.sh
RUN chmod +x /usr/src/app/run_tests.sh

ENV PYTHONPATH /usr/src/app

CMD ["sh", "/usr/src/app/run.sh"]
