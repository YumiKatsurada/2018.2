#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import socket

host = ''
port = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

#s.send(b'A'*50000 + b'F')

texto = raw_input("insira o texto a ser enviado para o servidor")

s.send(texto)

s.close()


