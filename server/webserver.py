import os
from twisted.web import server, resource
from twisted.internet import reactor

class Simple(resource.Resource):
    isLeaf = True
    def render_GET(self, request):
        return "<html>Hello, world from Python!</html>"

site = server.Site(Simple())
try:
    aspnetcore_port = int(os.environ["ASPNETCORE_PORT"])
except KeyError:
    aspnetcore_port = 5000
reactor.listenTCP(aspnetcore_port, site)
reactor.run()