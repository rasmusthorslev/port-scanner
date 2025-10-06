#!/usr/bin/env python3
import socket, sys

host = sys.argv[1]
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(1.0)
try:
    s.connect((host, port))
    print(f"{host}:{port} OPEN")
except:
    print(f"{host}:{port} CLOSED")
s.close()
