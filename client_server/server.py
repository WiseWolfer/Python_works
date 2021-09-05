import socket

HOST = '127.0.0.1'
PORT = 50007
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print(conn, "\n")
    print(addr)
    with conn:
        print('Connected by', addr)
        while True:
           data = conn.recv(1024)
           if not data:
              break
           conn.sendall(data)
