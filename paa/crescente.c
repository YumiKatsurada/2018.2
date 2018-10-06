//Escreva uma função que verifique se um vetor v[0..n-1] está em ordem crescente. 

#include <stdio.h>
#include <stdlib.h>

#define TAM 5

int ordemCrescente(int* v){
	int cresc = 1;
	for(int i = 0; i < TAM; i++){
		if(v[i] > v[i+1]){
			cresc = 0;
		}
	}
	
	return cresc; //1 - esta em ordem crescente / 0 - nao esta 
}

int main(){
	
	int vetor[TAM] = {1, 2, 3, 4, 5}; //pode ser mudado para ler os valores
	
	if(ordemCrescente(vetor)){
		printf("Esta em ordem crescente");
	} else{
		printf("Nao esta em ordem crescente");
	}
	
	return 0;
}
