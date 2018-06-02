import signal
import sys
from time import sleep

def handler(signal, frame):
	"""function call when programme is signaled"""
	print("the time come to an end : signal : {}"\
	.format(signal))
	sys.exit(0)

signal.signal(signal.SIGINT, handler)

print("infinity loop !")
char="-\\|/"
while True:
	for c in char:
		print(c, sep='', end='\r')
		sleep(0.1)
	continue
