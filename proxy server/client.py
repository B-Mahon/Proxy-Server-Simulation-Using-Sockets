#!/usr/bin/python3
import socket

FORMAT = "utf-8"
HEADER = 64

class Client:

    def __init__(self,port,ip):
        self.PORT = port
        self.SERVER = ip
        self.ADDR = (self.SERVER,self.PORT)
        self.DISCONNECT_MESSAGE= "!DISCONNECT"
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client.connect(self.ADDR)

    def send_message(self,msg):
        message = msg.encode(FORMAT)
        message_length = len(message)
        send_length = str(message_length).encode(FORMAT)
        send_length += b' ' *(HEADER - len(send_length))
        self.client.send(send_length)
        self.client.send(message)
        server_msg = self.client.recv(512).decode(FORMAT)
        return server_msg





