
# O que é?

App desenvolvido para a disciplina de sistemas distribudos que utiliza a replicação para lidar com a tolerância a falhas em um sistema distribuído.


## Executando a aplicação

Necessario ter Python 3.5+ instalado.

1 - Instale as dependencias
```bash
pip3 install -r library.txt
```

2 - Inicie o servidor pyro
```python
python3 -m Pyro4.naming
```

3 - Em um novo terminal execute o servidor do app
```python
python3 server.py
```

4 - Em outro terminar execute o client do app
```python
python3 client.py
```


### Para validar a replicação:

- envie uma (ou mais) mensagens 
- liste as mensagens
- suba um novo servidor
- desligue o 1o 
- liste as mensagens novamente
