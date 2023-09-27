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

def create_socket(peer):
    pass


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

