'''TCP echo сервер, работающий одновременно с несколькими клиентами'''

import socket
import threading  # модуль для распараллеливания 

def server_alone(conn, addr):
    while True:
        data = conn.recv(1024)
        if str(data) == 'close':
            break
        if not data: break
        conn.send(data)
    conn.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)
while True:
    conn, addr = s.accept()
    t = threading.Thread(target=server_alone, args=(conn, addr))
    t.start()
