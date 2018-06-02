import random
import sys
import time
from threading import Thread, RLock

lock = RLock()

class Display(Thread):

	def __init__(self, word):
		Thread.__init__(self)
		self.word = word

	def run(self):
		i = 0
		while i < 5:
			with lock:
				for lettre in self.word:
					sys.stdout.write(lettre)
					sys.stdout.flush()
					attente = 0.2
					attente += random.randint(1, 60) / 100
					time.sleep(attente)
			i += 1

thread_1 = Display("holla")
thread_2 = Display("BONJOUR")

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()
