# from driver import motors, MAX_SPEED
import socket
import time
from json import loads as stringToDict

READ_SIZE = 256
DELIM = 'AAAAAA'

IP   = '10.245.178.93'
PORT = 5001

s = socket.socket()
s.connect((IP, PORT))

def main():
	tmp = ''
	while(True):
		tmp += s.recv(READ_SIZE).decode()
		tmp = tmp.split(DELIM)[0]
		try:
			msg = stringToDict(tmp)
			print("MSG: {}".format(msg))
			tmp = ''
			# motors.motor1.setSpeed(msg['left'])
			# motors.motor2.setSpeed(msg['right'])
		except: continue


if __name__ == '__main__':
	main()