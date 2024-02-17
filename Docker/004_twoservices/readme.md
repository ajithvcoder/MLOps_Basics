docker run -d --name=my_container your_image_name:tag

docker build -t  producer001 .
docker build -t consumer001 .

docker network create my_network

docker run -d --name=myproducer -p 8088:8088 --network=my_network producer001
docker run -d --name=myconsumer -p 8089:8089 --network=my_network consumer001