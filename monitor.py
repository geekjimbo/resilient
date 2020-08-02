from circuitbreaker import CircuitBreakerMonitor
from datetime import datetime
import random
from time import sleep

if __name__ == "__main__":
	while True:
		print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), end='')

		print(" Registered Circuits = {}".format(CircuitBreakerMonitor.get_circuits()) )
		sleep(1)
