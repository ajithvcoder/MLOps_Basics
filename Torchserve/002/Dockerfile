FROM pytorch/torchserve:latest
EXPOSE 5000
USER root
WORKDIR /usr/app
# RUN apt-get update -y
# RUN apt-get install ffmpeg libsm6 libxext6  -y
ADD ./requirements.txt ./

RUN pip3 install  -r requirements.txt
# RUN pip install  eventlet

EXPOSE 5000

ADD ./ ./

CMD tail -f /dev/null