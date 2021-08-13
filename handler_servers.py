import Pyro4
import sys
from rotas import RoutesConfig


def echo(method, *args):
  try:
    ns = Pyro4.locateNS(RoutesConfig.HOST, RoutesConfig.PORT)
    server_names = ns.list('server-') #nao mexer
    keys = list(server_names.keys())

    for key in keys:
      each_server = Pyro4.Proxy(server_names[key])

      try:
        return getattr(each_server, method)(*args)
      except Pyro4.errors.CommunicationError:
        pass
  except Pyro4.errors.NamingError:
      print('Não há nenhum servidor ativo')
      sys.exit(0)


# def get_servers():
#   ns = locateNS(RoutesConfig.HOST, RoutesConfig.PORT)
#   server_names = ns.list('server-')
#   return list(server_names.keys())