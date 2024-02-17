from confluent_kafka import Producer
import time
import cv2
import os

# Kafka broker configuration
bootstrap_servers = 'broker:29092'
topic = 'url_stream_topic'

# Kafka producer configuration
producer_conf = {
    'bootstrap.servers': bootstrap_servers,
}

def delivery_callback(err, msg):
    if err:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

def delivery_callback(err, msg):
    if err:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

def main():
    # Create Kafka producer
    producer = Producer(producer_conf)

    # OpenCV video capture
    video_path= "./videos/video1.mp4"
    vcap = cv2.VideoCapture(video_path)
    # vcap = cv2.VideoCapture("http://192.168.1.6:8080", cv2.CAP_FFMPEG)

    while True:
        ret, frame = vcap.read()
        if not ret:
            print("Error reading frame")
            break

        # Convert frame to bytes
        frame = cv2.resize(frame, (640, 640))
        _, img_bytes = cv2.imencode('.jpg', frame)
        print("frame sent")

        # Produce the image bytes to Kafka topic
        producer.produce(topic, img_bytes.tobytes(), callback=delivery_callback)
        producer.poll(0)  # Trigger delivery report callback
        time.sleep(0.1)   # Adjust as needed to control the rate of data consumption

    vcap.release()
    producer.flush()
    # producer.close()

if __name__ == "__main__":
    main()
