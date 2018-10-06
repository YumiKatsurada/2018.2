/*Considere a ordenação de n números armazenados no arranjo A,
localizando primeiro o menor elemento de A e permutando esse elemento com o
elemento contido em A[1]. Em seguida, encontre o segundo menor elemento de
A e o troque pelo elemento A[2]. Continue dessa maneira para os primeiros n - 1
elementos de A. Escreva o pseudocódigo para esse algoritmo, conhecido como
ordenação por seleção. Que loop invariante esse algoritmo mantém? Por que
ele só precisa ser executado para os primeiros n - 1 elementos, e não para todos
os n elementos? Forneça os tempos de execução do melhor caso e do pior caso
da ordenação por seleção em notação T.


Que loop invariante esse algoritmo mantém? 
O loop for externo (de i), de modo que:
v[0..i-1] está em ordem crescente e 
v[i-1] <= v[k] qualquer que seja k em i..n 

Por que ele só precisa ser executado para os primeiros n - 1 elementos, e não para todos
os n elementos? 



Forneça os tempos de execução do melhor caso e do pior caso
da ordenação por seleção em notação T.
*/

#include <stdio.h>
#include <stdlib.h>

void selection_sort(int *v, int n){
	//localiza o menor elemento
	int aux, menor;
	for(int i = 0; i < n; i++){
		menor = i;
		for(int j = i+1; j < n; j++)
		{	
			if(v[j] < v[menor]){
			menor = j;
			}
		}
		//faz o swap
		aux = v[i];
		v[i] = v[menor];
		v[menor] = aux;
	}
}

int main(){
	
	int vetor[5] = {3, 1, 4, 2, 5};
	selection_sort(vetor, 5);
	
	for (int i = 0; i < 5; i++){
		printf("V[%d] = %d\n", i, vetor[i]);
	}
	
	return 0;
}
