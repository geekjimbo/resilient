import Pyro4
from twisted.internet import reactor
from twisted.web import resource, server
import json

class consumer1(resource.Resource):
    isLeaf = True
    def render_GET(self, request):
        uri = "PYRONAME:consumers.consumer1"
        client = Pyro4.Proxy(uri)
        print("::: call is consumer1 ")
        print(client.call())
        request.responseHeaders.addRawHeader(b"Content-Type", b"application/json")
        return '{"message": "OK"}'.encode('utf-8')

class consumer2(resource.Resource):
    isLeaf = True
    def render_GET(self, request):
        uri = "PYRONAME:consumers.consumer2"
        client = Pyro4.Proxy(uri)
        print("::: call is consumer2 ")
        print(client.call())
        request.responseHeaders.addRawHeader(b"Content-Type", b"application/json")
        return '{"message": "OK"}'.encode('utf-8')

class consumer3(resource.Resource):
    isLeaf = True
    def render_GET(self, request):
        uri = "PYRONAME:consumers.consumer3"
        client = Pyro4.Proxy(uri)
        print("::: call is consumer3")
        print(client.call())
        request.responseHeaders.addRawHeader(b"Content-Type", b"application/json")
        return '{"message": "OK"}'.encode('utf-8')

class consumer4(resource.Resource):
    isLeaf = True
    def render_GET(self, request):
        uri = "PYRONAME:consumers.consumer4"
        client = Pyro4.Proxy(uri)
        print("::: call is consumer4")
        print(client.call())
        request.responseHeaders.addRawHeader(b"Content-Type", b"application/json")
        return '{"message": "OK"}'.encode('utf-8')

site1 = server.Site(consumer1())
site2 = server.Site(consumer2())
site3 = server.Site(consumer3())
site4 = server.Site(consumer4())

try:
    reactor.listenTCP(8000, site1)
    reactor.listenTCP(8001, site2)
    reactor.listenTCP(8002, site3)
    reactor.listenTCP(8003, site4)
    reactor.run()
except:
    print("::: services up!")
