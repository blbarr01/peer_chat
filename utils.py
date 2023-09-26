import socket

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 1))  # connect() for UDP doesn't send packets
    local_ip_address = s.getsockname()[0]
    return local_ip_address


def prompt():
    print('enter options')
    print('---------------')
    print('info: display my ip')
    print('connect: make a new connection')
    print('list: list all connections')
    print('exit: terminate program')

