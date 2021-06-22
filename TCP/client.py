#客户端
import socket
# while True:
s = socket.socket()#实例化一个socket对象
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)#TCP
# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)#UDP
s.connect(("127.0.0.1",555))#客户端发送连接请求
success = s.recv(1024).decode('utf8')#客户端接收成功提示消息
print(success)#客户端打印接收到的消息
while True:
    message = input("请输入内容：")#客户端键盘输入消息
    s.send(message.encode('utf8'))#将输入的消息发送给服务端
    content = s.recv(1024).decode('utf8')#接收服务端转发的消息
    print(content)#打印接收的消息