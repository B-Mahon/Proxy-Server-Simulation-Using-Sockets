#!/usr/bin/python3
from client import Client 

def main():
    #create client and connect to the proxy server 
    print("Connecting to PROXY SERVER.....") 
    client = Client(5552,"127.0.0.1")
    #send message to the proxy server to forward to target server
    print("requesting content from target server")
    print(client.send_message("FORWARD"))
    #disconnect from proxy after receiving message back from target server 
    print("disconnecting from proxy server now....")
    disconnect_msg = client.send_message("!DISCONNECTED")
    print(disconnect_msg)

if __name__ == "__main__":
    main()

