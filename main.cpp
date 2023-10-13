#include <iostream>
#include <vector>
#include <map>
#include <string>

using namespace std;

// Funcao para calcular o fatorial de um número
int calcularFatorial(int n) {
    if (n <= 1) {
        return 1;
    }
    return n * calcularFatorial(n - 1);
}

int main() {
    // Entrada de dados
    int numero;
    cout << "Digite um numero: ";
    cin >> numero;

    // Condicional
    if (numero % 2 == 0) {
        cout << "O numero e par." << endl;
    } else {
        cout << "O numero e impar." << endl;
    }

    // Loop for
    cout << "Contagem regressiva de " << numero << " ate 1:" << endl;
    for (int i = numero; i >= 1; i--) {
        cout << i << " ";
    }
    cout << endl;

    // Manipulação de arrays (vector)
    vector<int> numeros;
    for (int i = 1; i <= 5; i++) {
        numeros.push_back(i);
    }
    cout << "Elementos do vetor: ";
    for (int num : numeros) {
        cout << num << " ";
    }
    cout << endl;

    // Manipulação de strings
    string nome = "Exemplo";
    cout << "Tamanho da string: " << nome.length() << endl;

    // Mapa (map)
    map<string, int> idadeMap;
    idadeMap["Alice"] = 25;
    idadeMap["Bob"] = 30;
    cout << "Idade de Alice: " << idadeMap["Alice"] << " anos" << endl;

    // Chamada de função
    int fatorial = calcularFatorial(numero);
    cout << "O fatorial de " << numero << " e " << fatorial << endl;

    return 0;
}
