#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import socket

print("servidor iniciado, aguardando cliente")

host = ''
port = 8000

#conexao entre dois ips
#sock_stream - tcp
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port)) #aguarda uma conexao
s.listen(1) #pode lidar com ate 1 conexao ao mesmo tempo (tentar mudar isso depois)

cli, addr = s.accept() #recebe uma conexao e a aceita
arq = open('teste.txt', 'w') #abre em modo de escrita arquivo que vai receber as informacoes

while 1:
	dados = cli.recv(1024)
	if not dados:
		break
 	arq.write(dados)

arq.close()
cli.close()






"""
while True:
    cli, addr = s.accept() #recebe uma conexao e a aceita

    print('Servidor conectado por ', addr)

    dados = b''
    contador = 0
    while not b'F' in dados:   # experimente não colocar este while
        dados += cli.recv(1000000)
        contador += 1
    print('Recebi %d bytes' % len(dados))
  #  cli.send('recebido pelo servidor' + dados)

print('Executei recv() %d vezes' % contador)

"""
