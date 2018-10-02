#include <stdio.h>
#include <stdlib.h>

#define TAM 10

void bubble(int *v){
	for(int ultimo = TAM; ultimo > 0; ultimo--){
		for(int i = 0; i < ultimo; i++){
			if(v[i] > v[i+1]){ //se o elemento for maior que o proximo
				int aux = v[i]; //faz o swap
				v[i] = v[i+1];
				v[i+1] = aux;
			}
		}
	}
}

int main(){
	int v[TAM] = {55, 0, -78, -4, 32, 200, 52, 63, 69, 125};
	bubble(v);
	for(int i = 0; i < TAM; i++){
		printf("Elemento %d: %d\n", i, v[i]);
	}
	
	return 0; 
}
