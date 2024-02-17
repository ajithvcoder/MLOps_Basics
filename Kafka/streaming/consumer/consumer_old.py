from confluent_kafka import Consumer
import cv2
import numpy as np

# Kafka broker configuration
bootstrap_servers = 'broker:29092'
topic = 'url_stream_topic'

# Kafka consumer configuration
consumer_conf = {
    'bootstrap.servers': bootstrap_servers,
    'group.id': 'image_consumer_group',
    'auto.offset.reset': 'earliest'
}

def main():
    # Create Kafka consumer
    consumer = Consumer(consumer_conf)
    consumer.subscribe([topic])

    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue

        # Convert message value (image bytes) to numpy array
        img_bytes = np.frombuffer(msg.value(), dtype=np.uint8)

        # Decode image
        img = cv2.imdecode(img_bytes, cv2.IMREAD_COLOR)
        print(img.shape)
        # Display image
        # cv2.imshow('Image from Kafka producer', img)
        # cv2.waitKey(1)

    consumer.close()

if __name__ == "__main__":
    main()
