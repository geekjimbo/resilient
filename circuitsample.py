from circuitbreaker import CircuitBreaker, CircuitBreakerMonitor
from datetime import datetime
import random
from time import sleep
import consul
from subprocess import Popen

def fallback():
	print(' / Fallback was called !', end='')
	cmd = "./init.sh >>log.log"
	try:
		Popen(cmd, shell=True)
	except:
		print("::: Services re-initiated !")
	return True

@CircuitBreaker(failure_threshold = 4, recovery_timeout = 10, name="my_circuit_breaker", fallback_function=fallback)
def consumers_health_status():
	c = consul.Consul()
	health = [ c.health.service(s)[1][0]["Checks"][1]["Status"] for s in c.agent.services()]
	unhealthy = [ u for u in health if u != "passing"]
	if len(unhealthy) > 0:
		raise Exception("Consumers services are down !")
	print("::: Health status = passed", end="")
	return True

if __name__ == "__main__":
	while True:
		print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), end='')
		cb = CircuitBreakerMonitor.get('my_circuit_breaker')

		try:
			consumers_health_status()
		except Exception as e:
			print(" Monitor state: {} opened: {} closed: {} failure_count: {} open_remaining: {}".format(cb.state, cb.opened, cb.closed, cb.failure_count, cb.open_remaining))
			print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), end='')
			print(' / {} {}'.format(type(e), e), end='')
		finally:
			print('')
			sleep(1)
