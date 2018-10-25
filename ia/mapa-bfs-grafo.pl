%define que as arestas nao sao direcionadas
aresta(V1,V2) :- aresta(V2,V1).

:-discontiguous aresta/2.

resolva(N,[N]) :- final(N). %alcançou a meta
% s(N,N1) - faça um movimento valido / resolva(N1,Caminho) - recurs.
resolva(N,[N|Caminho]) :- s(N,N1), resolva(N1,Caminho).
s(N,N1) :- aresta(N,N1). %caminho valido se tem aresta

%%%%%%%%%%%%%% andar1 - horizontal
aresta(a1,b1).
aresta(b1,c1).
aresta(c1,d1).
aresta(d1,e1).
aresta(e1,f1).
aresta(f1,g1).
%aresta(g1,h1). carrinho
%aresta(h1,i1). carrinho
aresta(i1,j1).

%%%%%%%%%%%%%% andar2 - horizontal
aresta(a2,b2).
%aresta(b2,c2). carrinho
%aresta(c2,d2). carrinho
aresta(d2,e2).
aresta(e2,f2).
aresta(f2,g2).
aresta(g2,h2).
aresta(h2,i2).
aresta(i2,j2).

%%%%%%%%%%%%%% andar3 - horizontal
aresta(a3,b3).
aresta(b3,c3).
%aresta(c3,d3). carrinho
%aresta(d3,e3). carrinho
aresta(e3,f3).
aresta(f3,g3).
aresta(g3,h3).
aresta(h3,i3).
aresta(i3,j3).

%%%%%%%%%%%%%% andar4 - horizontal
aresta(a4,b4).
aresta(b4,c4).
aresta(c4,d4).
aresta(d4,e4).
aresta(e4,f4).
aresta(f4,g4).
aresta(g4,h4).
aresta(h4,i4).
aresta(i4,j4).

%%%%%%%%%%%%%% andar5 - horizontal
aresta(a5,b5).
%aresta(b5,c5). carrinho
%aresta(c5,d5). carrinho
%aresta(d5,e5). carrinho
aresta(e5,f5).
aresta(f5,g5).
aresta(g5,h5).
aresta(h5,i5).
aresta(i5,j5).

%%%%%%%%%%%%%% escadas
aresta(i1,i2).
aresta(b1,b2).
aresta(e2,e3).
aresta(c3,c4).
aresta(h3,h4).
aresta(j3,j4).
aresta(a4,a5).
aresta(f4,f5).

final(j5). %posiçao do ladrao

%define que as arestas nao sao direcionadas
%aresta(V1,V2) :- aresta(V2,V1). 









