#!/usr/bin/python3
import socket
import threading
HEADER = 64
FORMAT = 'utf-8'
ACK_MESSAGE = "[ACK]"

class Server:

    def __init__(self):    
        self.PORT = 5555
        self.SERVER = socket.gethostbyname("127.0.0.1")
        self.ADDR = (self.SERVER,self.PORT)
        self.DISCONNECT_MESSAGE = "!DISCONNECT"
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def handle_client(self,conn,addr):
        print(f"[INCOMING CONNECTION] {addr} has connected to server")
        connection = True 
        while connection:
            msg_length = conn.recv(HEADER).decode(FORMAT)   
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                if msg == "!DISCONNECTED":
                    print(f"[{addr}] has disconnected....")
                    conn.send(ACK_MESSAGE.encode(FORMAT))
                    connection = False
                elif msg == "REQUEST":
                    print(f"[{addr}] has requested content... sending content...")
                    conn.send("CONTENT".encode(FORMAT))
                else:
                    print(f"[{addr}] has sent {msg} acknowledging it now...")
                    conn.send(ACK_MESSAGE.encode(FORMAT))
        print(f"[{addr}] is closing connection to server")
        conn.close()        

    def start_server(self):
        self.server.bind(self.ADDR)
        print(f"[STARTING SERVER] {self.SERVER} is listening for incoming connections on port {self.PORT}")
        self.server.listen(1)
        while True:
            conn, addr = self.server.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn,addr))
            thread.start()
            print(f" [ACTIVE CONNECTIONS] {threading.active_count() -1}")


