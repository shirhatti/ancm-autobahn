import os
from autobahntestsuite import echo
from twisted.internet import reactor
from twisted.internet.defer import Deferred

def run(ws_uri):
    res = echo.startServer(ws_uri, debug=False)
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
    ws_uri = "ws://127.0.0.1:" + str(aspnetcore_port)
    print(ws_uri)
    run(ws_uri)