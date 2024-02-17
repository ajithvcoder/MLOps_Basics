basic:
env: trainingpipeline

docker network create kafka-network 
docker compose -f kafka-server\\docker-compose.yml up

python topic.py 

python producer.py

zookeeper, server - topic, producer, consumer (group id)
distributed streaming service meaning ? 

you can create more servers, more topics, more producers, more consumers , your message is not lost it will be stored in queue even if consumer is not consuming

# Video streaming 

python topic.py 

python producer.py

python consumer.py

