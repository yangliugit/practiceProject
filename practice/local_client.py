# -*- coding: utf-8 -*-
import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 建立连接:
# s.connect(('10.10.138.247', 1999))
# # 接收欢迎消息:
# print(s.recv(1024).decode('utf-8'))
# for data in [b'Michael', b'Tracy', b'lijun']:
#     # 发送数据:
#     s.send(data)
#     print(s.recv(1024).decode('utf-8'))
# s.close()


def send_password(word):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('10.10.133.175', 1999))
    print(s.recv(1024).decode('utf-8'))
    s.send(bytes(word))
    print(s.recv(1024).decode('utf-8'))
    s.close()

send_password("asd")

