#!/usr/bin/python3
import socket 
def scan(targetIp,port):
    #create socket object 
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = client.connect_ex((targetIp,port))
    if result==0:
        print(f'port {port} is open')
    else:
        print(f'Port {port} is not open')
if __name__=='__main__':
    target= 'testasp.vulnweb.com'
    scan(target,80)