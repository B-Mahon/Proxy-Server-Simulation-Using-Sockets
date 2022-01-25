#!/usr/bin/python3
from server import Server, HEADER, FORMAT,ACK_MESSAGE
from client import Client
import threading
import queue as Queue 
queue = Queue.Queue()

class Proxy(Server):
    
    def __init__(self):
        super().__init__()
        self.PORT = 5551
        self.ADDR = (self.SERVER,self.PORT)
        
    def handle_client(self,conn,addr):
        print(f"[INCOMING CONNECTION] {addr} has connected to server")
        connection = True 
        while connection:
            msg_length = conn.recv(HEADER).decode(FORMAT)   
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                if msg == "!DISCONNECTED":
                    print(f"[{addr}] is disconnecting from proxy....")
                    message_length = len(ACK_MESSAGE)
                    message_length = str(message_length).encode(FORMAT)
                    message_length += b' ' *(HEADER - len(message_length))
                    conn.send(message_length)
                    conn.send(ACK_MESSAGE.encode(FORMAT))
                    connection = False
                elif msg == "FORWARD":
                    thread = threading.Thread(target=self.forward_message, args=("REQUEST",))
                    thread.start()
                    print(f" [ACTIVE CONNECTIONS] {threading.active_count() -1}")     
                    thread.join()
                    content = queue.get()
                    print("CONTENT FROM QUEUE IS ",content)
                    content_length = len(content)
                    content_length = str(content_length).encode(FORMAT)
                    content_length += b' ' *(HEADER - len(content_length))
                    conn.send(content_length)
                    conn.send(str(content).encode(FORMAT))
                else:
                    print(f"message from [{addr}] is not valid for proxy please send FORWARD or !DISCONNECTED\n")
                    message_length = len(ACK_MESSAGE)
                    conn.send(str(message_length).encode(FORMAT))
                    conn.send(ACK_MESSAGE.encode(FORMAT))
        conn.close()     

    def forward_message(self,message):
        #instantiate client object connect to target server
        client = Client(5555,"127.0.0.1")      
        #send message to target server 
        content = client.send_message(message)
        print("Printing the content from thread",content)
        client.send_message("!DISCONNECTED")
        queue.put(content)
     
def main():
    proxy = Proxy()
    proxy.start_server()    

if __name__ == "__main__":
    main()


