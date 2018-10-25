%policia(X,Y).
%ladrao(X,Y).

carro(2,3).
carro(4,5).
escada(1,1). %parcela baixa da escada

acao(andar_esquerda, policia(X,Y), policia(X-1,Y)) :- pode_andar_horizontal(policia(X-1,Y)).
acao(andar_direita, policia(X,Y), policia(X+1,Y)) :- pode_andar_horizontal(policia(X+1,Y)).
acao(andar_cima, policia(X,Y), policia(X,Y+1)) :- pode_andar_subir(policia(X, Y+1)).
acao(andar_baixo, policia(X,Y), policia(X,Y-1)) :- pode_andar_descer(policia(X, Y-1)).

pode_andar_horizontal(policia(X,Y)) :- X>=1, X<10, carrinho(X,Y).

pode_andar_subir(policia(X,Y)) :- Y>0 , Y<5, escada_subir(X,Y).

pode_andar_descer(policia(X,Y)) :- Y>0 , Y<5, escada_descer(X,Y).

%verifica se pode pular o carrinho
% nao pode haver escada, outro carrinho ou ladrao em um quadrado
% adjacente e nao pode estar do lado de uma parede

carrinho(X,Y) :- not(posEscada(X-1, Y)); not(posEscada(X+1, Y));
                             not(posCarrinho(X-1,Y)); not(posCarrinho(X+1, Y));
                             not(posLadrao(X-1, Y)); not(posLadrao(X+1, Y));
                             X\=0; X\=9.

escada_descer(X,Y) :- escada(X,Y-1).
escada_subir(X,Y) :- escada(X,Y).

meta(policial(X,Y), ladrao(X,Y)).
