from Pyro4 import locateNS, Proxy
import sys
from rotas import RoutesConfig
from Pyro4.errors import CommunicationError, NamingError


def get_servers():
  ns = locateNS(RoutesConfig.HOST, RoutesConfig.PORT)
  server_names = ns.list('server-')
  return server_names

def echo(method, *params): #params = mensagem digitada
  try:
    servers = get_servers()
    server_keys = list(servers.keys())
    
    for key in server_keys:
      connection = Proxy(servers[key])

      try:
        return getattr(connection, method)(*params)
      except CommunicationError:
        pass
  except NamingError:
      print('Não há nenhum servidor ativo')
      sys.exit(0)