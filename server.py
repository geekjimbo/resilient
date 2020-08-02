import Pyro4
from external_api import looping

@Pyro4.expose
class consumer1(object):
	def call(self):
		return looping()

@Pyro4.expose
class consumer2(object):
	def call(self):
		return "consumer 2"

@Pyro4.expose
class consumer3(object):
	def call(self):
		return "consumer 2"

@Pyro4.expose
class consumer4(object):
	def call(self):
		return "consumer 2"

daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
uri = daemon.register(consumer1)
ns.register("consumers.consumer1", uri)
uri = daemon.register(consumer2)
ns.register("consumers.consumer2", uri)
uri = daemon.register(consumer3)
ns.register("consumers.consumer3", uri)
uri = daemon.register(consumer4)
ns.register("consumers.consumer4", uri)

print("::: Daemons ready.")
daemon.requestLoop()
