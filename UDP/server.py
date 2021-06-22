# 服务端：
import socket
print("服务器已启动。。。。。。")
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)#UDP
s.bind(("127.0.0.1",555))#绑定服务端IP和port
while True:
    data,addr = s.recvfrom(1024)#接收客户端发送的消息
    content = addr[0] + ":" + str(addr[1]) + "-" + data.decode('utf8')
    print(content)#输出格式化后的客户端消息
    s.sendto(content.encode('utf8'),addr)
