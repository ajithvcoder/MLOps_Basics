from confluent_kafka import Consumer
from flask import Flask, render_template, Response

app = Flask(__name__)

# Kafka broker configuration
bootstrap_servers = 'broker:29092'
topic = 'url_stream_topic'

# Kafka consumer configuration
consumer_conf = {
    'bootstrap.servers': bootstrap_servers,
    'group.id': 'image_consumer_group3',
    'auto.offset.reset': 'earliest'
}

def generate_video():
    consumer = Consumer(consumer_conf)
    consumer.subscribe([topic])
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + msg.value() + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_video(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

# Close the Kafka consumer when the Flask app is terminated
# c.close()
