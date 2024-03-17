## Kafka Basic

what is poll in kafka producer
.poll(0): The method poll is invoked with an argument of 0. This argument specifies the maximum amount of time 
(in seconds) the call will block waiting for event callbacks. A value of 0 means the call is non-blocking; 
it will check for any available callbacks to trigger (such as delivery reports) and return immediately.



What is poll in kafka consumer

The poll method is used to fetch records from Kafka. The argument passed to poll is a timeout value in seconds, indicating how long the poll call will block if data is not immediately available in the buffer. If this timeout expires without any new data, poll will return None (or an empty list, depending on the client library).

1.0 as the argument specifies that the consumer will wait up to 1 second for new data to become available.


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

    GO to http://localhost:5000/video_feed url
