import Pyro4

#from StringUtil import StringUtil

#util = StringUtil()

util = Pyro4.Proxy("PYRONAME:StringUtil")    # use name server object lookup uri shortcut

s = util.toUpperCase("hello world")
print(s)

s = util.reverse(s)
print(s)