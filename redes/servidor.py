#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
servidor.py
Autora: Leila Aparecida da Silva
Etapa 1 do trabalho da disciplina de Redes de Computadores
Servidor TCP que cria um arquivo .txt com nome e conteúdo enviados pelo cliente.
"""

import socket 

host = ''
port = 8000

print "Servidor iniciado na porta", port
print "Aguardando cliente..."

#conexao entre dois ips
#sock_stream - tcp

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria um socket TCP/IP
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
s.bind((host, port)) #aguarda uma conexao
s.listen(1) #pode lidar com ate 1 conexao ao mesmo tempo 

cli, addr = s.accept() #recebe uma conexao e a aceita

print"\nCliente com IP ", addr[0], "conectado!"

name = cli.recv(100) #recebe até 100 bytes do cliente

name = name + '.txt' #concatena a extensão do arquivo

arq = open(name, 'w') #cria o arquivo em modo de escrita

while 1:
	dados = cli.recv(1024) #recebe o texto a ser escrito no arquivo
	if not dados:
		break
 	arq.write(dados)

print "\nArquivo ", name, " criado com o texto enviado pelo cliente ;) ", dados 

arq.close() #fecha o arquivo
cli.close() #encerra a conexão 

