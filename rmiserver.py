from Pyro4 import expose
from Pyro4 import locateNS, Proxy
from Pyro4.errors import CommunicationError

from rotas import RoutesConfig


@expose #deixa a classe exposta pro objeto remoto acessar 
class EchoServer(object):

    def __init__(self, name_server):
        self.messages_list = list()
        self.name_server = name_server

    def send_msg_replicas(self, name_server, message):
        ns = locateNS(RoutesConfig.HOST, RoutesConfig.PORT)
        server_names = ns.list('server-')
        keys = list(server_names.keys())

        for key in keys:
            each_server = Proxy(server_names[key])
            try:
                each_server.get_replicas_message(name_server, message)
            except CommunicationError:
                print('Erro no envio da mensagem')

    def get_replicas_message(self, name_server, message):
        print('Mensagem recebida do servidor ' + name_server)
        self.messages_list.append(message)

    def echo_service(self, message):
        self.send_msg_replicas(self.name_server, str(message))
        return str(message)

    def get_messages(self):
        return (self.messages_list)