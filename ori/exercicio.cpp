/* Esboce uma rotina em C ou C++ que aceite um ponteiro para uma cadeia de 
caracteres e retorne o comprimento dessa cadeia. Assuma que a representação 
de cadeia de caracteres usa como terminador o valor nulo (\0), o qual não
deve ser contado */

#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

#define TAM 100

int main(){
	
	char texto[] = "inconstitucionalissimamente";
	int i, tam;
	char letra;
	
	for(i = 0; i < sizeof(texto); i++){
		letra = texto[i];
		if(letra == '\0')
			tam = i;
	}
	
	printf("Comprimento: %d", tam);

    return 0; 
	
}