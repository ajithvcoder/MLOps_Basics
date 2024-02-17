from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import threading
import time

app = Flask(__name__)
socketio = SocketIO(app)

def background_task():
    while True:
        time.sleep(1)  # Generate a message every second
        message = f"Message from background task at {time.strftime('%H:%M:%S')}"
        socketio.emit('server_message', {'data': message}, namespace='/')

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect', namespace='/')
def handle_connect():
    print('Client connected')

if __name__ == '__main__':
    bg_thread = threading.Thread(target=background_task)
    bg_thread.daemon = True
    bg_thread.start()
    socketio.run(app, debug=True)
