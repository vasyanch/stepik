#пример tcp подключения со стороны сервера

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 1234))
s.listen(10)
while True:
     conn, addr = s.accept() # conn - сокет для работы с конкретным  клиентом 
     while True:            # addr - IP-адрес конкретного клиента 
         data = conn.recv(1024)
         if not data: break
         conn.send(data)
     conn.close()
