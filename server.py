
from Pyro4 import locateNS, Proxy, Daemon
from rmiserver import EchoServer
from rotas import RoutesConfig
from Pyro4.errors import CommunicationError, NamingError


import sys

name_server = ''

while name_server.strip() == '':
    name_server = input('Qual o nome do servidor?: ')

echo_server = EchoServer(name_server)

try:
    ns = locateNS(RoutesConfig.HOST, RoutesConfig.PORT)
    server_names = ns.list('server-')
    keys = list(server_names.keys())

    for key in keys:
        each_server = Proxy(server_names[key])

        if key.split('server-')[1] == name_server:
            continue

        try:
            returned_messages = each_server.getMessages() #getMessage é metodo do EchoServer
            echo_server.messages_list = returned_messages[1]
            print('Mensagens recebida do servidor %s' % (returned_messages[0] ) ) 
            break
        except CommunicationError:
            pass

    with Daemon() as daemon:  #registra os servidores no pyro
        ns = locateNS(host=RoutesConfig.HOST, port=RoutesConfig.PORT)
        uri = daemon.register(echo_server)
        ns.register('server-' + name_server, uri)
        print('Servidor pronto!')
        daemon.requestLoop()

except NamingError:
    sys.exit(0)