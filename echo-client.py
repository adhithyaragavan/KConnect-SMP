import socket
HOST = "127.0.0.1"
PORT = 65432

#intitiating connection
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))

#data exchange
    s.sendall(b"Hello, World")
    data = s.recv(1024)

print(f"Recieved {data}")