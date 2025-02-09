import socketio
import eventlet
import base64
import os

# Create the "uploads" folder if it doesn't exist
if not os.path.exists("uploads"):
    os.makedirs("uploads")

sio = socketio.Server(cors_allowed_origins="*")  # can connect from anywhere so allows any active members to connect
app = socketio.WSGIApp(sio)

connected_users = {}  # stores users that are active


@sio.event
def connect(sid, environ):

    print(f"User {sid} connected")
    connected_users[sid] = {"sid": sid}  # Store user info
    sio.emit("user_connected", {"sid": sid}, skip_sid=sid)  # Notify others


@sio.event
def disconnect(sid):

    print(f"User {sid} disconnected")
    connected_users.pop(sid, None)
    sio.emit("user_disconnected", {"sid": sid}, skip_sid=sid)  # Notify others


@sio.event
def send_messages(sid, data):

    print(f"Received from {sid}: {data} successfully")
    sio.emit("received_message", data, skip_sid=sid)  # Send to others


@sio.event
def send_file(sid, data):

    filename = data["filename"]
    filecontent = base64.b64decode(data["file"])  # Convert your data to ASCII

    # Save file in uploads folder
    filepath = os.path.join("uploads", filename)
    with open(filepath, "wb") as file:
        file.write(filecontent)  # wb means it's a set of binary code open for writing

    print(f"File received from {sid}: {filename}")
    sio.emit("received_file", {"filename": filename}, skip_sid=sid)  # Send to all active users


if __name__ == "__main__":
    print("WebSocket server started on port 5000")
    eventlet.wsgi.server(eventlet.listen(("0.0.0.0", 5000)), app)
