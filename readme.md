a simple peer to peer chat app

the application follows a decentralized peer-to-peer structure. 
there is no central server; instead, each program instance operates as as server and client
able to send simple text messages to peers within the local network 

program usage 
-----------
run ifconfig to learn the local IPv4 address 
launch using python3 
python3 peer.py -a "alias" -p port# 
two arguements may be provided:
  an alias for the user 
  a port number 
  alias defaults to anonymous 
  port defaults to 9000
the program will request the local IPv4 address and port# of any peers the user wishes to connect to 
and stores these connections for the user to use. 
