import socket

HOST = '127.0.0.1'    # The remote host
PORT = 44444           # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect_ex((HOST, PORT))
    s.sendall(b"hello server!")
    data = s.recv(1024)
print('Received', repr(data))