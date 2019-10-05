#как правильно записывать данные в сокет

def mysend(sock, msg):
    totalsent = 0
    while totalsent < len(msg):
        sent = sock.send(msg[totalsent:])
        if sent == 0:
            raise RuntimeError('broken')
        totalsent = totalsent + sent

        
#как правильно читать данные из сокета

def myreceive(sock, msglen):
    msg = ''
    while len(msg) < msglen:
        chunk = sock.recv(msglen - len(msg))
        print(chunk)
        if str(chunk) == '':
            raise RuntimeError('broken')
        msg = msg + str(chunk)
    return msg

#пример tcp подключения со стороны клиента

import socket
req = b"I change my work soon!"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 1234))
s.send(req)
rsp = myreceive(s, 1024)
print(rsp)
s.close()
