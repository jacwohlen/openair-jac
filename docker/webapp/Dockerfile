FROM ubuntu:latest
MAINTAINER Andreas Schmid <ikeark@gmail.com>

RUN apt-get update -y
RUN apt-get install -y python3-pip npm
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt

ENV OPENAIR_SECRET 50_Jahre_JAC
ENV FLASK_APP autoapp.py
ENV FLASK_DEBUG 0

# important for python3 (http://click.pocoo.org/5/python3)
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

RUN npm install
RUN npm run build

CMD ["flask", "run", "-h", "0.0.0.0"]
