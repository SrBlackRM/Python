import socket

target_port = 4444

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#criamos um objeto socket e passamos os parametros AF_INET e SOCK_STREAM
#AF_INET significa que usaremos IPv4
#SOCK_STREAM siginifica que que o client sera TCP


target_host = '187.122.5.52'

try:
	client.connect((target_host,target_port))

	client.send("")
	response = client.recv(4096)
except:
	print "ERRO"

print response
