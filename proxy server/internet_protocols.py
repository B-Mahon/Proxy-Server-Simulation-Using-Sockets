import socket
import threading

HEADER = 64
FORMAT = "utf-8"

def message_protocol(conn,message):
    message_length = len(message)
    message_length = str(message_length).encode(FORMAT)
    message_length += b' ' *(HEADER - len(message_length))
    conn.send(message_length)
    conn.send(message.encode(FORMAT))

def send_ack(conn):
    message_protocol(conn,"ACK")