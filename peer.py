import argparse 
import socket
from connection import *
from utils import * 

parser = argparse.ArgumentParser(description='enter the port number for you\'re peers to connect to')
parser.add_argument('--port', '-p', type=int)

args = parser.parse_args()
global con_id
con_id = 1
connections = set() 

def add_conn():
    ip = input("enter target IP address: ")
    port = input("enter target port: ")
    sock_tup = (ip, port)
    global con_id
    connections.add(connection(con_id, sock_tup))
    con_id +=1 

if __name__ == "__main__":
    port = args.port
    ip = get_ip()
    my_info= (ip, port)
    
    while True:
        prompt()
        sel = input('> ')
        match sel:
            case 'help':
                prompt()
            case 'connect':
                add_conn()
                print('here are the connections')
            case 'exit':
                exit()
            case 'list':
                print('here are the connections')
                print(connections)

