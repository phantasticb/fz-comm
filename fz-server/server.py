import socket

HOST = '127.0.0.1'
PORT = 42069

clients = []

s = socket.socket()
s.bind((HOST, PORT))

print("Socket bound to " + HOST + ":" + str(PORT));

s.listen(5)

running = True

def addClient():
    (c, a) = s.accept()
    callsign = c.recv(1024)
    print(callsign.decode())
    clients.append([(c, a), callsign.decode()])
    print(str(clients[0][0][1]) + " connected, callsign: " + callsign.decode())

while running:
    addClient()
    break
