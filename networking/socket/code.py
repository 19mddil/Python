#browsers follow http protocol to talk to web servers at port 80 which we can simulate in command line via telnet
import socket
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    #mysock.connect( ('http://py4e-data.dr-chuck.net/',80) )
    mysock.connect(('data.pr4e.org',80))
except:
    print("Error")
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
while True:
    data = mysock.recv(512)
    if(len(data) < 1):
        break
    print(data.decode())
mysock.close()
