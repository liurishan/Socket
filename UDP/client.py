#客户端
import socket
import time
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)#UDP
addr =("127.0.0.1",555)#客户端发送连接请求
while True:
    message = input("请输入UDP消息：")
    s.sendto(message.encode('utf8'),addr)
    response,address = s.recvfrom(1024)  # 接收客户端发送的消息
    print(response.decode('utf8'))  # 输出格式化后的客户端消息