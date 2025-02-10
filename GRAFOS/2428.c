#include <stdio.h>

int main() {

int A, B, C, D;
scanf("%d %d %d %d",&A, &B, &C, &D);

		if ((A*B == C*D) || (A*D == B*C) || (A*C == D*B)) { // Se uma das combinações for para a formação do retangulo for verdadeira,ele retorna sim.  
			printf("S\n");
		}
		 else {
			printf("N\n"); // Caso não forme o retangulo ele retorna não.
		}
	
	return 0;
}
