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
        wait_for_reply = True
        while wait_for_reply:
            msg_length = (self.client.recv(HEADER).decode(FORMAT))
            if msg_length:
                msg_length = int(msg_length)
                print(msg_length)
                message = (self.client.recv(msg_length).decode(FORMAT))
                print(message)
                wait_for_reply = False 
        return message

def main():
    client = Client(5550,'127.0.0.1')
    client.send_message("FORWARD")   

if __name__ == "__main__":
    main()



