#include <iostream>
using namespace std;

// Sendo n pessoas
//       k pulos
//       t sobrevivente

// Descobre qual é o sobrevivente
int josephus(int pessoas, int pulos) {
// i = 2 pois eh o valor minimo para realizar o algoritmo
// Vai matando cada pessoa, de 2 ate n pessoas
    if (pessoas == 1) {
      return 1;
    } else {
      return (josephus(pessoas - 1, pulos) + pulos - 1) % pessoas + 1;
    }
}

int main() {
  int qnt_testes, pessoas, pulos; 
  cin >> qnt_testes;
  
  for (int i = 0; i < qnt_testes; i++) {
  	
    cin >> pessoas;
    cin >> pulos;

    cout << "Case " << i + 1 << ": ";
    cout << josephus(pessoas, pulos) << endl;
  }
  return 0;
}
