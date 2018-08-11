import Pyro4

from StringUtil import StringUtil

util = StringUtil()

daemon = Pyro4.Daemon()           # make a Pyro daemon
ns = Pyro4.locateNS()             # find the name server
uri = daemon.register(StringUtil) # register the greeting maker as a Pyro object
ns.register("StringUtil", uri)    # register the object with a name in the name server

print("Ready.")
daemon.requestLoop()              # start the event loop of the server to wait for calls
