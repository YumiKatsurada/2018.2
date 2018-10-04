"""
Implemente o protocolo TCP.

Para obter a nota completa, você deve implementar e exercitar (testar e comprovar que funcionam) os seguintes aspectos do protocolo TCP:

Estabelecer conexão (handshake SYN, SYN+ACK, ACK) com número de sequência inicial aleatório.
Transmitir e receber corretamente os segmentos.
Retransmitir corretamente segmentos que forem perdidos ou corrompidos.
Estimar o timeout para retransmissão de acordo com as recomendações do livro-texto (RFC 2988).
Implementar a semântica para timeout e ACKs duplos de acordo com as recomendações do livro-texto.
Tratar e informar corretamente o campo window size, implementando controle de fluxo.
Realizar controle de congestionamento de acordo com as recomendações do livro-texto (RFC 5681).
Fechar a conexão de forma limpa (lidando corretamente com a flag FIN).
"""

#sender.py

import sys
import socket
import thread
import threading
from threading import Thread
import time
from time import strftime
import struct
import os

#constantes

TAMMAXSEG = 576        #o arquivo sera dividido em segmentos deste tamanho para ser transferido


#------------------------------------------------------------------------------------------
#classe usada para descrever o remetente
class Sender:
    mensagem = [] #Lista para salvar arquivos
    tamanho_arquivo = 0 #Tamanho do arquivo lido

    #construtor - inicializa a classe com os valores passados
    def _init_(self, arquivo, remote_ip, remote_port, numero_ack_port, arquivo_log, tamanho_janela):
        self.nome_arquivo = arquivo
        self.remote_ip = remote_ip
        self.remote_port = remote_port
        self.num_ack_port = numero_ack_port
        self.arquivo_log = arquivo_log
        self.tam_janela = tamanho_janela

        return

#MÉTODOS DA CLASSE SENDER:

#exibe as variáveis da classe sender
def exibeSender:

    return

#lê os dados que serão enviados do arquivo
def le_arquivo(self):
    #Verifica o tamanho do arquivo
    tam_arquivo = os.stat(self.nome_arquivo) #stat da biblioteca os

    #abre o arquivo com nome especificado por linha de comando
    try:
        arq_dados = open(self.nome_arquivo, "r") #abre em modo de leitura
    except:
        print("arquivo não encontrado") #caso nao encontre o arquivo

    #Corta o arquivo em pedaços de acordo com o valor dado em TAMMAXSEG
    #ex: se o tamanho do arquivo for 100 e o tamanho max do segmento for 10, percorre
    #de 100/10 = 10 em 10, pegando 10 a cada vez
        
    for i in range(int(tam_arquivo.st_size/TAMMAXSEG)): #percorre o arquivo 
        pedaco = arq_dados.read(TAMMAXSEG)
        Sender.mensagem.append(pedaco) #adiciona o pedaço à mensagem a ser enviada
    pedaco = arq_dados.read(tam_arquivo.st_size % TAMMAXSEG) #pega o restante dos dados que nao couberam no ultimo pedaco
    Sender.mensagem.append(pedaco)

    #Fecha o arquivo
    arq_dados.close()

    return

#-------------------------------------------------------------------------------------------

#FUNÇÕES

def calcula_checksum(string): #~~~~~~ ENTENDER FUNCIONAMENTO, seção 3.3.2 do livro
    soma = 0

    #divide a string por 16 bits e calcula a soma
    for i in range(len(string)):
        if i % 2 == 0: #posiçao par
            #ord() devolve o cod numerico do caractere passado como parametro
            #<< 8 realiza um shift 
            soma = soma + (ord(string[i]) << 8)
        elif i % 2 == 1: #posiçao impar
            soma = soma + ord(string[i])

    #retorna o inverso da soma
    return 65535 - (soma % 65536)


    













    
    
        
