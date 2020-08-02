import Pyro4

nameserver=Pyro4.locateNS()
uri=nameserver.lookup("example.external_api")
print(uri)

uri1 = "PYRONAME:example.external_api"
client = Pyro4.Proxy(uri1)
print("::: call is ")
print(client.call())
