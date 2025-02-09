import socketio
import base64

sio = socketio.Client()  # Create a Socket.IO client instance


@sio.event
def connect():

    print("Connected to Server")



@sio.event
def disconnect():

    print("Disconnected From Server")


@sio.event
def received_message(data):

    print(f"New message received: {data}")


@sio.event
def received_file(data):

    print(f"New file received: {data['filename']}")


def send_message(text):

    sio.emit("send_messages", text)  # Ensure it matches the server's event name


def send_file(filepath):
    # Sends a file to the server by encoding it in Base64
    with open(filepath, "rb") as file:
        encoded = base64.b64encode(file.read()).decode("utf-8")
        # Here the client side encodes the data and specifies it will be decoded in utf-8, which is text format

    sio.emit("send_file", {"filename": filepath.split("/")[-1], "file": encoded})
    # filepath.split("/")[-1] accesses the last element in the path, which is the filename


def start_client():

    sio.connect("http://localhost:5000")


# Start the client
start_client()
#send_message("Hello, World!")
#send_file("C:/Users/Tab's/PycharmProjects/Chatty/images/ulysse.png")
