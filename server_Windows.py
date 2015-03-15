import socket
import sys
from threading import *
import Tkinter
from xml.dom import minidom
from pymouse import PyMouse

HOST = 'localhost'
PORT = 8888

connId = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #for IPv4 and TCP

try:
	s.bind( (HOST, PORT) ) #port explicitly for defined IP
except socket.error: #catch socket error
	print "Failed To Create Socket. " + str(msg[0])
	s.close()
	sys.exit()

s.listen(10) #backlog = 10

print "listening..."

while 1:
	conn, addr = s.accept() #accept() returns conn socket and address at other end
	print 'Connected with', addr[0], str(addr[1]),"		id:",connId

	connId+=1
	threadNewConnect  = Thread(target=clientThread, args=(conn, connId))
	threadNewConnect.start()

def clientThread(conn, cid):
	msg = 'Welcome to the server: ' + str(cid)
	conn.send(str.encode(msg))

	while True:
		data = conn.recv(1024)
		# reply = str(data)
		if not data:
				break
		print (data.decode('utf-8'))
		conn.send(data)
conn.close() #new connection socket
s.close() #searching socket
		#m = PyMouse()
		#x_dim, y_dim = m.screen_size()
		#m.click(x_dim/2, y_dim/2, 1)
		#conn.sendall(data)
	#conn.close()
