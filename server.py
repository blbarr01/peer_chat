import socket
import utils

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((utils.get_ip(), 8000))
    s.listen(5)

    while True:
        c_sock, c_addr = s.accept()
        print(f'connection from {c_addr} made')
        c_sock.send(bytes('welcome to the server', 'utf-8'))

