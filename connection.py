#documnent for creating connection objects 

class connection():
    def __init__(self, id, sock_tup, alias='anonymous'):
        self.id = id
        self.sock = sock_tup
        self.alias = alias

    def __repr__(self) -> str:
        return f"\n id: {self.id} \n address: {self.sock[0]} \n port: {self.sock[1]}\n alias: {self.alias}\n " 
