#include <iostream>
 
using namespace std;
 
int main() {
 
    float horas, velocidade;
    
    scanf("%f", &horas);
    scanf("%f", &velocidade);
    
    printf("%.3f\n", (horas * velocidade)/12.0);
 
    return 0;
}