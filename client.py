import os
from handler_servers import echo

if __name__ == "__main__":
  contador = 1
  list_messages = []

  while (contador > 0) :
    print('')
    print('---------Menu--------- \n')
    print('1 Enviar uma mensagem')
    print('2 Listar Mensagens')
    print('3 Sair')
    print('')
    
    try:
      option = int(input('Selecione uma opção: '))

      if option == 1:
        os.system('clear')
        message = input('Escreva sua mensagem: ')
        send_message = echo('echoService', message)
      
      elif option == 2:
        os.system('clear')
        returned_message = echo('get_messages')
        print(returned_message[1])
            

      elif option == 3:
        os.system('clear')
        print('Encerrando sessão...')
        contador = 0
      else:
        print("\n")
        print("**** Selecione uma opção válida ****")
    
    except ValueError:
      print("**** Selecione uma opção válida ****")