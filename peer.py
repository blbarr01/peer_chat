import argparse 
import socket
from utils import * 

parser = argparse.ArgumentParser(description='enter the port number for you\'re peers to connect to')
parser.add_argument('--port', '-p', type=int)

args = parser.parse_args()
connections = {}




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
                #make_conn()
                print('here are the connections')
            case 'exit':
                exit()
            case 'list':
                print('here are the connections')

