#include <iostream>
 
using namespace std;
 
int main() {
 
    int k2, k3, k5, k6;

    scanf("%d %d %d %d", &k2, &k3, &k5, &k6);

    int soma = 0;
    
    while((k2 > 0) && (k5 > 0) && (k6 > 0)){
        soma += 256;
        k2--;
        k5--;
        k6--;
    }

    while((k3 > 0) && (k2 > 0)){
        soma += 32;
        k3--;
        k2--;
    }

    printf("%d\n", soma);

    return 0;
}