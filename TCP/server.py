#服务端
import socket
print("服务器已启动，处于监听等待状态。。。。。。")
# s = socket.socket()#实例化一个socket对象
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)#TCP
s.bind(("127.0.0.1",555))#绑定服务端IP和port
s.listen(5)#服务端监听等待队列长度
# while True:#循环接收客户端连接请求
c,address = s.accept()#接收客户端请求，返回服务端与客户端建立的socket连接，并返回客户端的ip和port
c.send("连接成功！".encode('utf8'))#非客户端发送“连接成功！”的消息
with open("log.txt",'a') as f:#打开日志文件
    while True:
        data = c.recv(1024).decode('utf8')#接收客户端发送的消息
        messgae = address[0] + ":" + str(address[1]) + ":" + data#格式化消息
        print(messgae)#输出格式化后的客户端消息
        c.send(messgae.encode('utf8'))#向客户端发送格式化后的消息
        # with open("log.txt",'a') as f:#打开日志文件
        f.write(messgae + '\n')#写入消息日志
