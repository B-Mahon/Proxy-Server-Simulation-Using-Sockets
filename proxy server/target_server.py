#!/usr/bin/python3
from server import Server

target_server = Server()
target_server.start_server()

def main():
    server = Server()
    server.start_server()    

if __name__ == "__main__":
    main()