#Creation of an docker-image based on python-buster
FROM python:3.8.1-buster

#set the working directory inside of the container
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

#copy the requirements.txt into the container and execute them
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip3 install -r requirements.txt

#copy the project folder into container and make it executable
COPY . /usr/src/app
RUN chmod +x /usr/src/app/run.sh
RUN chmod +x /usr/src/app/run_tests.sh

#set default project path
ENV PYTHONPATH /usr/src/app



#run run.sh
CMD ["sh", "/usr/src/app/run.sh"]


