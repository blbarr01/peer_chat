import socket
import utils

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #open connection to the target addr
    s.connect((utils.get_ip(), 8000))
    msg = s.recv(1024)
    print(msg.decode())
