#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
cliente.py
Autora: Leila Aparecida da Silva
Etapa 1 do trabalho da disciplina de Redes de Computadores
Cliente TCP que envia um nome e um conteúdo para um arquivo .txt a ser criado no servidor.
"""

import socket

host = ''
port = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria um socket TCP/IP
s.connect((host, port)) #conecta ao host na porta indicada

nome = raw_input("Insira o nome do arquivo a ser criado:")

s.send(nome) #envia os bytes do nome

texto = raw_input("\nInsira o texto a ser enviado para o servidor:")

s.send(texto) #envia os bytes do conteúdo do texto

s.close() #encerra a conexão 


