from autobahntestsuite import choosereactor
import os
import json

import autobahn
import autobahntestsuite

from autobahntestsuite import fuzzing
from autobahntestsuite import echo

from twisted.internet import reactor
from twisted.python import log, usage
from twisted.internet.defer import Deferred


# try:
#     ASPNETCORE_TOKEN = os.environ["ASPNETCORE_TOKEN"]
# except KeyError:
#     ASPNETCORE_TOKEN = ""



# class Simple(resource.Resource):
#     isLeaf = True
#     def render_GET(self, request):
#         return "Hello, world!"

# site = server.Site(Simple())
# reactor.listenTCP(ASPNETCORE_PORT, site)
# reactor.run()

def run(spec):
    """
    Start WS server
    """

    res = fuzzing.startServer(spec, 0)
    if isinstance(res, Deferred):
        def shutdown(_):
            reactor.stop()
        res.addBoth(shutdown)
    reactor.run()


if __name__ == '__main__':
    try:
        aspnetcore_port = int(os.environ["ASPNETCORE_PORT"])
    except KeyError:
        aspnetcore_port = 5000
    except ValueError:
        raise SystemExit
    spec = {}
    spec['url'] = "ws://127.0.0.1:" + str(aspnetcore_port)
    spec['outdir'] = './reports/clients'
    spec['cases'] = []
    spec['cases'].append("*")
    spec['exclude-cases'] = []
    spec['exclude-agent-cases'] = {}
    print spec
    run(spec)
