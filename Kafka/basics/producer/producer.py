from confluent_kafka import Producer
import time
p = Producer({'bootstrap.servers': 'broker:29092'})

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

for _ in range(0, 100):
    # Trigger any available delivery report callbacks from previous produce() calls
    p.poll(0)
    data = "hi " + str(_)
    # Asynchronously produce a message. The delivery report callback will
    # be triggered from the call to poll() above, or flush() below, when the
    # message has been successfully delivered or failed permanently.
    p.produce('topic1', data.encode('utf-8'), callback=delivery_report)
    time.sleep(1)

# Wait for any outstanding messages to be delivered and delivery report
# callbacks to be triggered.
p.flush()