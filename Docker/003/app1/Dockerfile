FROM python:slim-bookworm

RUN apt update -y
WORKDIR /app
EXPOSE 8085
COPY . /app 
RUN pip3 install -r requirements.txt

CMD python app.py