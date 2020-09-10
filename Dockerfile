FROM joyzoursky/python-chromedriver:3.7-selenium
USER root

RUN apt-get update

# install dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install -U pip
RUN pip install -r /requirements.txt