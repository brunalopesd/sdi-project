
from Pyro4 import locateNS, Proxy, Daemon
from rmiserver import EchoServer
from rotas import RoutesConfig
from handler_servers import get_servers
from Pyro4.errors import CommunicationError, NamingError


import sys

name_server = ''

while name_server.strip() == '':
    name_server = input('Qual o nome do servidor?: ')

echo_server = EchoServer(name_server)

try:    
    servers_names = get_servers()
    server_list = list(servers_names.keys())

    for server in server_list:
        each_server = Proxy(servers_names[server])

        if server.split('server-')[1] == name_server:
            continue

        try:
            returned_messages = each_server.get_messages()
            echo_server.messages_list = returned_messages
            print('Mensagens recebidas do servidor %s' % (returned_messages[0] )) 
            break
        except CommunicationError:
            pass

    with Daemon() as daemon:  #registra os servidores no pyro
        ns = locateNS(RoutesConfig.HOST, RoutesConfig.PORT)
        uri = daemon.register(echo_server)
        ns.register('server-' + name_server, uri)
        print('Servidor pronto!')
        daemon.requestLoop()

except NamingError:
    sys.exit(0)