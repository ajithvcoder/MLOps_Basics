## Kafka Basic

For clean build

```docker compose -f docker-compose.yml build --no-cache```

**Usage**

    docker network create kafka-network 
    cd basics
    docker compose -f kafka-server\\docker-compose.yml up
    # After server starts
    docker compose -f docker-compose.yml up   

    # Enter producer container
    docker exec -it 49cb066bc158 bash
    python topic.py 
    python producer.py

    # Enter consumer container
    docker exec -it 49cb066bc158 bash
    python consumer.py

    docker compose -f kafka-server\\docker-compose.yml down
    docker compose -f docker-compose.yml down

zookeeper, server - topic, producer, consumer (group id)
distributed streaming service meaning ? 

you can create more servers, more topics, more producers, more consumers , your message is not lost it will be stored in queue even if consumer is not consuming

# Video streaming with Flask (open in browser with gmail account not orgainzation account)

    Debugging: Change the groupid in consumer

    docker network create kafka-network 
    cd basics
    docker compose -f kafka-server\\docker-compose.yml up
    # After server starts
    docker compose -f docker-compose.yml up   

    # Enter producer container
    docker exec -it 49cb066bc158 bash
    python topic.py 
    python producer.py

    # Enter consumer container
    docker exec -it 49cb066bc158 bash
    python consumer.py

    docker compose -f kafka-server\\docker-compose.yml down
    docker compose -f docker-compose.yml down
