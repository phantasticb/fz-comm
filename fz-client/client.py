import socket

HOST = '127.0.0.1'
PORT = 42069

TARGET = None
CSIGN = None


def readMSG(data):
    print(data.decode())


print("FZ Client 1.0")
CSIGN = input("Enter callsign: ")


def connectFZ():
    s.connect((HOST, PORT))
    s.sendall(CSIGN.encode())


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    connectFZ()
    print("Connected to central FZ Server")

    while True:
        action = input("FZ-D: ")
        if action == "quit":
            break
        elif action == "list":
            print("FZ Server found these targets:")
            s.send(b'list-request')


