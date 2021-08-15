
### Executando a aplicação

Necessario ter python 3.x instalado.

1 - Abra o terminal e execute 
```bash
pip3 install -r library.txt
```

2 - Execute o servidor pyro
```python
python3 -m Pyro4.naming
```

3 - Em um novo terminal execute o servidor 
```python
python3 server.py
```

4 - Em outro terminar execute o cliente
```python
python3 client.py
```


### Para validar a replicação:

- envie mensagens 
- liste as mensagens
- suba um novo servidor
- desligue o 1o control+d
- liste as mensagens novamente
