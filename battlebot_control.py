import xbox
import time
from json import dumps as dictToJson
import socket

PORT = 5001
MAX_SPEED = 480
DEBOUNCE = 0.05
DELIM = 'AAAAAA'

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('',PORT))
print("Socket bound to port {}".format(PORT))
s.listen(1)
print("Socket listening...")

c, addr = s.accept()
print("Socket connection accepted!")

def calculate_speeds(diff_x, diff_y):
	x = diff_x * MAX_SPEED
	y = diff_y * MAX_SPEED
	return x-y, x+y


def main():
	ctrl = xbox.Joystick()
	inverted = False
	init_x, init_y = ctrl.leftStick()
	then = time.time()
	while(True):
		now = time.time()

		if ctrl.A() and now - then > 1:
			then = time.time()
			inverted = not inverted
			print("Inversion State: {}".format(inverted))

		if now - then > 0.05:
			curr_x, curr_y = ctrl.leftStick()
			weapon = ctrl.rightTrigger()
			left, right = calculate_speeds(curr_x-init_x, curr_y-init_y)
			command = dictToJson({'left': left, 'right': right, 'weapon': weapon*255})
			c.send((command + DELIM).encode())
			print("Command Sent: {}".format(command))
			then = time.time()

		time.sleep(DEBOUNCE)


if __name__ == '__main__':
	main()
