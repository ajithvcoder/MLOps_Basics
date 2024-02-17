FROM python:3.10-slim

# USER ROOT
WORKDIR /usr/app
# RUN apt-get update && \
#   apt-get install -y net-tools

RUN apt-get update -y
ADD ./ ./
RUN pip3 install  -r requirements.txt

# RUN python create_topic.py

CMD tail -f /dev/null
