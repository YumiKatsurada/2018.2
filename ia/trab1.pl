policia([Policia_X , Policia_Y]).
ladrao([Ladrao_X, Ladrao_Y]).

carro(2,3).
carro(4,5).
escada(1,1). % parcela baixa da escada

%acao(policia(X,Y), policia(X-1,Y)) :- pode_andar_horizontal(policia(X-1,Y)), write("andou esquerda").
%acao(policia(X,Y), policia(X+1,Y)) :- pode_andar_horizontal(policia(X+1,Y)), write("andou direita").
%acao(policia(X,Y), policia(X,Y+1)) :- pode_andar_subir(policia(X, Y+1)), write("andou cima").
%acao(policia(X,Y), policia(X,Y-1)) :- pode_andar_descer(policia(X, Y-1)), write("andou baixo").

acao([Policia_X, Policia_Y]) :- pode_andar_horizontal([Policia_X, Policia_Y]).

pode_andar_horizontal([Policia_X, Policia_Y]) :- Policia_X >= 0, Policia_X < 10, write("andou"). %, carrinho(X,Y).
pode_andar_subir(policia(X,Y)) :- Y>0 , Y<5, escada_subir(X,Y).
pode_andar_descer(policia(X,Y)) :- Y>0 , Y<5, escada_descer(X,Y).

% verifica se pode pular o carrinho
% nao pode haver escada, outro carrinho ou ladrao em um quadrado
% adjacente e nao pode estar do lado de uma parede

carrinho(X,Y) :- not(posEscada(X-1, Y)); not(posEscada(X+1, Y));
                 not(posCarrinho(X-1,Y)); not(posCarrinho(X+1, Y));
                 not(posLadrao(X-1, Y)); not(posLadrao(X+1, Y));
                 X\=0; X\=9.

escada_descer(X,Y) :- escada(X,Y-1).
escada_subir(X,Y) :- escada(X,Y).

meta([Policia_X, Policia_Y], [Ladrao_X, Ladrao_Y]).