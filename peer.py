import argparse 
import socket
import threading
from connection import *
from utils import * 

parser = argparse.ArgumentParser(description='enter the port number for you\'re peers to connect to')
parser.add_argument('--port', '-p', type=int, default=9000)

args = parser.parse_args()
global con_id
con_id = 1
connections = set() 


def add_conn():
    ip = input("enter target IP address: ")
    port = int(input("enter target port: "))
    sock_tup = (ip, port)
    global con_id
    connections.add(connection(con_id, sock_tup))
    con_id +=1 

def create_socket(peer):
    msg = input("enter your message > ")
    print(peer.sock)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(peer.sock)
        s.sendall(msg.encode('utf-8'))


def send_message():
    sel = input('would you like to see available peers? Y or N > ').capitalize()
    if sel == 'Y':
        print(connections)
    sel = input(" would you like to enter a new peer? Y or N > ").capitalize()
    if sel == 'Y':
        add_conn()
        print(connections)
    sel = int(input('enter the id of the peer you wish to connect to > '))
    
    # search for the connection 
    pp = None #potential peer 
    for connection in connections:
        if connection.id == sel:
            pp = connection
            break 

    print(pp)
    if pp is None:
        print('connection not found, aborting send')
    else:
        create_socket(pp)

def server_thread(addr, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((addr, port))
        s.listen()
        print(f'listening of port {port}')
        p_sock, p_addr = s.accept()
        full_msg = ''
        with p_sock:
            print(f'connection from {p_addr}')
            while True:
                partial = p_sock.recv(16)
                if len(partial) <= 0: break 
                full_msg += partial.decode()
            print(full_msg)

if __name__ == "__main__":
    port = args.port
    ip = get_ip()
    my_info= (ip, port)
    
    serv_t = threading.Thread(target=server_thread, args=(ip, port))
    serv_t.daemon = True
    serv_t.start()

    while True:
        prompt()
        sel = input('> ')
        match sel:
            case 'help':
                prompt()
            case 'info':
                print(my_info)
            case 'connect':
                add_conn()
                print('here are the connections')
            case 'exit':
                exit()
            case 'message':
                send_message()
            case 'list':
                print('here are the connections')
                print(connections)

