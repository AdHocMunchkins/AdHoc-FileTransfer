import socket

UDP_IP = ""
UDP_PORT = 54540

cs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cs.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
cs.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
cs.sendto('This is a test', ('192.168.1.255', 54540))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

network = set() 
while True:
	data, addr = sock.recvfrom(20)
	print addr
	# we add the ip to the list of IPs in the network	
	network.add(addr[0])
	print network
	# we also send our IP back to the client 
	# hardcoding our ip here, doesn't look like it's possible to discover our
	# IP in python when you're in an Ad-Hoc network
	cs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	cs.sendto('Heres my IP back buddy', (addr[0], 54540))
