from confluent_kafka import Consumer
from flask import Flask, render_template, Response

app = Flask(__name__)

# Initialize Kafka consumer
c = Consumer({
    'bootstrap.servers': 'broker:29092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})
c.subscribe(['url_stream_topic'])

def generate_video():
    while True:
        msg = c.poll(1.0)

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
c.close()
